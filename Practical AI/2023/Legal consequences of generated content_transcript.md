[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[43.14 --> 46.40]  Welcome to another episode of Practical AI.
[46.72 --> 48.28]  This is Daniel Whitenack.
[48.38 --> 55.22]  I'm a data scientist and founder of PredictionGuard, and I'm joined as always by my co-host, Chris
[55.22 --> 58.48]  Benson, who is a tech strategist at Lockheed Martin.
[58.98 --> 59.62]  How are you doing, Chris?
[60.04 --> 60.86]  Doing well.
[60.96 --> 61.48]  Doing well.
[61.68 --> 65.90]  I'm really excited about today because there's so many questions you and I have brought up
[65.90 --> 70.30]  in the show without the ability to answer, and I know we might get some answers today.
[70.68 --> 70.98]  Yes.
[71.00 --> 77.38]  And actually, this one, not only will it be super practical and interesting, but it's
[77.38 --> 81.48]  also a tip from one of our listeners who suggested this guest.
[81.48 --> 87.44]  So we're really excited to have with us Damien Reel, who is a lawyer and technologist with
[87.44 --> 91.94]  experience in litigation and digital forensics and software development.
[92.20 --> 93.04]  So welcome, Damien.
[93.40 --> 94.34]  Thank you so much for having me.
[94.40 --> 95.06]  I'm thrilled to be here.
[95.26 --> 95.54]  Yeah.
[95.70 --> 103.48]  I feel very selfish this episode because I just have like a million sort of like legal implications,
[103.96 --> 109.28]  copyright questions related to like generative AI, large language models, all sorts of things.
[109.28 --> 117.64]  But before we get into some of those specifics, I know over the course of this show, we have
[117.64 --> 124.28]  commented on various things that have come about, like GDPR and then California data privacy
[124.28 --> 124.88]  stuff.
[125.00 --> 130.16]  And now we have like the EU AI Act and all of this sort of regulation stuff.
[130.26 --> 135.14]  And then you've got other things on the other side on the litigation front where companies
[135.14 --> 143.62]  are, you know, getting sued for code generation based on maybe questionable training of models
[143.62 --> 144.36]  and other things.
[144.50 --> 149.84]  So maybe before we get in from someone who is an expert in this area and thinking about
[149.84 --> 157.76]  it all the time, how do you view where we're at in relation to AI technology and regulation
[157.76 --> 160.26]  and kind of the legal side of things?
[160.26 --> 164.32]  How are those things catching up to one another or outpacing one another?
[164.52 --> 168.36]  And where are we at now as opposed to like maybe a year ago?
[168.46 --> 169.16]  What's changed?
[169.70 --> 169.80]  Sure.
[169.96 --> 173.84]  And maybe before I answer that, a brief, I litigated for about 20 years.
[173.96 --> 175.58]  So I was a litigator for about 20 years.
[175.66 --> 176.72]  I did tech litigation.
[176.96 --> 180.60]  So I'm coming to this from a perspective as a lawyer, but I've also been a coder since
[180.60 --> 181.10]  1985.
[181.50 --> 182.82]  So I have the law plus tech background.
[183.00 --> 186.80]  So for your listeners' benefit, I'm not just a stuffed shirt that doesn't know what he's
[186.80 --> 187.26]  talking about.
[187.26 --> 191.44]  I can walk the tech walk and talk the legal talk, if you will.
[192.02 --> 199.72]  So really, as far as regulation, having litigated since 2002, I've seen ways that the EU and
[199.72 --> 202.52]  the United States have tried to regulate technology.
[202.74 --> 209.64]  And of course, they've had various degrees of failure, I would say, largely because the
[209.64 --> 213.00]  three of us know exactly how lots of technology works.
[213.04 --> 216.32]  But sadly, the congresspeople and the regulators do not.
[216.32 --> 222.46]  And so it's really the law is by nature slow and trying to get up to speed on a fast moving
[222.46 --> 224.26]  area such as AI is very difficult.
[224.42 --> 229.66]  So I would say that, you know, if past is prologue, I don't anticipate much good things
[229.66 --> 231.70]  coming out of regulation of AI in the near future.
[232.14 --> 240.00]  Some of these things are related to like this generative wave of AI where people are generating
[240.00 --> 242.04]  a lot of content with AI.
[242.04 --> 244.66]  I know that also you have a background.
[244.80 --> 249.66]  You mentioned your sort of coding background, but you also have a background with generative
[249.66 --> 250.56]  technologies.
[251.08 --> 255.88]  You know, maybe not like some with large language models and other things, but I know you have
[255.88 --> 260.48]  a very interesting story of some generative things that you did with with music.
[260.60 --> 261.66]  Could you describe some of that?
[262.16 --> 262.66]  Yeah, absolutely.
[262.66 --> 266.30]  So I have both my current state with my job that pays me money.
[266.42 --> 269.42]  That is with Vlex, where I'm doing lots with large language models right now.
[269.54 --> 273.00]  We have a billion legal documents that we're running large language models across and doing
[273.00 --> 275.08]  embeddings to be able to do outputs.
[275.48 --> 279.78]  For example, a legal research memorandum and eventually be able to provide emotions, briefs,
[279.82 --> 280.72]  pleadings, that sort of thing.
[280.76 --> 282.56]  So that's my my job that pays me money.
[282.64 --> 286.52]  And for the job that doesn't pay me money at all, which you referenced, is my all the music
[286.52 --> 286.94]  project.
[286.94 --> 292.46]  This is a project that I started with my friend, Noah Rubin, who one thing your listeners might
[292.46 --> 295.58]  find interesting is that around 2018, I did cybersecurity.
[295.90 --> 299.82]  The biggest thing I did was that Facebook hired me and my company to investigate Cambridge
[299.82 --> 300.24]  Analytica.
[300.50 --> 304.60]  So I spent a year of my life on Facebook's campus with Facebook's data scientists and my
[304.60 --> 309.42]  former FBI, CIA, NSA people that worked with me to figure out how bad guys use Facebook
[309.42 --> 309.70]  data.
[309.96 --> 312.02]  Did that for about 50 some weeks in a row.
[312.40 --> 315.70]  The stuff we would do on Monday would make the New York Times and the Times of London by Friday.
[315.70 --> 321.30]  So at the end of a 14 hour day on the Facebook campus, I retreated to my hotel with Noah Rubin,
[321.36 --> 321.78]  my friend.
[322.18 --> 326.88]  We were in the lounge and over a beer, I said, do you know, Noah, how we can brute force passwords
[326.88 --> 328.96]  by going A, A, A, B, A, C?
[329.46 --> 332.46]  I said, what if we could do that with music where we would go do, do, do, do, do, do,
[332.46 --> 336.22]  do, do, ray, do, do, do, me, do, do, fa until we mathematically exhausted every melody
[336.22 --> 338.80]  that's ever been and every melody that ever can be.
[339.32 --> 342.22]  And so he said F, yeah, but he didn't say F, yeah.
[342.22 --> 346.74]  So within a few hours, he had a prototype where he cranked out 3,000 melodies.
[347.18 --> 352.18]  To date, we've now cranked out 471 billion melodies with a B, mathematically exhausting
[352.18 --> 354.18]  every melody that's ever been and ever can be.
[354.54 --> 355.90]  We've written all those to disk.
[356.06 --> 358.46]  Once they're written to disk, they're copyrighted automatically.
[358.76 --> 361.08]  So we've copyrighted 471 billion melodies.
[361.50 --> 364.94]  And then we placed everything in the public domain to be able to protect, to use to all my
[364.94 --> 366.20]  melody lawsuit defendants.
[366.20 --> 371.62]  And so the idea is that before my talk in 2019, every defendant in one of those lawsuits
[371.62 --> 372.26]  has lost.
[372.74 --> 377.40]  After my talk, which has been seen 2 million times, every defendant has used largely my
[377.40 --> 378.60]  arguments and has won.
[378.88 --> 383.48]  And my arguments are largely that maybe if a machine cranks this thing out at 300,000
[383.48 --> 388.44]  melodies per second, maybe we shouldn't give one person a monopoly, which is a copyright,
[388.60 --> 393.28]  a monopoly of life of the author plus 70 years for what the machine cranked out in a millisecond.
[393.28 --> 398.24]  So that's largely my all the music project, which goes to, it is in a sense generative
[398.24 --> 398.58]  AI.
[398.74 --> 401.18]  It's a brute force generative AI, but it's generative AI.
[401.64 --> 406.10]  But the real question is if the output of that is copyrightable, essentially if carpet
[406.10 --> 411.00]  bombed the entirety of every melody that's ever been, and if I were a megalomaniac, I
[411.00 --> 412.40]  would sue everybody, right?
[412.44 --> 412.82]  But I'm not.
[412.88 --> 413.82]  I put them all in the public domain.
[413.98 --> 418.56]  But if machine generated works are copyrightable, these are the bad things that can happen.
[419.00 --> 419.70]  I love that story.
[419.84 --> 420.58]  I just want to say that.
[420.96 --> 421.60]  It's pretty fun.
[421.60 --> 426.96]  And because it's been seen so many times now, 2 million, I've been able to meet with
[426.96 --> 428.14]  some good friends now.
[428.56 --> 432.60]  There's, for example, the former chief economist of Spotify I'm now friends with, and the guy
[432.60 --> 437.02]  who was responsible for the first commercial MP3 to be downloaded, Jim Griffin, I'm friends
[437.02 --> 437.30]  with him.
[437.50 --> 439.62]  So anyway, so it's opened a lot of doors for me.
[440.06 --> 440.52]  That's awesome.
[440.94 --> 448.16]  And one thing that comes to my mind as you're talking about that is because I'm also a musician,
[448.16 --> 453.36]  and I think a lot of people would think of, oh, these sort of melodies or chord progressions
[453.36 --> 454.98]  or however you want to frame it.
[455.32 --> 458.98]  There's a very human element to that that involves creativity.
[458.98 --> 464.32]  And I think this would maybe be extended to if we think about knowledge work more generally,
[464.32 --> 471.00]  whether that's like you being a lawyer and writing briefs or us being programmers and
[471.00 --> 474.86]  writing code or marketers being marketers and writing copy.
[475.02 --> 481.82]  Right now, these generative models can generate a lot of those things in a very compelling.
[481.82 --> 487.86]  And even I think people would perceive it as a very creative way, however you think about
[487.86 --> 489.54]  that creativity and coherence.
[490.04 --> 495.10]  So in your own work, maybe it's on the lawyer side or the coding side.
[495.56 --> 499.88]  How is that project and maybe some of the work you do day to day with large language models,
[499.98 --> 505.96]  how is that shaping how you think about this sort of knowledge work and the output of humans
[505.96 --> 508.22]  versus the output of models?
[508.22 --> 510.32]  I would say two aspects to this.
[510.44 --> 514.72]  And I think that the word creative is ambiguous, as all words are, most words are.
[515.00 --> 521.04]  And it is, you know, when I generated 471 billion melodies, I was creating those melodies.
[521.04 --> 523.58]  But it was by no means creative, right?
[523.88 --> 525.02]  So in that way, you know,
[525.60 --> 530.92]  those are just mathematically exhausting everything that's ever been.
[531.36 --> 535.36]  So that is a very simple version of what large language models do, right?
[535.36 --> 538.68]  Just saying, what is the statistically next sentence, right?
[539.06 --> 544.14]  And so this really gets to the heart of what we think human creativity is, right?
[544.22 --> 545.90]  Is it creative as in brute forcing?
[546.16 --> 551.58]  Or is it truly lightning in a bottle creativity that we want to protect with intellectual property
[551.58 --> 552.94]  laws and other things like that?
[553.30 --> 557.60]  I think what we're learning from my project and from the large language models is that maybe
[557.60 --> 561.46]  human creativity ain't as special as we think it is.
[561.46 --> 568.02]  As an example, on a Tuesday, a jury found that Katy Perry had violated a copyright of a melody
[568.02 --> 568.96]  that sounded like this.
[569.26 --> 571.08]  Dun, dun, dun, dun, dun, dun, dun, dun.
[571.48 --> 572.22]  That was on a Tuesday.
[572.88 --> 580.74]  On my talk on a Saturday, I said that my, that particular melody shows up in my data set 8,128 times.
[581.06 --> 586.60]  So Katy Perry got dinged for $2.8 million over something that I had thousands of times just
[586.60 --> 587.28]  through brute force.
[587.72 --> 589.64]  So was that melody creative?
[589.64 --> 591.88]  No, it was just a brute force.
[592.36 --> 597.48]  After my talk was made public, the judge actually went back and reversed the jury verdict saying
[597.48 --> 600.48]  that melody was so unoriginal as to be uncopyrightable.
[600.78 --> 602.26]  Essentially what I was arguing my TED talk.
[602.52 --> 607.26]  I think going to the heart of what is human creativity, it's good that we have large language
[607.26 --> 610.76]  models and projects like mine to be able to go to the heart of there are some things that
[610.76 --> 613.88]  we should protect and there are some things that are just unprotectable because they're
[613.88 --> 614.24]  unoriginal.
[614.70 --> 618.74]  You're putting an obstacle against what was otherwise maybe the weaponization of IP.
[618.74 --> 620.24]  Is that a fair way of putting that?
[620.70 --> 621.06]  A hundred percent.
[621.14 --> 622.68]  We're using it as a shield, not a sword.
[622.90 --> 623.04]  Right.
[623.28 --> 628.14]  Which I like because it's having seen a lot of, for a non-attorney as having seen a lot
[628.14 --> 632.54]  of IP concerns out there in business, sometimes you're just kind of like, there's not much
[632.54 --> 632.78]  there.
[633.06 --> 633.24]  So.
[633.70 --> 634.06]  Absolutely.
[634.24 --> 636.32]  And so I did that with the copyright side.
[636.46 --> 640.52]  My friend, Mike Bomarito, who was one of the guys who you may have heard beat the
[640.52 --> 641.00]  bar exam.
[641.16 --> 644.14]  They use GPT-4 to beat 90% of humans on the bar exam.
[644.26 --> 645.40]  One of those was Mike Bomarito.
[645.40 --> 648.56]  Mike approached me and said, I love what you did with copyrights.
[648.56 --> 650.22]  Wouldn't be great to do that for patents.
[650.66 --> 654.08]  And so right now we're doing, I was doing all the music project.
[654.18 --> 656.00]  We're now doing all the patents project.
[656.46 --> 660.82]  What that project is, is going to be taking all, all the patents that have ever been filed,
[661.12 --> 665.68]  taking each of the claims for each of those patents, putting those claims together in
[665.68 --> 667.74]  vector space and clustering them that way.
[667.74 --> 673.12]  And then generating every possible combination of all of those claims in all those existing
[673.12 --> 673.56]  patents.
[673.86 --> 679.26]  So if anyone in the future tries to recombine any existing claim into a new thing, they
[679.26 --> 683.32]  can point to our thing as prior art to be able to say, no, no, no, Bomarito, Real Cats,
[683.40 --> 684.18]  and maybe Rubin.
[684.32 --> 685.72]  They already did that in 2023.
[686.04 --> 689.36]  You can't do that again because they did that as prior art.
[689.36 --> 696.02]  As both a coder and a lawyer who I'm assuming some of these things you're generating are
[696.02 --> 702.90]  generated, but I'm also assuming in your day-to-day work and in your day-to-day coding, there are
[702.90 --> 708.52]  portions of what you're doing still that are not completely generated, or at least that you're
[708.52 --> 709.52]  editing heavily.
[709.52 --> 717.54]  How has this type of work influenced how you think about your own job moving into the future,
[718.26 --> 724.30]  working alongside these models, or at least in an environment where these models exist?
[724.94 --> 730.00]  So I will say, and anyone who works with me will agree that I am a coder, but I'm a crappy
[730.00 --> 730.42]  coder.
[730.60 --> 732.80]  I'm probably one of the worst coders you're ever going to meet.
[732.88 --> 736.60]  So a lot of my work with large language models is in the textual area rather than the code
[736.60 --> 736.98]  area.
[736.98 --> 741.06]  But in the textual area, I'll give you an anecdote that answers your question.
[741.52 --> 745.32]  I was reached out by the editor of a large legal magazine to say, hey, Damien, I want
[745.32 --> 746.76]  you to write the cover story on GPT.
[746.96 --> 748.60]  I said, how long do you want it to be?
[748.66 --> 750.60]  He said about 17 double-spaced pages.
[750.80 --> 754.86]  And I was like, man, I don't have time because my rule of thumb is one hour per double-spaced
[754.86 --> 755.24]  page.
[755.30 --> 757.36]  So that's 17 hours that I just don't have time to do.
[757.78 --> 759.86]  But then I realized, oh, wait, the topic is GPT.
[760.12 --> 763.88]  So what I did is I created an outline of headings and subheadings.
[763.88 --> 765.32]  That's about two pages worth.
[765.32 --> 769.32]  And I said to GPT, for each of the bullet points, give me four sentences, essentially
[769.32 --> 770.90]  a paragraph for each of the bullet points.
[771.10 --> 771.68]  And it out.
[771.98 --> 773.26]  That was my one for the day.
[773.56 --> 774.88]  Crapped out the 15 pages worth.
[775.06 --> 780.64]  And then I spent the next three hours editing, moving, adding, working with the text, not
[780.64 --> 783.98]  accepting the 15 pages outright, but working with the text and regenerating.
[784.14 --> 786.04]  And then I got it out the door three hours later.
[786.04 --> 787.78]  And the editor's like, oh, this is perfect.
[787.94 --> 788.84]  I don't need any edits.
[788.88 --> 789.68]  Let's get it out the door.
[789.68 --> 793.16]  So that took a 17-hour project down to three hours.
[793.66 --> 798.18]  That's thing number one, is that this is not just accepting the machine output as is, but
[798.18 --> 803.00]  it's really us using the output as an assistant, much like Copilot on GitHub is using it as
[803.00 --> 803.74]  an assistant, right?
[803.80 --> 807.90]  These are essentially pair coding, if you will, co-authoring with the machine.
[807.90 --> 813.16]  I was doing a talk with the U.S. Copyright Office Assistant General Counsel.
[813.68 --> 817.52]  And he was talking about the regulations that they're putting out, saying that if machine
[817.52 --> 819.52]  generated, therefore uncopyrightable.
[819.72 --> 822.02]  If human generated, therefore copyrightable.
[822.22 --> 826.28]  And if machine generated, you have to be able to disclose what aspects of the thing is
[826.28 --> 826.94]  machine generated.
[827.58 --> 832.50]  So if you think about if I were to file a copyright registration with my article that I just drafted,
[833.00 --> 834.80]  what extent was that machine generated?
[835.08 --> 836.84]  And what extent was that human generated?
[836.84 --> 839.34]  Because I spent three hours adding, editing.
[839.54 --> 844.76]  If the machine generated in a sentence three of the words that were unmolested by me, and
[844.76 --> 850.40]  the other 20 words in the sentence were actually mine, do I have to disclose what three words
[850.40 --> 852.76]  were machine generated versus the ones that I edited?
[853.16 --> 854.20]  And that's with text.
[854.74 --> 856.38]  How would I do that with music, right?
[856.40 --> 860.78]  If I said to the machine, hey, generate a melody, and generate a chord structure, and generate
[860.78 --> 861.16]  lyrics.
[861.16 --> 864.16]  And then I spent from 1 a.m. to 3 a.m.
[864.16 --> 867.22]  Rearranging all those things, and then getting out the door.
[867.62 --> 871.04]  If the copyright office said what aspects of that was human generated and what's machine
[871.04 --> 873.46]  generated, I would honestly say, I have no friggin' idea.
[873.78 --> 877.96]  Because there's no track changes with my DAW that I make my music on, right?
[877.98 --> 878.92]  There's no track changes.
[879.38 --> 881.88]  I didn't track changes on my lyrics that I messed around.
[882.34 --> 887.28]  So I think this idea of trying to bifurcate what is machine created and what is human created
[887.28 --> 890.18]  is a fool's errand, and we're really going to have to reckon with that.
[890.86 --> 897.84]  Well, Damian, I have some very selfish questions that I've been pondering over in my own life
[897.84 --> 899.32]  as I've encountered them.
[899.80 --> 904.64]  And hopefully this won't seem like popcorn questions, because I think it's very related
[904.64 --> 905.76]  to what you're talking about.
[905.76 --> 913.56]  But I think practical developers are hitting these snags as they're developing apps with
[913.56 --> 917.82]  this technology that are entering a sort of gray zone.
[917.96 --> 919.74]  So I'd love to get your thoughts on a few of these.
[920.20 --> 925.66]  One example that I can think of is a lot of people are building chat interfaces.
[926.08 --> 930.78]  It's very popular now to say, oh, build a chat interface over a website, or build a chat
[930.78 --> 934.56]  interface over documents, or build a chat interface over data.
[934.56 --> 936.04]  Something like that.
[936.10 --> 937.84]  But people are doing this very frequently.
[938.02 --> 938.88]  It's very useful.
[939.42 --> 945.88]  My question is, that chat interface or those messages are generated content, right?
[945.94 --> 948.00]  And that's what the user is seeing.
[948.24 --> 953.70]  But I see this huge gray area where, let's say that I want to chat with Harry Potter, right?
[953.84 --> 958.36]  I take the book of Harry Potter, and I put it in my vector database.
[958.46 --> 962.46]  And someone asks a question of Harry Potter, and I go retrieve the content.
[962.46 --> 965.42]  I'm just injecting that into a prompt, right?
[965.58 --> 970.28]  And I'm sending the prompt with, I guess, the book content into a model.
[970.38 --> 973.32]  The model's outputting some generated answer.
[973.48 --> 975.76]  And I'm sending that to the user.
[976.06 --> 982.32]  Now, I'm assuming, you know, I'm no lawyer, but I'm assuming I can't sell a new copy of
[982.32 --> 986.36]  Harry Potter unless I have certain rights and agreements in place.
[986.36 --> 991.78]  But what if I put this, you know, interface up on the internet and I start selling access
[991.78 --> 992.20]  to it?
[992.24 --> 998.08]  So I guess with that kind of very real world scenario, what sorts of elements do I need
[998.08 --> 998.84]  to consider there?
[998.92 --> 1001.96]  And what's known to have a good answer?
[1002.10 --> 1003.02]  What's gray area?
[1003.28 --> 1006.62]  What's kind of being maybe being litigated right now?
[1007.22 --> 1008.52]  I'm going to answer your question.
[1008.70 --> 1010.24]  And it's going to be a fun walk.
[1010.30 --> 1011.40]  So take a walk with me.
[1011.56 --> 1012.34]  Okay, perfect.
[1012.34 --> 1016.66]  So this walk, it's going to begin with the Google Books project.
[1016.90 --> 1020.90]  So you might remember the Google Books ingested every book that ever existed, perhaps also
[1020.90 --> 1022.02]  including the Harry Potter book.
[1022.52 --> 1027.02]  A bunch of publishers said, hey, no fair, because you can't ingest all these things because these
[1027.02 --> 1027.84]  things are copyrighted.
[1027.90 --> 1029.24]  Every one of these books is copyrighted.
[1029.32 --> 1029.80]  They sued.
[1030.38 --> 1035.14]  And then the district court and the appellate court, the second court of appeals, said, yes,
[1035.24 --> 1036.58]  all those things are copyrighted.
[1036.62 --> 1038.82]  But Google's use of that is actually fair use.
[1038.96 --> 1042.30]  And the particular type of fair use is called transformative use.
[1042.74 --> 1047.38]  That the use that Google was using was transformative to what the original purpose of the book was.
[1047.62 --> 1049.74]  Purpose of a book is to read it, enjoy it, etc.
[1050.38 --> 1055.08]  Google's purpose was to index it, to be able to create a word index, to be able to then search
[1055.08 --> 1060.26]  all of the books and to be able to provide the end user with a snippet, say maybe a page or two
[1060.26 --> 1060.98]  of that.
[1061.26 --> 1065.56]  So because it was not, you couldn't, I as a user couldn't use Google Books to be able to
[1065.56 --> 1067.48]  essentially replicate the book process.
[1067.48 --> 1069.32]  But instead, I'm using it to search.
[1069.32 --> 1072.02]  That is a transformative use, therefore fair use.
[1072.10 --> 1074.00]  That is not infringement of copyright.
[1074.22 --> 1075.12]  So that was back in the day.
[1075.64 --> 1077.74]  Now think about how large language models work.
[1077.96 --> 1082.04]  So a large language model, if you have the input, it is ingesting, say, the entirety of
[1082.04 --> 1082.50]  Harry Potter.
[1082.68 --> 1085.16]  But really what it's doing is placing those in vector space, right?
[1085.18 --> 1088.80]  It's saying that these words are similar to those words in vector space.
[1088.80 --> 1093.04]  And once that happens, largely it jettisons the thing, right?
[1093.40 --> 1097.22]  In copyright law, there is the idea expression dichotomy.
[1097.66 --> 1099.02]  Ideas are uncopyrightable.
[1099.30 --> 1104.32]  So if I have the idea of a man in a black hat fighting a man with a white hat over a woman
[1104.32 --> 1107.54]  who is tied to a railroad track, those are ideas that are uncopyrightable.
[1107.68 --> 1109.08]  You've seen lots of movies like that.
[1109.46 --> 1114.36]  But the expression of the idea, any particular movie that has that in there, that is copyrightable.
[1114.60 --> 1118.08]  So ideas uncopyrightable, expressions of the ideas are copyrightable.
[1118.08 --> 1123.50]  So if you apply that to what's happening when the large language model ingests all the books,
[1124.04 --> 1126.74]  it's essentially putting all the words into vector space.
[1127.26 --> 1131.64]  So it's saying, you know, this is a Bob Dylan-ism, or this is an Ernest Hemingway-ism,
[1131.86 --> 1133.24]  or this is a Harry Potter-ism.
[1133.66 --> 1136.96]  Each of those are ideas, not expressions of ideas.
[1137.52 --> 1143.50]  And so really, it's taking the expressions and effectively jettisoning those in favor of the ideas.
[1143.80 --> 1145.10]  So that's on the input side.
[1145.10 --> 1150.40]  And then on the output side, one can imagine that it's taking those ideas, Bob Dylan-ism,
[1150.66 --> 1154.70]  Ernest Hemingway-ism, and then it's outputting them in a new expression.
[1155.28 --> 1159.84]  And if you believe the copyright office, machine-generated output is similarly uncopyrightable.
[1160.22 --> 1164.48]  So we're kind of faced with an idea that inputs ideas uncopyrightable,
[1165.00 --> 1169.68]  outputs the expressions of ideas created by machines similarly uncopyrightable.
[1169.68 --> 1172.84]  To your particular point, this has not been tested in court.
[1173.00 --> 1176.96]  So, you know, a judge who, by the way, may not know what he's talking about or she is talking about,
[1177.32 --> 1179.78]  might rule against what I'm about to say right now.
[1179.84 --> 1185.76]  But at least I would make the really good argument that the ingestion of the thing is extracting the ideas from the book.
[1186.16 --> 1187.98]  And that is a transformative use.
[1188.06 --> 1193.86]  Because if you think about Google Books, they were printed three pages or so verbatim of these books.
[1194.36 --> 1198.04]  That's way more bulk than just, you know, think about the vector space.
[1198.20 --> 1200.80]  It's not reproducing any expression, right?
[1200.88 --> 1202.24]  It's merely taking the ideas.
[1202.38 --> 1206.78]  So if Google Books is permissible, almost certainly the large language model should also be.
[1207.08 --> 1213.16]  And that's really what is being argued right now in the cases that are happening with the GitHub copilot case happening in the West Coast.
[1213.30 --> 1217.66]  And then the stable diffusion case in Delaware, and there's others like it,
[1217.88 --> 1221.48]  where if I were the lawyers in that, I would be arguing exactly what I just argued right now.
[1221.48 --> 1226.68]  So to your specific use case, you are kind of interrogating this copyrighted work.
[1227.08 --> 1231.56]  But I would make the argument, if I were representing you, that this would be a transformative use.
[1231.90 --> 1238.50]  And just like you as a human would have read the book, and you can, as a human, could provide output based on that book.
[1238.82 --> 1244.68]  In the same way, a machine should be able to read that book and provide output that is just taking the ideas of the thing,
[1244.88 --> 1246.48]  not necessarily the expressions of the ideas.
[1246.48 --> 1253.48]  So with that new expression coming out that you're describing, and it being assuming that copyright office view stands,
[1253.68 --> 1261.92]  it's not copyrightable, that's a massively different way of producing content from before till now and in the future.
[1262.30 --> 1270.30]  What does that mean for business and the world at large, considering, I mean, that's a major, major change in how everything works.
[1270.56 --> 1273.90]  How do you see the future rolling out if that were to stand?
[1273.90 --> 1279.70]  First, I think it should stand, because otherwise, my All the Music project would essentially carpet bomb all the music,
[1279.90 --> 1285.40]  and we would just have machines creating new expressions that would essentially make human expression obsolete.
[1285.64 --> 1290.92]  So number one, I think it should stand, because if not, we are in a world of hurt with a copyright.
[1291.38 --> 1298.82]  Thing number two is, you're right, that never before in human history have we had a machine that creates new things.
[1298.82 --> 1303.50]  We've had the printing press, where we take my ideas, and then I can replicate it a whole bunch of times.
[1303.82 --> 1309.14]  We have the digital revolution in this, you know, 70s, 80s, 90s, 2000s, where now we can replicate human stuff.
[1309.26 --> 1314.74]  But never before have we had a way that the machine itself is making new expressions of ideas.
[1315.26 --> 1318.90]  And so as a result of that, some of the smartest people I know that are thinking about this,
[1319.20 --> 1325.34]  has said that the web, as it stands, is probably, large language models are going to stop right around November of 2022,
[1325.34 --> 1329.22]  because anything after that, you're going to have a whole bunch of machine-generated content
[1329.22 --> 1332.96]  that is going to be essentially large language model created things.
[1333.32 --> 1338.76]  If you know about the tech, and I assume your audience does, because it's statistically likely, it is smooth.
[1339.12 --> 1343.90]  Humans are jagged in the way that they write text, and that's what DetectGPT and others,
[1343.96 --> 1345.58]  is see the jaggedness of humanness.
[1346.00 --> 1349.78]  Machine-generated content is smooth, not jagged, so that's what DetectGPT says.
[1349.78 --> 1353.08]  Could you define that real quick, what jagged versus smooth means in this context?
[1353.08 --> 1357.96]  Sure. Yeah, so jagged means random. Smooth means statistically almost deterministic.
[1358.22 --> 1363.90]  So the idea is that we as humans say random things, and we put things in a way that maybe hasn't been said before,
[1364.26 --> 1367.52]  whereas machine, at least an LLM machine, is going to be able to say, you know,
[1367.56 --> 1369.64]  what's the most statistically likely word?
[1369.98 --> 1373.04]  And therefore, that is smoother than our jagged randomness.
[1373.52 --> 1379.84]  The idea is that as the machines are creating this smooth, deterministic, statistically likely next word,
[1379.84 --> 1386.56]  that is essentially, as new large language model ingests that smooth text, it's going to further smooth the corpus,
[1386.98 --> 1390.44]  and we're going to miss all of the human-created jaggedness that is going in there.
[1390.66 --> 1396.22]  So some of the smartest people I know are saying that maybe the web, as it stood in November of 22,
[1396.60 --> 1401.14]  is maybe that's the last time we're going to have a lot of human-created stuff that is truly jagged,
[1401.52 --> 1404.12]  because here and out, we're just going to have machine-created stuff that is smooth.
[1404.12 --> 1410.62]  And one last thing I would add is that one of the last bastions of human-created jaggedness that we have is the courts,
[1410.98 --> 1416.30]  because it turns out that, you know, people have talked about us being in a post-truth era and post-fact era.
[1416.58 --> 1420.14]  There is a person that's literally called a fact-finder, and his name is a judge.
[1420.48 --> 1424.82]  They spend years trying to find facts, and then they write things called judicial opinions
[1424.82 --> 1428.46]  that have found facts that have been battled over years in the courts.
[1428.46 --> 1434.46]  So one of the last places where we can find this jagged, almost certain-to-be-human-ridden thing
[1434.46 --> 1438.66]  that is actually based in fact in our post-fact world maybe is judicial opinions.
[1439.06 --> 1442.64]  And my employer, Vlex, has about a billion of those across the world.
[1443.00 --> 1447.46]  So maybe as we think about what are new corpuses that the large language models can train on
[1447.46 --> 1452.22]  that are truly jagged, that are full of factual things and not bulls**t that's on the internet,
[1452.22 --> 1453.40]  that is unvalidated, right?
[1453.44 --> 1456.82]  This is truly validated, human-created content that is high quality,
[1456.82 --> 1458.94]  that might be a source to be able to ingest.
[1459.62 --> 1462.74]  Maybe this gets a little bit back to your article example,
[1462.74 --> 1467.68]  where you interacted with the GPT output to write an article,
[1467.68 --> 1471.04]  and at a certain point, it kind of morphs into its own thing.
[1471.14 --> 1474.44]  What portion of it is machine-generated, what portion isn't?
[1474.84 --> 1479.86]  I know this is also happening just from seeing things like people are generating,
[1479.86 --> 1483.92]  for example, adult coloring books using AI models,
[1483.92 --> 1487.92]  and posting those in an almost automated way to Amazon.
[1488.40 --> 1491.22]  And then someone can literally order a book.
[1491.40 --> 1493.60]  I think of other examples maybe where,
[1494.14 --> 1496.64]  hey, this book was written a long time ago,
[1496.72 --> 1498.16]  and so the wording is really difficult.
[1498.32 --> 1502.68]  What if I used a large language model to rephrase it in modern English,
[1502.68 --> 1505.90]  and then I just post that and start selling it?
[1505.90 --> 1510.32]  So how long will this be debated in terms of the copyright around this,
[1510.32 --> 1516.34]  and what should be on people's minds as they're creating this kind of content
[1516.34 --> 1518.34]  that they actually want to commercialize?
[1518.70 --> 1520.54]  Maybe that's a more practical question.
[1521.12 --> 1521.22]  Sure.
[1521.34 --> 1524.76]  If I were to create this machine-created coloring book, for example,
[1525.20 --> 1527.80]  which under the U.S. Copyright Office today,
[1527.90 --> 1530.68]  that entirely machine-created thing is therefore uncopyrightable,
[1531.14 --> 1533.90]  this really goes to the heart of what is copyright in the first place,
[1533.90 --> 1536.34]  and all copyright is is a monopoly.
[1536.90 --> 1539.84]  It is a government-sanctioned monopoly giving you, the author,
[1540.18 --> 1543.84]  a monopoly of life of the author plus 70 years on the thing you created.
[1544.14 --> 1546.20]  But as an exchange for that monopoly,
[1546.68 --> 1548.80]  the government says this has to be original.
[1549.16 --> 1551.86]  That is, it has to be your creative work that does this.
[1551.92 --> 1554.78]  And if it is truly original and it is truly creative,
[1555.02 --> 1556.90]  we will give you that monopoly of 70 years,
[1557.02 --> 1558.30]  a life of the author plus 70 years.
[1558.70 --> 1560.40]  So really the question is,
[1560.40 --> 1563.52]  is there anything copyrightable in the machine-generated work?
[1563.52 --> 1566.98]  Well, probably not because there was no human creativity in that thing.
[1567.18 --> 1568.26]  So that's thing number one.
[1568.70 --> 1570.28]  But then let's look at another scenario.
[1570.46 --> 1573.92]  What if somebody else did a human-created coloring book
[1573.92 --> 1576.82]  that was identical to what the machine had done?
[1577.16 --> 1580.56]  Does that turn it from unoriginal, therefore uncopyrightable,
[1580.62 --> 1581.70]  with the machine-created one,
[1582.12 --> 1583.34]  to all of a sudden if a human does it,
[1583.72 --> 1585.74]  it is copyrightable, even though they're identical?
[1586.18 --> 1589.30]  Yeah, essentially because the machine wasn't copyrightable
[1589.30 --> 1590.58]  and you're recreating it,
[1590.58 --> 1592.86]  even though there might be no creativity on the human's part
[1592.86 --> 1595.08]  because they're literally looking at the output
[1595.08 --> 1597.40]  of the uncopyrightable machine output,
[1597.68 --> 1600.66]  but they can steal the idea without the creativity involved
[1600.66 --> 1601.74]  and then copyright.
[1601.86 --> 1602.70]  Am I understanding you correctly?
[1602.98 --> 1603.32]  That's right.
[1603.38 --> 1604.18]  And we've dealt with this,
[1604.24 --> 1606.10]  the courts have dealt with this for a few hundred years,
[1606.10 --> 1609.22]  and you can imagine Shakespeare is in the public domain.
[1609.36 --> 1611.16]  It's not been in copyright for hundreds of years.
[1611.52 --> 1613.02]  You can build a top Shakespeare,
[1613.40 --> 1614.58]  say with West Side Story,
[1614.82 --> 1616.46]  that was based on Romeo and Juliet, right?
[1616.46 --> 1619.08]  The writers of West Side Story don't get copyright
[1619.08 --> 1621.40]  in the underlying story of Romeo and Juliet,
[1621.84 --> 1625.30]  but they do get copyright in whatever they put atop Romeo and Juliet.
[1625.52 --> 1627.98]  So the fact that it's New York City and all of these things.
[1628.02 --> 1629.96]  So they just get what's called thin copyright
[1629.96 --> 1631.70]  on top of the public domain thing.
[1632.18 --> 1635.58]  So you can imagine going back to our coloring book example, right?
[1635.58 --> 1637.44]  If someone then copies that
[1637.44 --> 1639.50]  and then adds a little human touch on that,
[1639.88 --> 1641.98]  they don't get the underlying copyright thing
[1641.98 --> 1642.92]  because that's public domain.
[1642.92 --> 1646.52]  They only get what they've added atop the machine created thing.
[1646.96 --> 1648.52]  And really, the question is,
[1648.60 --> 1650.22]  how much can you really add atop
[1650.22 --> 1653.22]  that is really creative enough to make it worthwhile?
[1653.74 --> 1654.66]  And I would say, you know,
[1654.72 --> 1657.58]  if it's just another line here or there,
[1657.68 --> 1659.82]  that's not sufficiently original or creative
[1659.82 --> 1661.02]  to add copyright ability.
[1661.38 --> 1664.12]  I do want to get back to another couple of themes,
[1664.30 --> 1666.40]  but maybe one more selfish question,
[1666.50 --> 1667.80]  which is less related to,
[1668.12 --> 1669.92]  I guess the inputs and outputs
[1669.92 --> 1673.64]  would be more related to the models themselves,
[1673.64 --> 1677.10]  what they're trained on and how they're released.
[1677.26 --> 1680.50]  Of course, we're seeing a lot of different approaches
[1680.50 --> 1682.40]  to how models are being released
[1682.40 --> 1683.44]  in the sense that,
[1683.90 --> 1685.12]  well, is a model code?
[1685.18 --> 1686.12]  Is it data?
[1686.60 --> 1687.98]  Do I use Creative Commons?
[1688.24 --> 1690.06]  Or do I use Apache 2?
[1690.68 --> 1694.02]  Also, the data that was used in the training,
[1694.28 --> 1697.02]  maybe that's a mix of copyrightable material,
[1697.02 --> 1698.32]  or maybe it's not even known.
[1698.32 --> 1701.84]  Maybe it's a model shows up on Hugging Face,
[1701.98 --> 1705.56]  and I don't know what the mix of the data set was
[1705.56 --> 1707.78]  that was used in training.
[1707.96 --> 1711.14]  As you've been working with these large language models
[1711.14 --> 1713.02]  and advising around this
[1713.02 --> 1715.02]  and thinking about these concepts,
[1715.24 --> 1717.36]  how do you see that side of,
[1717.48 --> 1719.14]  I guess, training data,
[1719.48 --> 1721.60]  fine-tuning data, model release?
[1721.86 --> 1723.78]  What's on your mind as you look forward
[1723.78 --> 1724.96]  to this next season,
[1725.10 --> 1726.84]  which I assume will continue.
[1726.84 --> 1728.16]  We just had an episode with,
[1728.38 --> 1729.10]  I think it was titled,
[1729.24 --> 1731.60]  The Cambrian Explosion of Models.
[1731.66 --> 1733.40]  There's so many being released.
[1734.36 --> 1735.38]  This will continue.
[1735.54 --> 1737.78]  How do you see that side of things developing
[1737.78 --> 1740.86]  over the next season that we're entering?
[1740.86 --> 1743.98]  I think that what you're asking really about
[1743.98 --> 1746.92]  is the provenance of everything that comes downstream.
[1747.20 --> 1748.90]  That is, what is the provenance of the input
[1748.90 --> 1751.46]  and what is the provenance of the essentially
[1751.46 --> 1753.64]  being able to manipulate that input
[1753.64 --> 1755.24]  to create a thing that's called a model?
[1755.66 --> 1756.98]  Yeah, of course, the output of the model
[1756.98 --> 1758.60]  could train new inputs
[1758.60 --> 1760.26]  to be able to go into new models, right?
[1760.44 --> 1762.56]  Yes, the cyclical sort of thing.
[1762.98 --> 1763.36]  That's right.
[1763.38 --> 1764.78]  It's like a snake eating its own tail.
[1764.90 --> 1766.76]  And so within the law, in criminal law,
[1766.76 --> 1769.36]  there's a thing called the fruit of the poisonous tree.
[1769.36 --> 1771.36]  The first act might be innocuous,
[1771.50 --> 1773.14]  but then it leads to a chain reaction,
[1773.34 --> 1775.08]  a bunch of dominoes that leads to the end.
[1775.18 --> 1776.76]  So this is the fruit of the poisonous tree
[1776.76 --> 1778.80]  is a legal concept that you can imagine
[1778.80 --> 1780.70]  is similar for the questions you asked.
[1780.86 --> 1782.76]  If there is input data
[1782.76 --> 1785.08]  that maybe has questionable licensing.
[1785.42 --> 1787.18]  So for example, LLAMA, right?
[1787.26 --> 1789.16]  So it was released for open source,
[1789.28 --> 1790.40]  but only for academic purposes.
[1790.96 --> 1792.72]  So you could imagine if someone were to be able
[1792.72 --> 1795.22]  to create a model for commercial purposes
[1795.22 --> 1797.66]  that is based on that ostensibly licensed
[1797.66 --> 1798.72]  for academic purposes,
[1798.72 --> 1801.66]  that is maybe a fruit of the poisonous tree question
[1801.66 --> 1802.34]  to be able to say,
[1802.48 --> 1803.80]  is that model now tainted
[1803.80 --> 1807.18]  because it was ingested in opposition to the license?
[1807.50 --> 1807.60]  Yeah.
[1808.18 --> 1812.12]  I've wanted to use some of these LLAMA-based models
[1812.12 --> 1815.20]  quite recently and just haven't
[1815.20 --> 1817.94]  because it makes me ask a lot of questions.
[1818.22 --> 1820.42]  So am I right with that hesitation
[1820.42 --> 1822.66]  or is it yet to be determined,
[1822.94 --> 1824.72]  but you would make certain assumptions
[1824.72 --> 1825.90]  or what do you think?
[1825.90 --> 1826.38]  Yeah.
[1826.64 --> 1828.26]  So I should clarify that I'm a lawyer,
[1828.34 --> 1829.26]  but I'm not your lawyer.
[1829.38 --> 1831.26]  So nothing I'm saying is going to be legal advice.
[1831.38 --> 1831.50]  Okay.
[1831.66 --> 1832.42]  Yes, correct.
[1832.62 --> 1832.98]  Correct.
[1833.24 --> 1834.86]  So I would say that yes,
[1834.98 --> 1838.68]  anytime that you are ingesting items that are licensed
[1838.68 --> 1841.36]  and then you're using them in a way
[1841.36 --> 1842.84]  that is maybe against that license
[1842.84 --> 1844.46]  or not permitted by that license,
[1844.46 --> 1845.74]  I think anyone should be worried
[1845.74 --> 1847.24]  when that happens, speaking generally.
[1847.72 --> 1849.64]  I would also say that yes,
[1849.86 --> 1851.70]  anyone who does that should be worried.
[1852.10 --> 1856.12]  Also proving such things is tricky, right?
[1856.16 --> 1857.82]  Because there is the law
[1857.82 --> 1859.48]  and then there's what can be proved
[1859.48 --> 1861.50]  in a preponderance of the evidence in the court of law.
[1861.90 --> 1863.54]  As the dominoes fall
[1863.54 --> 1865.72]  and as the snake keeps eating its tail,
[1866.14 --> 1868.94]  the provenance of what data did you actually use
[1868.94 --> 1870.40]  and where did it come from?
[1870.56 --> 1871.20]  It gets murky.
[1871.52 --> 1872.48]  It does get really murky.
[1872.66 --> 1873.94]  And so that's something I imagine
[1873.94 --> 1875.22]  litigation is going to happen a lot.
[1875.22 --> 1877.48]  So I'm absolutely fascinated by that
[1877.48 --> 1879.46]  and want to take it farther.
[1879.70 --> 1883.02]  So I'm thinking back on years of business
[1883.02 --> 1884.68]  and all the IP concerns.
[1885.30 --> 1886.66]  I work for a big corporation.
[1886.88 --> 1888.30]  Lots of other people work for various...
[1889.36 --> 1891.02]  If the snake continues to eat its tail
[1891.02 --> 1893.42]  and you're seeing this happen over and over again,
[1894.00 --> 1897.16]  the value of current IP generally,
[1897.42 --> 1899.34]  I would argue, diminishes over time
[1899.34 --> 1901.24]  because its usefulness in business
[1901.24 --> 1903.62]  as things are progressing ever faster
[1903.62 --> 1905.44]  in the business plus technology world.
[1905.96 --> 1908.32]  You know, something that was a great piece of IP
[1908.32 --> 1909.10]  a few years ago,
[1909.16 --> 1910.40]  it might still be covered legally,
[1910.58 --> 1912.08]  but you're not necessarily going to use
[1912.08 --> 1913.62]  what was, you know, 20 years ago
[1913.62 --> 1915.38]  versus what you did yesterday.
[1915.68 --> 1917.28]  With that kind of utility
[1917.28 --> 1919.24]  of current IP diminishing
[1919.24 --> 1922.56]  and with this sequence of snake eating its tail
[1922.56 --> 1923.34]  that you're describing
[1923.34 --> 1925.24]  and, you know, fruit of the poison tree,
[1925.30 --> 1926.14]  I believe you called it,
[1926.44 --> 1929.92]  that has to have massive, massive repercussions
[1929.92 --> 1934.00]  for how business uses IP in the large,
[1934.30 --> 1934.90]  in general,
[1934.98 --> 1937.18]  like your entire strategy about...
[1937.18 --> 1937.80]  Because right now,
[1938.12 --> 1939.40]  you know, organizations,
[1939.72 --> 1940.96]  they will come up with an idea,
[1941.06 --> 1942.02]  they'll immediately go copyright,
[1942.12 --> 1944.08]  but whatever the appropriate mechanism is
[1944.08 --> 1945.06]  and get that in,
[1945.12 --> 1945.78]  they lock it in,
[1945.82 --> 1946.94]  it's part of their business strategy.
[1947.40 --> 1948.76]  That seems to me,
[1948.82 --> 1949.48]  from what you're saying,
[1949.52 --> 1951.06]  to fail in the future.
[1951.26 --> 1953.60]  It is no longer a good strategy.
[1953.84 --> 1955.72]  What does that mean in the large?
[1955.88 --> 1958.06]  I mean, that's a gigantic question, I think.
[1958.06 --> 1959.56]  What I think you've described
[1959.56 --> 1961.46]  and what I think we're saying in a society
[1961.46 --> 1963.54]  is the intellectual property laws
[1963.54 --> 1964.90]  that we've created, you know,
[1964.94 --> 1966.52]  since the beginning of our founding history.
[1966.90 --> 1968.56]  You know, the Constitution says
[1968.56 --> 1970.04]  that we will protect inventions.
[1970.30 --> 1971.36]  That's constitutional.
[1971.60 --> 1973.16]  So what I think we're seeing
[1973.16 --> 1975.62]  is our intellectual property regime
[1975.62 --> 1977.66]  that has existed since the 1700s
[1977.66 --> 1979.02]  creaking under its own weight
[1979.02 --> 1981.32]  with this new large language model
[1981.32 --> 1982.84]  generating in a way
[1982.84 --> 1984.24]  that's never been done in human history.
[1984.40 --> 1985.18]  I think you're right.
[1985.24 --> 1986.20]  The value of patents,
[1986.60 --> 1987.70]  what is the value of a patent?
[1987.70 --> 1989.18]  And if I can use a large language model
[1989.18 --> 1990.68]  to much like I described
[1990.68 --> 1991.62]  with all the patents,
[1992.02 --> 1993.04]  you know, we with all the patents
[1993.04 --> 1994.08]  are saying every patent
[1994.08 --> 1994.88]  that's ever been done
[1994.88 --> 1995.72]  and every idea,
[1995.86 --> 1996.96]  every claim and every patent,
[1997.06 --> 1997.98]  let's recombine those.
[1998.36 --> 1999.00]  But you can imagine,
[1999.18 --> 2000.64]  and I've heard that there are companies
[2000.64 --> 2001.60]  out there that are doing
[2001.60 --> 2003.14]  not what's been done before,
[2003.28 --> 2004.32]  but new ideas.
[2004.50 --> 2007.20]  And then making a ton of new claims
[2007.20 --> 2008.52]  and filing those new claims
[2008.52 --> 2009.58]  with the U.S. Patent Office.
[2009.80 --> 2011.36]  And to be able to say,
[2011.52 --> 2012.64]  here's a new idea.
[2012.64 --> 2014.28]  And if you carpet bomb
[2014.28 --> 2015.30]  the U.S. Patent Office
[2015.30 --> 2016.78]  with all of these new things
[2016.78 --> 2018.32]  that are just machine generated,
[2018.76 --> 2019.76]  there's currently a case,
[2020.10 --> 2021.24]  the Thaler case,
[2021.32 --> 2022.34]  T-H-L-E-R,
[2022.76 --> 2024.22]  that he created,
[2024.46 --> 2025.96]  has said a machine created this patent.
[2026.44 --> 2027.40]  And the patent office said,
[2027.48 --> 2029.00]  ah, machine created patents
[2029.00 --> 2029.58]  are not a thing.
[2029.62 --> 2030.22]  You can't do it.
[2030.56 --> 2031.38]  But they only knew that
[2031.38 --> 2032.62]  because Thaler told him
[2032.62 --> 2033.96]  that it was machine created.
[2034.42 --> 2035.26]  How many of these things
[2035.26 --> 2035.94]  are being filed
[2035.94 --> 2037.28]  that nobody has told anybody
[2037.28 --> 2038.40]  that it's been patented?
[2038.72 --> 2039.76]  And then is that fraud
[2039.76 --> 2040.62]  on the patent office?
[2041.40 --> 2041.76]  Probably.
[2042.08 --> 2042.96]  But the question is,
[2042.98 --> 2043.82]  who's going to find out
[2043.82 --> 2045.10]  if it doesn't go to litigation?
[2045.64 --> 2045.94]  For a moment,
[2046.00 --> 2046.68]  I want to ask you
[2046.68 --> 2048.00]  to stop being an attorney
[2048.00 --> 2049.80]  and be a speculator here.
[2049.96 --> 2050.86]  I want you to kind of
[2050.86 --> 2051.68]  blue sky it.
[2051.76 --> 2054.36]  Like, where can this possibly go?
[2054.40 --> 2055.64]  Or what are the different paths?
[2056.20 --> 2057.60]  You know, what's your gut tell you
[2057.60 --> 2059.40]  in terms of how this plays out?
[2059.40 --> 2060.96]  Because you've described
[2060.96 --> 2062.00]  multiple ways
[2062.00 --> 2062.94]  in the last few minutes
[2062.94 --> 2063.76]  where the whole system
[2063.76 --> 2065.30]  can essentially collapse
[2065.30 --> 2066.08]  under its own weight.
[2066.42 --> 2067.20]  Not just one way.
[2067.20 --> 2068.74]  You've done it several different ways
[2068.74 --> 2069.94]  where that can happen.
[2070.06 --> 2071.34]  Which isn't surprising
[2071.34 --> 2073.04]  because over the episodes
[2073.04 --> 2073.62]  of the show,
[2073.76 --> 2075.08]  we keep talking about
[2075.08 --> 2076.14]  the rapid change
[2076.14 --> 2077.74]  that all this is bringing in AI.
[2077.88 --> 2079.10]  It's the most fascinating moment
[2079.10 --> 2080.24]  in human history, in my view.
[2080.64 --> 2081.54]  And you're describing
[2081.54 --> 2083.26]  the weight of all
[2083.26 --> 2084.78]  the structure of the past
[2084.78 --> 2087.02]  in terms of the legal considerations,
[2087.52 --> 2088.46]  unable to keep up
[2088.46 --> 2089.40]  with what's going on now.
[2089.44 --> 2090.52]  And it's only accelerating.
[2090.74 --> 2091.82]  Where do we go from here?
[2091.90 --> 2092.68]  What does that mean?
[2093.28 --> 2093.38]  Sure.
[2093.52 --> 2094.94]  If past is prologue
[2094.94 --> 2096.02]  to what's going to happen,
[2096.14 --> 2096.78]  I would say that,
[2096.78 --> 2097.28]  you know,
[2097.34 --> 2098.70]  we've seen over the last decade
[2098.70 --> 2100.02]  business patents
[2100.02 --> 2101.06]  essentially going away.
[2101.20 --> 2102.34]  We've seen software patents
[2102.34 --> 2103.86]  almost pretty much go away
[2103.86 --> 2104.78]  with the Alice decision
[2104.78 --> 2105.26]  and others.
[2105.76 --> 2106.78]  So patents have already
[2106.78 --> 2108.32]  been diminishing in value,
[2108.42 --> 2108.98]  you know,
[2109.00 --> 2110.50]  over the last 10 years or so.
[2110.84 --> 2111.80]  And I think this is just
[2111.80 --> 2112.74]  going to accelerate
[2112.74 --> 2113.48]  that diminishment.
[2113.82 --> 2114.66]  Because, you know,
[2114.68 --> 2115.80]  if I'm going to compete
[2115.80 --> 2116.44]  in the marketplace,
[2117.06 --> 2118.08]  largely the, you know,
[2118.32 --> 2119.52]  anything I invent today
[2119.52 --> 2120.48]  is going to be obsolete
[2120.48 --> 2121.44]  in three years anyway.
[2121.88 --> 2122.66]  So what's the good
[2122.66 --> 2123.80]  in patenting a thing
[2123.80 --> 2124.48]  that is obsolete,
[2124.72 --> 2125.26]  you know,
[2125.26 --> 2125.88]  in three years?
[2126.00 --> 2127.30]  I think Elon Musk said,
[2127.42 --> 2127.80]  you know,
[2127.80 --> 2128.48]  I'm open sourcing
[2128.48 --> 2129.06]  all my patents,
[2129.14 --> 2129.46]  he said,
[2129.76 --> 2130.50]  because a patent
[2130.50 --> 2131.90]  is merely a license to sue.
[2132.30 --> 2133.34]  And that's true, right?
[2133.38 --> 2134.68]  It's I spend a million dollars
[2134.68 --> 2135.42]  or two million dollars
[2135.42 --> 2136.16]  to get the patent
[2136.16 --> 2136.96]  and then I have to spend
[2136.96 --> 2137.88]  millions on top of it
[2137.88 --> 2138.64]  to sue somebody
[2138.64 --> 2139.46]  over that patent.
[2139.62 --> 2140.56]  That license to sue
[2140.56 --> 2141.28]  often just doesn't
[2141.28 --> 2142.02]  make business sense.
[2142.12 --> 2142.66]  And I think it makes
[2142.66 --> 2143.42]  even less sense
[2143.42 --> 2144.30]  as the system
[2144.30 --> 2145.30]  is collapsing in its own way.
[2145.30 --> 2146.46]  So if you're looking
[2146.46 --> 2147.56]  for me to speculate
[2147.56 --> 2148.40]  and you are,
[2148.50 --> 2149.30]  I would hope
[2149.30 --> 2150.94]  that the patent regime
[2150.94 --> 2152.02]  is going to fall away
[2152.02 --> 2152.60]  in importance
[2152.60 --> 2153.22]  and people are just
[2153.22 --> 2153.72]  going to innovate.
[2154.44 --> 2155.68]  As all of us
[2155.68 --> 2156.80]  on this call
[2156.80 --> 2158.72]  are knowledge workers
[2158.72 --> 2160.40]  and program
[2160.40 --> 2162.16]  or do legal work,
[2162.24 --> 2163.10]  that sort of thing,
[2163.64 --> 2164.56]  I think we're all
[2164.56 --> 2165.10]  benefiting
[2165.10 --> 2167.16]  in terms of productivity
[2167.16 --> 2169.12]  moving into the future.
[2169.34 --> 2169.94]  You know,
[2170.00 --> 2171.48]  outside of the IP stuff,
[2171.58 --> 2172.62]  the copyright things,
[2172.70 --> 2173.66]  all of those things,
[2174.00 --> 2175.28]  I'm coding much faster
[2175.28 --> 2175.64]  now,
[2175.72 --> 2176.80]  not because I'm
[2176.80 --> 2178.38]  necessarily a better coder,
[2178.46 --> 2179.64]  which maybe I'd like
[2179.64 --> 2180.32]  to think I am,
[2180.38 --> 2181.36]  but I'm probably not.
[2181.50 --> 2183.04]  It's because I'm using
[2183.04 --> 2184.56]  generative tools
[2184.56 --> 2185.38]  and suggestions
[2185.38 --> 2187.36]  in a much more robust way.
[2188.02 --> 2189.74]  And I was fascinated
[2189.74 --> 2191.60]  in one of your recent talks
[2191.60 --> 2192.86]  when you're talking about
[2192.86 --> 2193.60]  kind of the practical
[2193.60 --> 2194.74]  consequences of that.
[2194.82 --> 2195.64]  Like if I can work
[2195.64 --> 2197.08]  50% faster,
[2197.88 --> 2199.34]  do I still work
[2199.34 --> 2200.34]  the same amount
[2200.34 --> 2203.06]  or do I work less?
[2203.22 --> 2204.54]  And what are the implications
[2204.54 --> 2206.48]  of my employer's viewpoint
[2206.48 --> 2207.58]  on my work
[2207.58 --> 2208.34]  and that sort of thing?
[2208.64 --> 2209.30]  Could you talk us
[2209.30 --> 2209.96]  through a little bit
[2209.96 --> 2210.82]  about your thinking
[2210.82 --> 2211.70]  in that regard?
[2212.10 --> 2212.32]  Yeah.
[2212.46 --> 2213.32]  So I'm going to talk
[2213.32 --> 2214.52]  about four worlds.
[2214.66 --> 2216.60]  First world is 2022 world
[2216.60 --> 2218.18]  before the large language bottles.
[2218.76 --> 2219.58]  And in that world,
[2219.58 --> 2220.86]  I would work 40 hours a week
[2220.86 --> 2221.46]  full time
[2221.46 --> 2222.54]  and I would give
[2222.54 --> 2223.66]  40 hours a week
[2223.66 --> 2225.78]  of 2022 productivity
[2225.78 --> 2226.86]  as a result of that.
[2227.04 --> 2228.00]  And as a result of that,
[2228.24 --> 2229.20]  an employer would hire
[2229.20 --> 2230.14]  a workforce like me
[2230.14 --> 2230.56]  to do that.
[2230.56 --> 2231.72]  So that's world number one.
[2232.14 --> 2233.20]  In world number two,
[2233.42 --> 2235.20]  I know of people anecdotally
[2235.20 --> 2236.24]  that have,
[2236.36 --> 2237.18]  are working three
[2237.18 --> 2238.10]  full time jobs
[2238.10 --> 2239.32]  because they're getting
[2239.32 --> 2240.32]  at least, you know,
[2240.36 --> 2242.76]  100% or so productivity gains,
[2242.86 --> 2244.62]  maybe 10x productivity gains
[2244.62 --> 2245.40]  based on the code
[2245.40 --> 2245.82]  that you said.
[2245.90 --> 2246.78]  So they have three
[2246.78 --> 2247.52]  full time jobs.
[2247.58 --> 2248.56]  So he's essentially working
[2248.56 --> 2249.64]  30% of the time
[2249.64 --> 2250.40]  for each,
[2250.54 --> 2251.34]  but still providing
[2251.34 --> 2252.60]  100% of the output
[2252.60 --> 2253.40]  for that.
[2253.52 --> 2254.28]  And their employer
[2254.28 --> 2254.76]  is saying,
[2254.86 --> 2255.66]  wow, that's great output.
[2255.80 --> 2256.76]  They don't care, right?
[2256.88 --> 2258.18]  So that's world number two.
[2258.18 --> 2259.84]  I think what we're in today.
[2260.52 --> 2261.34]  World number three
[2261.34 --> 2263.02]  is probably the employer
[2263.02 --> 2263.42]  is going to say,
[2263.54 --> 2264.14]  hey, hey, hey, hey,
[2264.28 --> 2265.38]  don't give me 30%
[2265.38 --> 2265.92]  of your time.
[2266.30 --> 2267.60]  Give me 100% of your time
[2267.60 --> 2269.12]  and maybe give me
[2269.12 --> 2270.04]  10x output
[2270.04 --> 2272.70]  of 2022 level output, right?
[2272.80 --> 2274.16]  I want that productivity
[2274.16 --> 2275.02]  gain from you.
[2275.18 --> 2276.52]  So that's world number three.
[2277.00 --> 2278.28]  But I think shortly thereafter
[2278.28 --> 2278.86]  is going to come
[2278.86 --> 2279.84]  world number four
[2279.84 --> 2281.82]  where the executives
[2281.82 --> 2282.28]  are going to say,
[2282.36 --> 2282.78]  whoa, wait, wait.
[2282.98 --> 2284.08]  If we lay off
[2284.08 --> 2285.24]  two thirds of the workforce
[2285.24 --> 2287.24]  and then still require them
[2287.24 --> 2288.52]  to work 40 hours a week
[2288.52 --> 2289.92]  with their 10x productivity,
[2290.60 --> 2291.78]  I can say to my shareholders,
[2292.00 --> 2292.92]  look at all the costs
[2292.92 --> 2293.68]  that we cut
[2293.68 --> 2294.68]  by laying off
[2294.68 --> 2295.58]  two thirds of the workforce
[2295.58 --> 2296.66]  and we're still getting
[2296.66 --> 2297.80]  5x productivity
[2297.80 --> 2298.76]  on top of our
[2298.76 --> 2299.86]  2022 productivity.
[2300.36 --> 2301.42]  We've cut costs.
[2301.72 --> 2302.74]  We've increased productivity.
[2303.28 --> 2304.02]  Aren't we great?
[2304.54 --> 2305.70]  I think that that's probably
[2305.70 --> 2306.98]  the world that we're headed for.
[2307.50 --> 2308.06]  And there's a world
[2308.06 --> 2308.98]  six beyond that,
[2309.14 --> 2310.20]  which that leads
[2310.20 --> 2311.02]  very obviously
[2311.02 --> 2312.40]  to that recognition
[2312.40 --> 2314.04]  of cut the workforce
[2314.04 --> 2314.50]  and stuff.
[2314.62 --> 2314.92]  I don't know
[2314.92 --> 2315.62]  if we want to go there
[2315.62 --> 2317.14]  or not to finish up,
[2317.20 --> 2318.10]  but we've got some
[2318.10 --> 2319.24]  tough social issues
[2319.24 --> 2320.10]  to navigate there.
[2320.38 --> 2320.78]  Really,
[2320.90 --> 2322.00]  what we're describing here
[2322.00 --> 2323.78]  is there's a scarcity mindset
[2323.78 --> 2325.52]  and there's an abundance mindset.
[2325.76 --> 2326.48]  The scarcity mindset
[2326.48 --> 2328.30]  is that around 1979,
[2328.76 --> 2329.86]  accountants were really worried
[2329.86 --> 2331.04]  with this artificial intelligence
[2331.04 --> 2331.98]  that's called the spreadsheet
[2331.98 --> 2333.42]  because they said,
[2333.54 --> 2334.52]  wow, all we do all day
[2334.52 --> 2335.24]  is use ledgers
[2335.24 --> 2336.66]  and we add and subtract numbers
[2336.66 --> 2337.74]  and machines can do that
[2337.74 --> 2338.16]  in seconds.
[2338.36 --> 2338.98]  That's going to put us
[2338.98 --> 2339.58]  all out of work.
[2340.08 --> 2340.66]  But what happened
[2340.66 --> 2341.86]  was that when the clients
[2341.86 --> 2342.28]  realized,
[2342.50 --> 2343.36]  oh, it's not going to take me
[2343.36 --> 2343.76]  a week
[2343.76 --> 2344.82]  to get that ledger back,
[2344.82 --> 2345.82]  but it's going to take seconds.
[2346.24 --> 2347.24]  Let's do the scenario two
[2347.24 --> 2348.04]  and scenario three
[2348.04 --> 2348.70]  and scenario four
[2348.70 --> 2349.84]  and run more scenarios
[2349.84 --> 2350.86]  and now we have
[2350.86 --> 2351.76]  more accountants than ever
[2351.76 --> 2352.84]  because the tools
[2352.84 --> 2354.00]  are actually a force multiplier
[2354.00 --> 2355.26]  that now there's more
[2355.26 --> 2355.86]  accounting work
[2355.86 --> 2356.68]  rather than less.
[2357.14 --> 2358.72]  So that is an abundance mindset
[2358.72 --> 2360.00]  that is not a scarcity mindset.
[2360.38 --> 2361.16]  So the real question
[2361.16 --> 2361.72]  in my mind
[2361.72 --> 2362.44]  and maybe should be
[2362.44 --> 2363.26]  on all of our minds
[2363.26 --> 2365.38]  is the scarcity mindset
[2365.38 --> 2366.44]  that I described
[2366.44 --> 2367.50]  with worlds one,
[2367.56 --> 2368.30]  two, three, and four,
[2368.66 --> 2369.60]  is that going to be our future
[2369.60 --> 2371.16]  or is there an abundance mindset
[2371.16 --> 2373.26]  where we just have 10x
[2373.26 --> 2374.22]  or 100x productivity
[2374.22 --> 2375.12]  and we keep growing
[2375.12 --> 2375.78]  and growing and growing.
[2376.14 --> 2377.76]  I think that's a great transition
[2377.76 --> 2379.06]  kind of as we get
[2379.06 --> 2380.20]  to the close here.
[2380.32 --> 2381.42]  Maybe one question
[2381.42 --> 2382.92]  that I'd like to ask you.
[2383.46 --> 2384.36]  We've talked about
[2384.36 --> 2385.90]  various interesting scenarios
[2385.90 --> 2386.82]  and maybe things
[2386.82 --> 2388.14]  that are honestly
[2388.14 --> 2390.42]  kind of uncomfortable
[2390.42 --> 2391.84]  for a lot of our
[2391.84 --> 2393.10]  kind of technical listeners
[2393.10 --> 2395.08]  around, oh, legal questions
[2395.08 --> 2396.04]  and lawsuits
[2396.04 --> 2396.98]  and copyright
[2396.98 --> 2398.32]  and that sort of thing.
[2398.64 --> 2399.94]  From your perspective
[2399.94 --> 2402.40]  as you look to the future
[2402.40 --> 2403.88]  kind of this next year,
[2404.00 --> 2405.46]  what are you encouraged by
[2405.46 --> 2406.86]  and or what,
[2407.24 --> 2408.28]  how would you encourage
[2408.28 --> 2409.28]  our listeners,
[2409.52 --> 2411.96]  maybe those practical developers
[2411.96 --> 2413.70]  or practitioners out there,
[2414.12 --> 2416.06]  like how would you encourage them
[2416.06 --> 2418.16]  to engage in this conversation
[2418.16 --> 2419.32]  and these topics
[2419.32 --> 2420.28]  moving to the future
[2420.28 --> 2421.88]  and what are you excited about
[2421.88 --> 2422.56]  or encouraged by
[2422.56 --> 2423.46]  moving to the future?
[2424.12 --> 2425.08]  I think about AI
[2425.08 --> 2426.66]  as largely a tidal wave
[2426.66 --> 2427.40]  or a tsunami
[2427.40 --> 2429.76]  and we are running faster
[2429.76 --> 2430.66]  than the tsunami.
[2431.06 --> 2431.98]  How do we run faster
[2431.98 --> 2432.60]  than tsunami?
[2432.80 --> 2434.10]  You learn how to use Copilot
[2434.10 --> 2435.80]  to be able to go faster.
[2436.22 --> 2437.10]  You learn how to be able
[2437.10 --> 2437.78]  to do things
[2437.78 --> 2438.32]  that the machine
[2438.32 --> 2439.54]  cannot yet do.
[2439.88 --> 2440.78]  That's running faster
[2440.78 --> 2441.38]  than tsunami.
[2441.98 --> 2442.60]  So really,
[2443.00 --> 2443.24]  there's,
[2443.46 --> 2444.28]  I say to lawyers
[2444.28 --> 2445.32]  that are worried about AI
[2445.32 --> 2446.76]  that AI will not
[2446.76 --> 2447.66]  take a lawyer's job
[2447.66 --> 2449.22]  but a lawyer that uses AI
[2449.22 --> 2450.02]  will take the job
[2450.02 --> 2450.40]  of a lawyer
[2450.40 --> 2451.72]  that does not use AI.
[2452.44 --> 2452.92]  And so really,
[2452.98 --> 2453.70]  I would say the same thing
[2453.70 --> 2454.70]  for coders who are listening
[2454.70 --> 2456.74]  that learning to use the tool
[2456.74 --> 2457.64]  to run faster
[2457.64 --> 2458.60]  than the tsunami,
[2459.04 --> 2459.78]  there's another joke,
[2459.88 --> 2460.04]  you know,
[2460.08 --> 2460.58]  there was a bear
[2460.58 --> 2461.20]  at a campground
[2461.20 --> 2462.02]  and two guys
[2462.02 --> 2462.62]  and the one guy
[2462.62 --> 2463.88]  gets out of tennis shoes
[2463.88 --> 2464.94]  and the other guy says,
[2465.02 --> 2465.88]  you can't outrun a bear
[2465.88 --> 2466.60]  and he said,
[2466.64 --> 2467.06]  I don't have to,
[2467.10 --> 2468.04]  I just have to outrun you,
[2468.20 --> 2468.38]  right?
[2468.76 --> 2469.52]  So in that sense,
[2469.68 --> 2470.36]  learn how to use
[2470.36 --> 2471.18]  the large language models
[2471.18 --> 2472.50]  to outrun your competition
[2472.50 --> 2473.76]  because as the wave
[2473.76 --> 2474.70]  crashes over them,
[2474.84 --> 2475.66]  it's not going to crash
[2475.66 --> 2476.08]  over you.
[2476.52 --> 2477.74]  I think that we all
[2477.74 --> 2478.38]  have to reckon,
[2478.64 --> 2479.84]  eventually the wave,
[2479.98 --> 2480.20]  I think,
[2480.30 --> 2481.72]  may crash over all of us
[2481.72 --> 2482.70]  but for,
[2482.96 --> 2483.60]  until then,
[2483.62 --> 2484.18]  I think we should be
[2484.18 --> 2484.68]  running as fast
[2484.68 --> 2485.16]  as we can.
[2485.78 --> 2486.06]  Awesome.
[2486.30 --> 2486.44]  Yeah,
[2486.44 --> 2487.38]  that's a great encouragement
[2487.38 --> 2488.66]  and thank you so much
[2488.66 --> 2489.90]  for humoring us
[2489.90 --> 2490.76]  with all of our
[2490.76 --> 2492.14]  random questions,
[2492.28 --> 2493.50]  some of which were
[2493.50 --> 2494.86]  selfish on my part
[2494.86 --> 2496.20]  but I've learned a lot
[2496.20 --> 2497.16]  and really appreciate
[2497.16 --> 2497.82]  your insights,
[2498.02 --> 2498.32]  Damien,
[2498.40 --> 2499.36]  and the work that you're doing.
[2499.70 --> 2501.10]  Look forward to seeing
[2501.10 --> 2502.42]  your future projects
[2502.42 --> 2504.22]  and I'm sure that
[2504.22 --> 2505.38]  our listeners will find
[2505.38 --> 2506.16]  this super interesting.
[2506.36 --> 2507.06]  Thank you so much.
[2507.40 --> 2507.74]  Thank you.
[2507.84 --> 2510.08]  I don't often get to speak
[2510.08 --> 2511.04]  to audiences
[2511.04 --> 2512.16]  as sophisticated as yours
[2512.16 --> 2513.10]  so I really enjoyed
[2513.10 --> 2513.70]  the really deep
[2513.70 --> 2514.42]  and probing questions
[2514.42 --> 2515.82]  and I really am grateful
[2515.82 --> 2516.58]  for the opportunity.
[2525.00 --> 2526.30]  Thank you for listening
[2526.30 --> 2527.50]  to Practical AI.
[2528.04 --> 2529.26]  Your next step
[2529.26 --> 2530.58]  is to subscribe now
[2530.58 --> 2531.82]  if you haven't already
[2531.82 --> 2533.30]  and if you're a long-time
[2533.30 --> 2534.06]  listener of the show,
[2534.42 --> 2535.74]  help us reach more people
[2535.74 --> 2537.16]  by sharing Practical AI
[2537.16 --> 2537.76]  with your friends
[2537.76 --> 2538.30]  and colleagues.
[2538.30 --> 2539.68]  Thanks once again
[2539.68 --> 2540.96]  to Fastly and Fly
[2540.96 --> 2542.04]  for partnering with us
[2542.04 --> 2542.72]  to bring you all
[2542.72 --> 2543.68]  Change Talk podcasts.
[2544.28 --> 2545.18]  Check out what they're up to
[2545.18 --> 2546.46]  at Fastly.com
[2546.46 --> 2548.06]  and Fly.io.
[2548.46 --> 2549.44]  And to our Beat Freakin'
[2549.52 --> 2549.88]  residents,
[2550.02 --> 2550.86]  Breakmaster Cylinder
[2550.86 --> 2552.48]  for continuously cranking out
[2552.48 --> 2553.78]  the best beats in the biz.
[2554.06 --> 2554.98]  That's all for now.
[2555.24 --> 2556.38]  We'll talk to you again next time.
[2556.38 --> 2559.38]  close by что ya poolero.
[2559.38 --> 2559.82]  start bomb
[2559.82 --> 2560.00]  open
[2560.00 --> 2560.94]  and reed
[2560.94 --> 2561.22]  on the заво.
[2561.22 --> 2561.80]  close by
[2561.80 --> 2562.48]  get yourself
[2562.48 --> 2562.70]  cautious
[2562.70 --> 2563.30]  of all
[2563.30 --> 2564.92]  content
[2564.92 --> 2584.58] ody hyperbolic. PRIisedеж
