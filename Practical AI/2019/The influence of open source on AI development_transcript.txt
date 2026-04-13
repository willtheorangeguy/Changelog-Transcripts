[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.02]  And unlike standard droplets, which use shared virtual CPU threads,
[29.02 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.40 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.20 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.30]  And now onto the show.
[106.66 --> 109.16]  Welcome to Practical AI.
[109.66 --> 111.28]  This is Daniel Whitenack.
[111.38 --> 114.10]  I'm a data scientist with SIL International,
[114.50 --> 117.00]  and I'm joined by my co-host, Chris Benson,
[117.60 --> 120.46]  a principal AI strategist at Lockheed Martin.
[121.04 --> 121.90]  How are you doing, Chris?
[121.96 --> 123.58]  I hear you just got off of a plane.
[123.58 --> 130.40]  Yeah, I just arrived in London via Heathrow and just got into the hotel room in time to record here.
[130.94 --> 132.52]  So looking forward to it.
[132.62 --> 139.54]  I'm in London because tomorrow I will be on a panel representing Lockheed Martin at the Royal Academy of Engineering
[139.54 --> 142.98]  for a panel discussion on artificial intelligence of all things.
[143.70 --> 144.08]  Oh, wow.
[144.12 --> 145.34]  That sounds intense.
[145.34 --> 149.96]  I don't know if I've ever been involved in any sort of royal anything.
[150.38 --> 150.48]  It's scary.
[150.70 --> 155.24]  The word, put royal in front of anything, and it's either big or scary or both.
[155.50 --> 156.32]  Right, exactly.
[156.50 --> 157.64]  I just, yeah.
[157.78 --> 162.74]  I don't know if there'll be anybody in like robes or wigs or anything in the audience.
[162.86 --> 164.22]  So that's kind of what I have pictured.
[164.42 --> 166.06]  I'm hoping they'll let me do that.
[166.20 --> 168.82]  You know, we can do, you know, kind of like the old movies.
[168.82 --> 169.02]  That'd be awesome.
[169.02 --> 172.28]  You know, we'll all be up on the panel talking about AI with our wigs on and stuff.
[172.34 --> 172.88]  That'd be perfect.
[172.88 --> 173.28]  Right.
[173.36 --> 173.84]  Yeah.
[174.18 --> 179.38]  Well, on a slightly different note, there's another event coming up relatively soon, which
[179.38 --> 183.92]  is a conference called All Things Open, which I've been to once.
[184.06 --> 184.96]  I spoke there.
[185.34 --> 186.48]  It was a great experience.
[186.88 --> 191.30]  A conference kind of focused on a lot of different things other than machine learning and AI,
[191.48 --> 193.66]  but kind of centered around the open source world.
[193.94 --> 200.96]  And one of the people talking there this year is Samuel Taylor, who is a data scientist at
[200.96 --> 201.36]  Indeed.
[201.36 --> 201.56]  Indeed.
[201.96 --> 205.46]  And he's talking about using open source tools for machine learning.
[205.90 --> 211.50]  And so we definitely thought that that was practical for those out of us trying to do
[211.50 --> 212.50]  practical AI.
[212.76 --> 216.32]  So we've got Samuel Taylor with us this week to talk about it.
[216.38 --> 216.92]  Welcome, Samuel.
[217.56 --> 218.34]  Thank you all so much.
[218.40 --> 219.72]  I'm really excited to be here.
[219.78 --> 224.78]  Really interested to be part of this project that you'll have to make AI more practical
[224.78 --> 227.78]  and more easy to use for people.
[227.78 --> 228.38]  Thanks.
[229.12 --> 232.48]  Yeah, it definitely seemed like your talk was in that vein.
[232.70 --> 235.14]  And we'll get to the subject of the talk.
[235.24 --> 239.58]  But maybe to start out, could you just give us a little bit of information about your background
[239.58 --> 243.08]  and how you got into data science and machine learning?
[243.08 --> 244.34]  Of course.
[244.58 --> 248.18]  So from some accounts, I've just always liked computers.
[248.50 --> 252.38]  There's a picture of me when I am, I think, seven or eight years old sitting at the family
[252.38 --> 252.80]  computer.
[252.80 --> 256.68]  And I have my hand on the mouse playing some point and click adventure game.
[256.68 --> 260.60]  And I guess I just never grew out of that and just always liked computers and had really
[260.60 --> 265.02]  great parents who encouraged me to pursue math and programming.
[265.54 --> 270.98]  And I was able to learn a lot of that and practice a lot of that leading up into high
[270.98 --> 271.20]  school.
[271.54 --> 275.06]  And at some point in high school, I saw a documentary on PBS.
[275.32 --> 276.58]  I think it was like a Nova documentary.
[276.58 --> 281.58]  And they were talking about machine learning, I guess, because they had an example where
[281.58 --> 284.90]  they showed a computer a bunch of images of English letters.
[284.90 --> 289.70]  And then it could tell with a new picture if it was an A or a B or a C or whatever.
[289.76 --> 290.86]  And that just blew my mind.
[291.30 --> 293.04]  You got to love those Nova documentaries.
[293.44 --> 293.74]  Oh, yeah.
[294.04 --> 294.90]  Yeah, totally.
[295.10 --> 295.32]  Totally.
[295.94 --> 298.34]  And it just, like I said, it just blew my mind.
[298.38 --> 302.04]  And then when I got into college and started studying computer science and realized, like,
[302.30 --> 303.56]  I can learn how to do that.
[303.62 --> 304.58]  That's that's really cool.
[304.58 --> 306.02]  I took some classes in that.
[306.16 --> 311.02]  And then after I graduated, started doing more like software engineering stuff and data
[311.02 --> 311.44]  engineering.
[311.84 --> 316.00]  And then at my current company, Indeed, we have this internal transfer program where I
[316.00 --> 320.32]  was able to transfer to a data scientist role at the company, which has been really
[320.32 --> 320.46]  good.
[320.50 --> 322.16]  So I guess that's how I ended up in data science.
[322.64 --> 322.96]  Congratulations.
[323.96 --> 324.24]  Yeah.
[324.50 --> 324.72]  Yeah.
[324.76 --> 325.04]  Thanks, y'all.
[325.06 --> 330.12]  Do you feel like I'm kind of I'm always intrigued by people's journeys and how it influences how
[330.12 --> 332.02]  they think about data science problems.
[332.02 --> 337.42]  Do you feel like your sort of initial emphasis on software engineering and building up that
[337.42 --> 339.48]  side of your your expertise?
[339.86 --> 343.68]  How do you think that's influenced, you know, your work in data science?
[344.12 --> 344.94]  That's a wonderful question.
[345.06 --> 349.68]  I think it is a it plays a huge part in the way that I think about these systems, because
[349.68 --> 356.20]  I recognize that I am never going to be as good at applied statistics as someone with
[356.20 --> 357.38]  an astrophysics Ph.D.
[357.38 --> 357.86]  Right.
[357.94 --> 360.04]  And I just know that that's not my strength.
[360.32 --> 365.38]  And so what I try to do is then understand these algorithms like I would any other algorithm
[365.38 --> 370.52]  and try to treat them like any kind of other engineering system and treat them with the
[370.52 --> 372.44]  same kind of rigor that I would in that way.
[372.54 --> 377.46]  The other way it's been helpful is that it kind of sets me up well to try to try to bridge
[377.46 --> 381.62]  the gap between some of these people who are brilliant statisticians and really understand
[381.62 --> 382.34]  data deeply.
[382.34 --> 385.94]  And then, you know, sometimes, especially if they're coming straight out of school, might
[385.94 --> 389.00]  not have as much experience in the software engineering side of things.
[389.10 --> 393.70]  And so it can create this really useful kind of knowledge share where I'm able to help
[393.70 --> 397.88]  some people with kind of skilling up at software engineering and they're able to help me get
[397.88 --> 400.72]  better at the stats side of things and introduce me to stuff I'm not familiar with.
[401.08 --> 404.38]  And so I think it ends up just being really good to have that diversity of backgrounds.
[404.62 --> 406.70]  You know, it's very it's I think it's been really good for me.
[407.36 --> 410.48]  So now that you've told us a little bit about your background and the fact that you're
[410.48 --> 415.22]  now at Indeed to kind of give context to our conversation, can you tell us a bit more about
[415.22 --> 415.56]  Indeed?
[415.70 --> 419.60]  I know, obviously, Daniel and I are very familiar with it, but there might be some people out
[419.60 --> 421.94]  there who haven't used it and let them know what it is.
[422.72 --> 423.08]  Absolutely.
[423.60 --> 426.32]  At Indeed, we are the world's number one job site.
[426.66 --> 431.92]  And the main thing that we emphasize, I think I've seen this on at least half of the presentations
[431.92 --> 435.88]  that people give, even internally, is our mission is to help people get jobs.
[435.88 --> 438.38]  And that's what we try to do every day.
[438.66 --> 442.98]  We have like orange chairs in our conference rooms to remind us that the job seeker is always
[442.98 --> 445.96]  the important thing and we need to try to do things that help them.
[446.58 --> 451.66]  So at its core, Indeed has sort of a search product that is well liked where people will
[451.66 --> 456.46]  go and you can search like data scientist jobs in Austin, Texas, and it'll have a list
[456.46 --> 461.02]  of jobs and there's all sorts of filtering and stuff that you can apply to find the right
[461.02 --> 461.46]  job for you.
[461.46 --> 468.12]  So also wondering here, kind of how long has Indeed been investing in data science and machine
[468.12 --> 471.38]  learning and what's their primary focus in that area?
[472.16 --> 472.48]  Definitely.
[472.72 --> 478.50]  So as with any other large internet company, there's a mound of data that you get just
[478.50 --> 479.68]  running an internet company.
[479.98 --> 485.30]  And it's obviously, if you can leverage that well, then you can do a lot of great stuff
[485.30 --> 486.48]  to help people get jobs better.
[486.48 --> 491.26]  And I wasn't involved at the creation of the team, so I can't really speak too much
[491.26 --> 496.06]  to the early parts, the early days, but it's been at least several years of investing in
[496.06 --> 497.84]  data science at our company.
[498.30 --> 504.62]  Some relevant use cases, for instance, salary estimation is one that comes up fairly often
[504.62 --> 509.12]  and it's nice to be able to, for job seekers, it's nice to be able to have some expectation
[509.12 --> 511.54]  of what the salary will be for a given job.
[511.54 --> 517.62]  Another example that ends up being useful in a variety of ways is training models that
[517.62 --> 522.32]  can determine how good of a fit a certain job is for a certain job seeker.
[522.66 --> 524.60]  And that can be leveraged in a few different ways.
[524.76 --> 530.08]  But with the data that we have, we're able to come up with these useful models that we
[530.08 --> 532.46]  can apply in several ways, which has been really nice.
[532.54 --> 537.66]  And I think, I mean, by empirically testing, we've found has really helped us be able to help
[537.66 --> 538.38]  people get jobs better.
[538.38 --> 545.62]  So at Indeed, is it kind of, is data science scattered throughout the teams that are working
[545.62 --> 552.08]  at Indeed, or is there kind of one data science group that consults on different projects?
[552.18 --> 558.18]  I know that those are two kind of common patterns that I've seen that probably each have their
[558.18 --> 559.54]  advantages or disadvantages.
[559.96 --> 564.06]  But at somewhere like Indeed that I'm sure has a lot of different projects going on, how
[564.06 --> 564.82]  does that work?
[564.82 --> 565.88]  Of course.
[566.16 --> 571.04]  So at Indeed, we try to practice something that we call full stack data science, where
[571.04 --> 576.68]  one individual is in charge of everything from coming up with an idea of some model that
[576.68 --> 581.96]  we could build through to gathering the data up about it and generating labels for it in
[581.96 --> 586.20]  some useful way, training the model, doing all the hyperparameter tuning, and then finally,
[586.34 --> 590.82]  you know, getting it deployed to production, writing that production code, monitoring it after
[590.82 --> 592.12]  the fact testing it.
[592.12 --> 594.44]  So that's sort of the model that we try to practice.
[594.78 --> 596.12]  And we find a lot of benefit in that.
[596.24 --> 602.12]  And that enables us to have, you know, a group of data scientists who all end up placed in
[602.12 --> 607.36]  various teams and are able to really provide a lot of value to an individual team in that
[607.36 --> 611.64]  way because they have a wide variety of skills and are able to get something all the way through
[611.64 --> 614.10]  from idea to actually in production.
[614.10 --> 615.78]  Full stack data science.
[615.94 --> 619.10]  I've definitely, I've heard that term a few times recently.
[619.40 --> 624.72]  I don't know if it was from Indeed, but I think that that's starting to be used a little
[624.72 --> 625.38]  bit more widely.
[625.50 --> 626.22]  Have you heard that, Chris?
[626.44 --> 627.04]  I have.
[627.16 --> 629.80]  It's becoming a popular buzzword now.
[629.98 --> 632.34]  So we have formally introduced it on the show here.
[632.42 --> 634.84]  So we are in place.
[634.84 --> 641.60]  I don't know if I can be considered, I think maybe based on your description, Samuel, I
[641.60 --> 647.54]  hope that I'm considered somewhat full stack, but I feel a little bit like cringe calling
[647.54 --> 649.82]  myself a full stack data scientist.
[650.22 --> 652.54]  I feel much better if someone else called me that.
[652.78 --> 654.72]  But anyway, not to get sidetracked.
[654.98 --> 658.84]  Well, actually, before you completely eliminate the sidetrack, it's kind of funny that you say
[658.84 --> 661.42]  that because, you know, we came from software development.
[661.60 --> 663.24]  It sounds like all three of us have come from there.
[663.24 --> 667.52]  And, you know, once upon a time, I did think of myself as a full stack software developer.
[667.66 --> 672.30]  So I wonder if we're going to grow into the sense of being full stack, you know, machine
[672.30 --> 674.24]  learning engineers, data scientists, whatever.
[674.86 --> 679.10]  Do I have to learn more JavaScript to be a full stack data scientist?
[679.32 --> 682.92]  You have to do React with your AI at that point, you know?
[683.94 --> 684.92]  I'll look into that.
[685.06 --> 685.46]  There we go.
[685.56 --> 691.28]  So, hey, you know, I'm trying to recall back, we had, from HireVue, we had Lindsey, I'm
[691.28 --> 692.82]  trying to remember, I'm going to butcher her name.
[692.82 --> 693.30]  Zoolaga.
[693.54 --> 693.94]  Zoolaga.
[694.10 --> 694.64]  That was it.
[695.38 --> 700.74]  And I think that was going back in our late teens, maybe up to episode 17, if I recall.
[701.12 --> 703.84]  She was talking about bias in hiring and data.
[704.42 --> 709.28]  And so, you know, Samuel, I'm kind of wondering, is that something that Indeed is working on
[709.28 --> 709.86]  as well?
[710.20 --> 712.56]  And, you know, it's a pretty big issue out there.
[712.66 --> 715.86]  And if you are working on it, kind of where is Indeed taking it as a company?
[715.86 --> 718.06]  Of course, that's a huge issue.
[718.24 --> 722.16]  Like, it's to the point where that kind of stuff is coming up at conversations at the
[722.16 --> 727.10]  national level, you know, in the presidential debates, people are caring about bias in algorithms
[727.10 --> 728.18]  and bias in data.
[728.18 --> 730.72]  And there are people at Indeed working on that.
[730.86 --> 732.52]  I really can't speak to what they're doing.
[732.62 --> 734.72]  I just am not super familiar with what they're doing.
[734.96 --> 739.28]  One area that I have found interesting that can be somewhat related here is working in
[739.28 --> 744.74]  cases where you have really imbalanced data sets, where you are drawing from where certain
[744.74 --> 748.26]  parts of the population that you're looking at might just be really underrepresented in
[748.26 --> 752.98]  your data set and trying to come up with useful techniques for correcting for that or for making
[752.98 --> 758.16]  sure that your model is still doing well on those subsets of the data that are underrepresented.
[758.40 --> 761.50]  I find really interesting because I feel like that comes up all the time.
[761.58 --> 768.18]  You'll have a case where, for instance, like your target variable could be 1% or 0.0001%
[768.18 --> 772.10]  of the smallest class, and then everything else is the majority class.
[772.20 --> 774.72]  And I found that to be a really interesting problem to try to attack.
[774.72 --> 779.38]  I don't think it's directly related to the issue of bias in machine learning, but I think
[779.38 --> 782.02]  there could be some benefit there to be had for sure.
[782.48 --> 787.94]  You know, I think that is probably the epitome of, you know, the type of area in terms of
[787.94 --> 792.84]  bias and even its extension into, you know, kind of the newfound field of AI ethics.
[793.08 --> 795.34]  And that is the one thing all of us are grappling with.
[795.42 --> 799.48]  I think no matter where we're at is the fact that, you know, we have these data sets and we're
[799.48 --> 800.68]  trying to create great models.
[800.68 --> 802.58]  And that's just a universal challenge.
[802.58 --> 805.20]  Just about everyone I ever talked to says that.
[805.90 --> 806.42]  Yeah, definitely.
[806.86 --> 808.36]  It's hard to grapple with for sure.
[808.84 --> 808.96]  Yeah.
[809.04 --> 814.56]  Every time I encounter that, it makes you stop and kind of take a step back and really think
[814.56 --> 820.32]  through your process and really how your data was generated, what the implications are of
[820.32 --> 822.88]  different sampling techniques and all of those things.
[823.22 --> 823.38]  Yeah.
[823.50 --> 825.56]  It's hard every time I encounter it, it seems like.
[825.56 --> 832.10]  So, Samuel, given that you work at Indeed and given that, like, data scientists are in
[832.10 --> 839.36]  demand and, you know, machine learning, AI is all the rage, do you have any sort of general,
[839.56 --> 844.08]  maybe just from your personal experience or patterns that you've seen, do you have any
[844.08 --> 849.52]  recommendations around, hey, I'm looking for an AI job or I'm looking for a data science
[849.52 --> 849.90]  job?
[849.90 --> 854.96]  What are maybe some good things to avoid or some good things to do generally as you're
[854.96 --> 856.68]  kind of going through that hiring process?
[857.60 --> 857.90]  Definitely.
[858.12 --> 862.64]  So, obviously, I can only really speak to what I know and what I know is how I got into this.
[862.86 --> 869.32]  And I think one of the biggest things that helped me get into this field was being able
[869.32 --> 874.16]  to work on sort of side projects, you know, either after work or on the weekends or something.
[874.16 --> 879.26]  I know that's not always an option for people who are busy or have kids, but if you can,
[879.40 --> 884.44]  if you do have the chance to do that, I think that's a really strong way to both just develop
[884.44 --> 888.24]  the skills and run into problems that you're going to run into in real life, but also to
[888.24 --> 892.28]  have a sort of portfolio to show to people and say, hey, look at all the cool things I
[892.28 --> 892.88]  can do with this.
[893.00 --> 898.48]  People are a lot more likely to take you seriously if you have some sort of example that you can
[898.48 --> 901.28]  show them of, here's the thing I built, look at how neat this is.
[901.28 --> 905.84]  And it can be a really good way to get on someone's radar if you can send them a link,
[906.04 --> 910.58]  for instance, to a website that you made that does some cool machine learning-y thing and
[910.58 --> 912.84]  they can play around with it and be like, oh, this is fun.
[913.16 --> 917.92]  And even if that website isn't super complicated, they still might end up being, you know, it
[917.92 --> 920.10]  helps set you apart from the rest of the crowd.
[931.28 --> 936.32]  This episode is brought to you by Brave.
[936.82 --> 942.08]  The Brave team is on a mission to fix the web by building an open source, privacy-focused,
[942.40 --> 944.40]  and performance-oriented browser.
[944.98 --> 947.90]  Browse the web up to eight times faster than Chrome and Safari.
[948.48 --> 950.44]  Block ads and trackers by default.
[950.78 --> 954.52]  And reward your favorite creators with the built-in basic attention token.
[955.12 --> 956.38]  Yes, you heard that right.
[956.46 --> 958.56]  A real-world use case for blockchain.
[958.56 --> 964.58]  Download Brave for free using the link in the show notes and give tipping a try on changelog.com.
[973.84 --> 977.66]  So Samuel, let's turn toward all things open.
[977.90 --> 982.80]  I'm familiar with it, and I know Daniel is, but there may very well be people in the audience
[982.80 --> 983.32]  that aren't.
[983.32 --> 988.84]  Could you kind of tell people what All Things Open is about and, you know, what organization
[988.84 --> 989.90]  backs it, that kind of stuff?
[990.78 --> 991.44]  Yeah, definitely.
[991.74 --> 1000.60]  So All Things Open is this just massive conference that takes place in North Carolina, in Raleigh,
[1000.64 --> 1005.96]  North Carolina, and has several thousand, I think it's in the three or four thousands of
[1005.96 --> 1007.64]  people that show up to this thing.
[1007.84 --> 1009.32]  So I haven't gotten to go before.
[1009.32 --> 1013.02]  I'm really excited to because conferences are always just a blast.
[1013.46 --> 1018.88]  Anytime you get around like 3,000 other nerds and you're all just like there to celebrate
[1018.88 --> 1021.46]  the nerdy things that you like, it's always a good time.
[1021.88 --> 1023.10]  There's always really interesting people.
[1023.22 --> 1024.72]  So I'm really excited to get to go.
[1025.50 --> 1025.58]  Yeah.
[1025.70 --> 1029.64]  And I think especially, I don't know if this has been your experience, Samuel, but like
[1029.64 --> 1034.66]  at conferences that are very open source focused and sort of have a community vibe,
[1034.66 --> 1039.62]  there's just a lot of excitement there and, you know, always interesting people to talk
[1039.62 --> 1046.46]  to and really, really interesting kind of random but awesome projects that probably wouldn't
[1046.46 --> 1050.96]  get highlighted at like very, very expensive industry conferences.
[1050.96 --> 1052.66]  Is that your impression as well?
[1053.30 --> 1054.00]  Oh, yeah, definitely.
[1054.42 --> 1059.50]  I have had, I mean, I've gone to some other more community open source e kind of conferences
[1059.50 --> 1064.10]  and the people you run into, you'll just sit down with someone and not know anything about
[1064.10 --> 1066.70]  them and start asking, oh, you know, what do you do?
[1066.78 --> 1067.96]  What kind of stuff do you work on?
[1068.34 --> 1072.28]  And they'll have this like incredible project that they're using to build their rugby league
[1072.28 --> 1074.10]  and like recruit people for this league.
[1074.12 --> 1076.16]  And you're like, I'm amazed that you came up with this, you know?
[1076.46 --> 1079.78]  So it's always cool to get to both run into people, but then also see them featured
[1079.78 --> 1081.56]  in the program itself is cool too.
[1082.58 --> 1083.08]  Yeah, definitely.
[1083.30 --> 1086.92]  And I did look it up because, you know, the internet can help with these things.
[1086.92 --> 1091.30]  And it is opensource.org that at least is partially behind the conference.
[1091.42 --> 1092.80]  I don't know the exact structure there.
[1093.22 --> 1094.16]  But yeah, cool.
[1094.26 --> 1097.74]  Well, we're really excited that you're getting featured there.
[1097.86 --> 1101.76]  And also a lot of other machine learning things are getting featured there that I saw.
[1102.42 --> 1104.12]  But maybe just for our listeners.
[1104.48 --> 1109.88]  So probably a lot of our listeners that maybe come over from the ChangeLog or another one of
[1109.88 --> 1115.64]  the ChangeLog podcasts might be familiar with open source and kind of that community in general.
[1115.64 --> 1121.36]  But some like data scientists and AI people maybe coming from academia or working in research,
[1121.52 --> 1129.44]  maybe it's a little bit less clear like what open source means and where you sort of like
[1129.44 --> 1131.78]  how you get open source software.
[1132.16 --> 1133.70]  And is it always free?
[1133.94 --> 1137.36]  What are the sort of like what is the community around it?
[1137.42 --> 1138.22]  How is it created?
[1138.64 --> 1140.32]  Could you kind of talk a little bit about that?
[1140.32 --> 1146.24]  Just kind of like what is open source and how you were initially exposed to open source,
[1146.36 --> 1146.52]  maybe?
[1147.40 --> 1153.64]  Open source software is this crazy, amazing collective of people who see a problem with
[1153.64 --> 1159.82]  something or need to do something and somehow come together and self-organize to create a
[1159.82 --> 1160.92]  lot of the world's software.
[1160.92 --> 1166.54]  I am sure that if you're listening to this podcast, you are using open source software
[1166.54 --> 1171.32]  at some level, whether it's the server that's hosting this MP3 file or if it's the actual
[1171.32 --> 1172.94]  software you're using to play it back.
[1173.00 --> 1175.46]  I'm sure there's some part of open source software in there.
[1176.46 --> 1176.56]  Yeah.
[1176.68 --> 1182.42]  So it's not just like free apps or something that's like in a lot of cases, tooling or lower
[1182.42 --> 1187.92]  level things that are just available widely that are integrated into all sorts of different
[1187.92 --> 1190.56]  applications that may even be commercial applications.
[1190.56 --> 1191.94]  Yeah, absolutely.
[1192.22 --> 1197.92]  And a lot of the, like I was mentioning, web servers, a lot of web servers run on Linux,
[1198.02 --> 1201.76]  which is this amazing open source piece of software that people have been building and
[1201.76 --> 1203.22]  maintaining for decades now.
[1203.48 --> 1209.04]  And it's really interesting to see the kind of collaboration that the internet enables
[1209.04 --> 1211.50]  and the kind of governance models that people come up with.
[1211.80 --> 1214.42]  Like you said, not all open source software is free.
[1214.58 --> 1218.96]  There are some discussions within the open source and free software communities about the
[1218.96 --> 1220.02]  differences between those.
[1220.34 --> 1225.40]  And when people talk about free software, there's either the free as in you're not paying for
[1225.40 --> 1229.34]  it or free as in sort of like a free as in freedom or free as in liberty kind of thing.
[1229.66 --> 1234.42]  And some people really appreciate that aspect of it too, because when you have software that is
[1234.42 --> 1237.86]  free as in freedom, that means that you have the right to change it.
[1237.90 --> 1240.56]  And if it doesn't suit your needs, you can go in and modify it.
[1240.56 --> 1244.32]  And there's some aspect of that that can be really satisfying for people who are using
[1244.32 --> 1247.84]  software and always want to have the ability to make it work like they want it to.
[1248.34 --> 1248.82]  Yeah.
[1248.94 --> 1255.04]  And we should just mention kind of for those just getting into software or AI or open source
[1255.04 --> 1259.22]  machine learning tooling and all of this, like most of the time you can find these sorts
[1259.22 --> 1261.26]  of projects, for example, on GitHub.
[1261.50 --> 1262.14]  Not always.
[1262.46 --> 1267.32]  It's definitely like various NLP things and other things that I've used where it just like
[1267.32 --> 1271.18]  downloaded off of some university site or something like that.
[1271.18 --> 1278.80]  But for the most part, anyone can like create a GitHub repo and open source their like project
[1278.80 --> 1284.78]  or their the code associated with their research paper or whatever that is.
[1284.78 --> 1291.26]  I'm curious, Samuel, have you kind of open source things or been involved on that side of things?
[1291.70 --> 1292.64]  I have a little bit.
[1292.88 --> 1298.66]  There was a project that I worked on in college where I at the time couldn't find a good
[1298.66 --> 1304.64]  recommender systems library for Python and sort of hacked my own together and then put
[1304.64 --> 1305.56]  that onto PyPI.
[1305.78 --> 1310.22]  That is long since dead, but it was really informative learning how to package up Python
[1310.22 --> 1313.04]  software and get it out to where people could actually use it.
[1313.18 --> 1318.42]  So I think even if the project doesn't become a success, like there's way better recommender
[1318.42 --> 1321.74]  systems libraries out there for Python now than that thing ever would have been.
[1322.10 --> 1326.68]  But despite that, there was still a lot of value in learning how to do that kind of stuff
[1326.68 --> 1331.04]  because you're going to, you know, potentially need to ship something to your internal PyPI
[1331.04 --> 1332.42]  at work or something like that.
[1332.66 --> 1338.24]  So, you know, it's interesting, you know, unlike, you know, the original software development
[1338.24 --> 1343.26]  world where there was lots of closed source and open source kind of grew over the years
[1343.26 --> 1344.56]  and even over the decades.
[1344.56 --> 1349.88]  We've had this really cool situation where machine learning and AI tools have started
[1349.88 --> 1351.64]  off as open source.
[1351.80 --> 1356.20]  I mean, some of the most popular, you know, in this area are like TensorFlow, which was
[1356.20 --> 1359.74]  open source by Google and PyTorch, which was open source by Facebook.
[1360.10 --> 1366.90]  And so I guess my question is, why do you think that having open source in the machine learning
[1366.90 --> 1370.44]  and artificial intelligence fields is important?
[1370.44 --> 1373.96]  And, you know, why do you feel that they probably started it off that way?
[1374.80 --> 1374.90]  Yeah.
[1375.02 --> 1376.62]  So let's do that in two parts.
[1376.62 --> 1380.22]  I have a theory as to why things are this way.
[1380.34 --> 1387.08]  My personal theory is that really high level researchers, people who are advancing the state
[1387.08 --> 1391.62]  of the art, really like to be able to publish their work openly and be recognized for the
[1391.62 --> 1392.30]  cool work they're doing.
[1392.98 --> 1397.52]  So my theory is that because they come from this culture of academia where it is important
[1397.52 --> 1402.48]  to publish things publicly that, well, then, you know, I'm going to publish my code as
[1402.48 --> 1404.56]  well because that's part of the research that I did.
[1404.78 --> 1405.92]  So that's kind of my theory.
[1406.12 --> 1409.98]  It's not empirically validated in any way, but that's my theory on why that would be.
[1410.08 --> 1411.98]  Spoken like a true data scientist.
[1413.04 --> 1418.02]  What do you think about just trying to get, you know, uptake on your tool and, you know,
[1418.02 --> 1423.74]  by making it, you know, for instance, back in 2015, if Google had not open sourced TensorFlow,
[1423.74 --> 1428.36]  maybe it had not, it would not have gotten such tremendous uptake as it did.
[1428.48 --> 1430.24]  And subsequently, Facebook as well.
[1430.38 --> 1434.18]  I mean, trying to, do you think there's an intent of trying to capture Mindshare in the
[1434.18 --> 1434.48]  community?
[1435.24 --> 1435.58]  Absolutely.
[1435.76 --> 1435.90]  Yeah.
[1435.92 --> 1439.90]  I think that's really important to these large software companies.
[1440.30 --> 1445.98]  My understanding is that when Google wrote a bunch of these papers for what ended up becoming
[1445.98 --> 1450.84]  Hadoop, they kind of saw the Hadoop world rebuild a lot of the internal tools they had.
[1450.84 --> 1454.76]  And then, you know, it's good because you sort of build that mindshare of knowing what
[1454.76 --> 1456.16]  MapReduce is, for instance.
[1456.36 --> 1459.62]  But then when you're hiring someone and they come in, it's like, well, this is a little
[1459.62 --> 1461.14]  different from the MapReduce you're used to.
[1461.26 --> 1466.16]  And so if they just start right out the gate, open sourcing TensorFlow, then when they are
[1466.16 --> 1469.60]  hiring new data scientists, they're going to know exactly what TensorFlow is and already
[1469.60 --> 1470.20]  be using it.
[1470.28 --> 1472.38]  So I think there's a lot of benefit to it.
[1472.90 --> 1473.26]  I agree.
[1473.34 --> 1474.98]  I think, I think that you hit on the point.
[1474.98 --> 1479.52]  I remember, you know, that going around the community, that exact issue of Google kind
[1479.52 --> 1483.70]  of saying, wow, we kind of created this up front, but since we didn't open source, somebody
[1483.70 --> 1486.76]  kind of turned around and we had to react to them later on.
[1487.02 --> 1491.14]  And I think that also happened to some degree with containerization with them.
[1491.22 --> 1495.50]  And so maybe, maybe in that particular case with that particular organization, maybe that
[1495.50 --> 1497.80]  was a lesson learned that they finally turned it right.
[1497.90 --> 1502.90]  And, and obviously that must have worked well for them because TensorFlow has a huge percentage
[1502.90 --> 1503.36]  of the market.
[1503.36 --> 1504.76]  So absolutely.
[1505.70 --> 1505.82]  Yeah.
[1505.90 --> 1511.60]  And I, I think that there's such a wide range of open source things now.
[1511.74 --> 1517.32]  I mean, I can't imagine doing any sort of AI project without open source tooling of, of
[1517.32 --> 1524.02]  some kind, but it's even past like TensorFlow and, and PyTorch now where like people are kind
[1524.02 --> 1529.32]  of sharing their pre-trained models, they're sharing data sets and, and all of those things.
[1529.32 --> 1535.56]  And of course this is kind of also created some, like a little bit of backlash in the sense
[1535.56 --> 1542.98]  that like, you know, uh, open AI models and others have been kind of deemed like dangerous
[1542.98 --> 1546.04]  and, Oh, maybe we shouldn't be releasing this code.
[1546.04 --> 1552.64]  And there's also like, it's kind of weird now that research is so close to applications.
[1552.64 --> 1558.44]  So like people release a paper and then there's like three implementations on GitHub, like the
[1558.44 --> 1559.02]  next day.
[1559.02 --> 1559.34]  Right.
[1559.34 --> 1565.08]  So what's your perspective on that Samuel in terms of like, should researchers and data
[1565.08 --> 1567.78]  scientists always be open sourcing things?
[1567.78 --> 1572.26]  Or do you think that there's, there's limits and boundaries within which we should work?
[1572.26 --> 1578.26]  I think of course there are times where it doesn't make sense to open source something
[1578.26 --> 1579.52]  or to release a data set.
[1579.52 --> 1584.72]  For instance, I imagine if you're Visa and you have a fraud detection algorithm, you
[1584.72 --> 1587.76]  definitely don't want to release that because then people are going to start doing really
[1587.76 --> 1589.58]  good credit card fraud to evade your algorithm.
[1589.58 --> 1589.88]  Right.
[1589.98 --> 1595.80]  But there's other cases where I think it does sort of help the species like humanity to get
[1595.80 --> 1599.42]  further along and understand how we can do certain things.
[1599.42 --> 1603.28]  So I will not pretend to be an expert about when is best.
[1603.50 --> 1606.82]  I can sort of see that there's cases where it's good and cases where it's bad.
[1607.24 --> 1611.78]  I probably tend toward thinking that there's something noble about trying to advance the
[1611.78 --> 1615.86]  frontier of human knowledge, but at times that isn't the right choice.
[1615.94 --> 1619.04]  And at times you have to have to make a difficult decision and not do that.
[1619.88 --> 1625.54]  You know, before I just thought I'd mention, I can give you an almost comical instance that
[1625.54 --> 1628.76]  I just read about where maybe open source wouldn't be a solution.
[1628.76 --> 1633.08]  Which is strange coming out of my mouth because I think all three of us are huge open source
[1633.08 --> 1633.48]  advocates.
[1633.48 --> 1639.20]  There was a push by the government accountability office for Department of Defense to, or kind
[1639.20 --> 1644.00]  of really all government agencies to try to open source 20% of the code they write, which
[1644.00 --> 1645.78]  in general, I love that idea.
[1646.20 --> 1651.96]  But there was pushback from the DOD CIO, the Department of Defense CIO, and I'm paraphrasing,
[1652.08 --> 1653.66]  I'm not quoting because I don't have it in front of me.
[1653.66 --> 1658.66]  But he basically said, well, our code is building is for weapon systems.
[1658.66 --> 1663.92]  And so we're not going to put the weapon system code out there in open source, which
[1663.92 --> 1666.10]  I just, I thought was kind of hilarious personally.
[1667.06 --> 1667.54]  Yeah.
[1667.68 --> 1674.14]  I mean, there's definitely, I don't know, domain specific situations like that.
[1674.14 --> 1679.20]  But I guess there's like, there is this side of like research where it's like, oh, we don't
[1679.20 --> 1681.70]  know exactly the implications of this.
[1681.78 --> 1683.98]  So maybe we're going to, maybe we're going to hold off.
[1684.28 --> 1688.36]  Anyway, moving past some of those like caveats, I guess.
[1688.52 --> 1694.56]  What are some of the, if you were to pick some of your, your favorite open source machine
[1694.56 --> 1699.06]  learning or AI projects that you use really frequently, what would, what would those be,
[1699.16 --> 1699.34]  Samuel?
[1699.34 --> 1705.40]  So I would have to start with Jupyter because I think almost every data scientist has at
[1705.40 --> 1707.50]  least run into a Jupyter notebook at some point.
[1707.80 --> 1711.50]  I don't know that I've had a day without using one since I started working.
[1711.68 --> 1716.78]  They're just incredibly useful ways to sort of see the results of your computation and
[1716.78 --> 1720.78]  experiment with things and prototype with things in a way that can be a lot less friction
[1720.78 --> 1722.64]  than traditional IDE.
[1723.06 --> 1724.04]  That'd be what I would start with.
[1724.04 --> 1729.38]  Also have to give a huge shout out to scikit-learn because it has an incredible API.
[1729.64 --> 1730.96]  The community is really strong.
[1731.08 --> 1737.46]  The documentation is really good and you can get a lot done with just everything built
[1737.46 --> 1739.06]  in scikit-learn, which is great.
[1739.40 --> 1741.68]  So those would be the two that I would give the biggest shout out to.
[1741.88 --> 1746.70]  If you have Jupyter and scikit, you can do a lot of stuff for sure.
[1746.70 --> 1747.70]  Thanks.
[1756.02 --> 1757.64]  Greetings, AI practitioners.
[1758.04 --> 1762.16]  Jared here, wanting to let you know that Changelog will be at All Things Open on October
[1762.16 --> 1763.48]  14th and 15th.
[1763.96 --> 1768.86]  We're hosting a live JS party on stage and as a special thanks from the organizers, we're
[1768.86 --> 1770.80]  giving away five free passes to the conference.
[1770.80 --> 1776.14]  All you have to do is tweet, I want a free pass to All Things Open because, state your
[1776.14 --> 1782.18]  reason and mention at Changelog or at PracticalAIFM so we see it and we will DM you if you win.
[1782.54 --> 1783.66]  Okay, that's all for me.
[1783.90 --> 1784.76]  Let's get back into it.
[1784.76 --> 1800.18]  So I am assuming that Indeed is not paying you to make music recommendation systems like
[1800.18 --> 1802.40]  you had mentioned in your ATO abstract.
[1802.86 --> 1804.88]  What kind of side projects are you engaged in?
[1805.04 --> 1809.12]  What are you doing and what's fun and what would you like to do that you may not have
[1809.12 --> 1809.68]  gotten to yet?
[1810.38 --> 1810.82]  Definitely.
[1810.82 --> 1815.84]  So there are machine learning related side projects and there are just sort of fun side
[1815.84 --> 1816.40]  projects.
[1816.64 --> 1822.32]  So as a fun one I'll start with, I do some volunteer coding instruction and I think that's really
[1822.32 --> 1825.96]  enjoyable and that's one of the most fun things that I do that's not work.
[1826.12 --> 1830.08]  As far as machine learning related projects, and these are some that I talk about in the
[1830.08 --> 1835.06]  talk actually, is working on some recommender system stuff I think has been really interesting.
[1835.36 --> 1839.96]  Trying to predict whether a certain musical artist will be liked by a certain user I think
[1839.96 --> 1843.12]  is a hard problem for sure, but really interesting.
[1843.12 --> 1846.18]  Are there like open source data sets related to that?
[1846.60 --> 1847.08]  There are, yeah.
[1847.20 --> 1852.68]  There's a conference called Rexis that released this massive data set that people gathered
[1852.68 --> 1853.88]  Last.fm data.
[1854.28 --> 1859.34]  Last.fm is this social music sharing website where people, their music client will submit
[1859.34 --> 1863.60]  that they're listening to certain music and then some researchers went out and scraped
[1863.60 --> 1865.28]  a bunch of data and put it into this thing.
[1865.58 --> 1869.06]  Now that's part of the open record and you can get this data, which is interesting.
[1869.06 --> 1869.10]  Interesting.
[1869.76 --> 1873.84]  Like, so you have that data in terms of like doing the recommendations.
[1873.84 --> 1879.58]  How did open source factor into kind of the way that you went about implementing a solution
[1879.58 --> 1879.94]  to that?
[1880.58 --> 1881.14]  Yeah, absolutely.
[1881.58 --> 1885.48]  The main thing I would say that it was helpful with for this specific problem was trying to
[1885.48 --> 1887.66]  do data exploration and visualization.
[1888.32 --> 1892.58]  I mentioned Jupyter earlier and that was a big part in the prototyping phase of this project.
[1892.84 --> 1897.52]  Another thing that was really useful was Pandas, which is a really good library for dealing
[1897.52 --> 1898.64]  with tabular data.
[1898.64 --> 1902.84]  If you have data that is rows and columns, use Pandas.
[1903.04 --> 1903.48]  It's great.
[1904.22 --> 1910.76]  And then also leveraging some tools like Matplotlib and Seaborn to do data visualization and try
[1910.76 --> 1916.98]  to see what sort of correlations exist in the data to try to get a first pass at what might
[1916.98 --> 1918.74]  be a useful model to start to build.
[1919.08 --> 1921.46]  I think those tools ended up being really useful.
[1921.46 --> 1926.76]  Do you have any other projects in particular that you've worked on or anything that you're
[1926.76 --> 1928.84]  aspiring to when you get enough time to?
[1929.56 --> 1929.72]  Yeah.
[1929.86 --> 1935.58]  So there's one that I started working on actually before I got it Indeed, where I wanted to
[1935.58 --> 1938.30]  use machine learning to find my next job.
[1938.40 --> 1940.06]  I just thought that was a really fun idea.
[1940.54 --> 1947.14]  And what that ended up being was I made a spreadsheet and read just a ton of job descriptions
[1947.14 --> 1950.10]  descriptions and pasted them in this spreadsheet and then rated them.
[1950.40 --> 1954.62]  And if I'm being honest, I definitely spent more time reading job descriptions this way
[1954.62 --> 1956.44]  than I would have any other way.
[1956.54 --> 1960.92]  But I would read them and try to figure out if they were cool or not and then have a training
[1960.92 --> 1963.06]  model to try to do this for me.
[1963.30 --> 1967.22]  And what I ended up doing, I mean, I don't have this email going anymore because I like
[1967.22 --> 1967.62]  my job.
[1967.62 --> 1972.42]  But what I ended up doing was having it do this weekly email where it would send me the
[1972.42 --> 1976.32]  top 10 jobs that sounded the coolest that went up that week, which I just thought
[1976.32 --> 1979.46]  was a fun little way to make your own life easier.
[1979.68 --> 1982.64]  I think that's a great way to get started with these machine learning projects.
[1982.76 --> 1986.70]  And like I was alluding to earlier, when you are trying to build a portfolio, it's cool
[1986.70 --> 1992.40]  to work on something that you actually want to solve because first off, it shows the potential
[1992.40 --> 1996.06]  employer what things you find interesting and you can inject some of your personality
[1996.06 --> 1996.60]  into that.
[1996.60 --> 2001.30]  And then second off, that you will be more motivated to work on the project.
[2001.86 --> 2002.42]  That's a great point.
[2002.96 --> 2003.52]  Yeah, definitely.
[2003.52 --> 2009.42]  I think passion is a big part of that that really helps with side projects.
[2009.74 --> 2015.58]  But yeah, I think you mentioned maybe a third project in your abstract having to do, was
[2015.58 --> 2016.64]  it something with sign language?
[2017.42 --> 2017.70]  Yes.
[2017.88 --> 2018.10]  Yes.
[2018.16 --> 2022.80]  So there was a, actually at a hackathon, a friend and I built a little thing that would
[2022.80 --> 2028.20]  try to predict what sign you were making of the American Sign Language alphabet.
[2028.20 --> 2033.82]  So American Sign Language is a really interesting language that is not just English with your
[2033.82 --> 2034.10]  hands.
[2034.22 --> 2035.46]  It's much different from that.
[2036.00 --> 2039.58]  And a friend and I went to a hackathon and we had this little device that could read hand
[2039.58 --> 2041.48]  position data when you plugged it into your laptop.
[2042.12 --> 2045.10]  And we thought, what if we could teach a computer sign language?
[2045.10 --> 2046.56]  That sounds really awesome.
[2046.66 --> 2047.36]  Wouldn't that be cool?
[2047.36 --> 2047.72]  Cool.
[2048.02 --> 2050.68]  And then we realized we only had 24 hours and that was not going to work.
[2050.84 --> 2055.00]  But what we did realize was that we could at least start with trying to get it to learn
[2055.00 --> 2055.38]  the alphabet.
[2055.78 --> 2060.86]  And so, you know, we gathered some training data and then, you know, did some model selection
[2060.86 --> 2063.10]  and found a model that worked reasonably well.
[2063.42 --> 2066.52]  And now I get to tell people that I taught a computer sign language.
[2066.52 --> 2067.32]  It's not true.
[2067.60 --> 2070.86]  Like the computer doesn't actually know sign language, but I can at least say that I, you
[2070.86 --> 2074.82]  know, with a caveat, was able to teach this computer something about sign language, which
[2074.82 --> 2075.20]  is cool.
[2075.74 --> 2079.26]  And what we ended up doing was turning this into a little learning game.
[2079.40 --> 2083.96]  We called it kind of like a Rosetta Stone, but for sign language, where it would show
[2083.96 --> 2087.98]  you a picture of a hand sign and say, hey, make an A. And you would make a little hand
[2087.98 --> 2089.68]  sign of an A above this sensor.
[2089.98 --> 2091.82]  And then once you got it right, it would say, great job.
[2091.88 --> 2093.00]  And, you know, give you some points.
[2093.34 --> 2095.26]  So that was a fun hackathon project.
[2095.26 --> 2100.14]  It was really interesting and ended up having surprising applications to the real world
[2100.14 --> 2105.48]  of like defining a limited scope and working iteratively and ended up, I think, surprising
[2105.48 --> 2108.50]  myself with how useful that project and the things I learned on that ended up being.
[2109.16 --> 2112.12]  Yeah, I'm so happy for you to share that.
[2112.58 --> 2118.46]  So obviously, as our listeners know, I'm very much involved in the world of AI and language
[2118.46 --> 2121.96]  and especially minority languages, which includes sign language.
[2121.96 --> 2130.68]  And yeah, I think if anybody out there wants a really cool, innovative and, you know, highly
[2130.68 --> 2136.18]  impactful project to work on, like working on sign language tech is really interesting
[2136.18 --> 2136.88]  AI wise.
[2137.02 --> 2140.56]  I know a couple of people that are working in that area and just doing amazing thing,
[2140.68 --> 2146.94]  like things like processing video from like three different directions and reconstructing
[2146.94 --> 2150.24]  hand motions in 3D and all sorts of amazing stuff.
[2150.24 --> 2153.38]  So I'm glad you were you're able to share that.
[2153.66 --> 2154.70]  That was at a hackathon.
[2155.08 --> 2160.06]  How much time and how often do you are you doing side projects?
[2160.06 --> 2161.42]  I'm kind of curious about that.
[2162.08 --> 2162.42]  Absolutely.
[2162.58 --> 2167.92]  So since I've got some things working, like I'm married and I have a volunteering thing
[2167.92 --> 2172.18]  that I do weekly, I don't put a ton of time into side projects at this point just
[2172.18 --> 2174.78]  because there's other things that I'm choosing to prioritize.
[2174.78 --> 2180.34]  But I think they were a really great way to scratch that itch for wanting to learn how
[2180.34 --> 2181.96]  to do machine learning by practice.
[2182.24 --> 2186.50]  And then I think partially, partially because of other time constraints and partially because
[2186.50 --> 2189.92]  of the fact that I get to scratch that itch actually at work now.
[2190.14 --> 2193.26]  I don't feel as much need to do that outside of work.
[2193.30 --> 2196.02]  But every now and again, something will come up where I'm just like, I need this.
[2196.08 --> 2196.68]  I need this thing.
[2196.74 --> 2197.46]  I'm going to go build it.
[2197.46 --> 2200.86]  So what do you think makes a good side project?
[2200.98 --> 2202.92]  A lot of people I know do that.
[2203.30 --> 2206.06]  We have what we do at work and then we all have our own little things.
[2206.14 --> 2208.32]  What do you think makes it worthwhile?
[2208.48 --> 2210.50]  What lends itself to being a great side project?
[2211.36 --> 2217.14]  The ones that I have found most fun to work on and the ones that other people seem to think
[2217.14 --> 2220.84]  are the coolest are things that are sort of tangible.
[2221.20 --> 2226.48]  So as an example, I have a website where you can go and type in a word and it'll try to
[2226.48 --> 2228.14]  make up puns based on that word.
[2228.32 --> 2233.58]  So if you type in Sam, for instance, into the thing and you click, give me some puns,
[2233.66 --> 2235.98]  it'll say like, ah, we're all in the Sam boat.
[2236.12 --> 2236.60]  Ah ha ha.
[2237.02 --> 2238.90]  You know, give really bad dad jokes like that.
[2239.24 --> 2241.56]  And I mean, it was a fun thing to work on.
[2241.70 --> 2243.12]  Sounds really useful for my life.
[2244.68 --> 2245.04]  Yeah.
[2245.58 --> 2249.76]  I mean, it's a fun thing to work on because it kind of has an element of humor and joy to
[2249.76 --> 2249.98]  it.
[2249.98 --> 2254.18]  And then part of what's enjoyable about working on a side project is showing it to people.
[2254.18 --> 2258.94]  And when you have something like that and you're able to get it out into the world, like
[2258.94 --> 2263.30]  anyone can go to puns.samueltaylor.org and try out this thing.
[2263.46 --> 2264.04]  Anybody can.
[2264.20 --> 2267.42]  And you can show it to your friends and say, hey, type your name into this, see what comes
[2267.42 --> 2267.66]  up.
[2267.84 --> 2269.34]  And it's really fun.
[2269.38 --> 2273.00]  So I think that's part of it is the joy of getting to share it with other people is
[2273.00 --> 2273.50]  really fun.
[2273.86 --> 2277.40]  In other cases, I think side projects don't have to be broadly useful.
[2277.40 --> 2282.50]  If you can find something that is extremely useful to you, that's a definitely a great place
[2282.50 --> 2283.02]  to start.
[2283.40 --> 2288.56]  If you can have this job email, for instance, that was really applicable to me at one point
[2288.56 --> 2289.04]  in my life.
[2289.08 --> 2289.96]  And it was really useful.
[2289.96 --> 2291.26]  And the time was well spent.
[2291.36 --> 2292.24]  And I learned a lot from it.
[2292.62 --> 2296.78]  And you might be surprised to find out that things that are extremely useful to you end
[2296.78 --> 2298.48]  up being useful to other people as well.
[2298.84 --> 2299.92]  So I'd say those are the first two things.
[2299.98 --> 2302.72]  And then the last one, which we've already talked about, is something that you just find
[2302.72 --> 2303.16]  interesting.
[2303.16 --> 2306.52]  And you feel an itch to scratch that thing.
[2306.52 --> 2312.50]  So let's say you're working on a side project or in your main job, you have some sort of
[2312.50 --> 2314.82]  machine learning AI project going.
[2315.42 --> 2319.90]  And you say, OK, well, I have this issue or I need to do X, Y, Z.
[2320.18 --> 2324.96]  I need to do recommendation or I need to parse this type of data or I need to scrape this type
[2324.96 --> 2328.26]  of data or I need to train this type of model.
[2328.50 --> 2331.12]  There's so much open source out there.
[2331.12 --> 2339.02]  How do you go about finding the right tool for the right situation and also sort of validating,
[2339.14 --> 2343.94]  especially if you're doing this for your job, how do you go about kind of validating if
[2343.94 --> 2350.54]  this thing actually works as it's supposed to or will be stable for any period of time
[2350.54 --> 2355.18]  or robust in any sort of way if you're just kind of grabbing stuff off of GitHub?
[2355.52 --> 2357.86]  What is your process for doing that?
[2357.86 --> 2362.82]  Because I know I've learned certain things over time, but I'm curious what your perspective
[2362.82 --> 2363.14]  is.
[2363.88 --> 2364.28]  Definitely.
[2364.46 --> 2368.74]  So I'm going to cheat a little bit and say that the easiest way to do this is to find
[2368.74 --> 2370.62]  someone you trust and ask them about that.
[2370.86 --> 2375.08]  So if you have other data scientists that you work with and you can walk up to them and
[2375.08 --> 2377.20]  say, hey, I'm running into this issue.
[2377.68 --> 2379.72]  Do you know any packages that might be helpful?
[2379.84 --> 2382.40]  And if they know something, hopefully they've vetted it.
[2382.86 --> 2384.10]  So that's the cheating way.
[2384.10 --> 2389.26]  If you can't do that, then one of the things that I actually try to instill in the talk
[2389.26 --> 2393.08]  is when you run into a kind of data that you don't know how to represent, just Google it.
[2393.26 --> 2397.06]  Like search, how do I do text with machine learning, for instance, and you'll get a lot
[2397.06 --> 2397.42]  of results.
[2398.12 --> 2402.26]  And I mean, you might have to wade through a little bit and figure out what kind of seems
[2402.26 --> 2407.38]  to be the most popular way of doing that and figure out, oh, I'll use TF-IDF, for instance.
[2407.80 --> 2412.38]  So the third kind of way, I would say if you're looking at projects on GitHub, and this is kind
[2412.38 --> 2417.36]  of still cheating, but you can do some amount of validation by looking at how many stars
[2417.36 --> 2419.36]  something has and how many forks things have.
[2419.92 --> 2424.98]  If something has a lot of activity related to it, it's a good chance that it is well-maintained.
[2425.76 --> 2430.90]  So could you describe a little bit more like how that activity is represented, like on GitHub,
[2431.08 --> 2431.48]  for example?
[2431.58 --> 2438.58]  You mentioned stars, activity, like how is that activity kind of represented or what could
[2438.58 --> 2439.32]  you be looking for?
[2439.32 --> 2440.68]  Yeah, yeah, of course.
[2440.82 --> 2447.46]  So when you go to a GitHub repository, in the top right-ish of the page, there'll be a thing
[2447.46 --> 2450.82]  that says stars and a thing that says forks, and they'll have little numbers next to them.
[2451.20 --> 2453.22]  You might see a project that has 27 stars.
[2453.50 --> 2458.86]  What that means is that 27 individuals have landed on that page and thought, oh, this is
[2458.86 --> 2459.08]  cool.
[2459.50 --> 2460.66]  I'll bookmark that for later.
[2460.74 --> 2461.82]  And they click the little star button.
[2461.86 --> 2462.36]  That's all it means.
[2462.46 --> 2465.26]  It's not a vetting of the quality necessarily.
[2465.26 --> 2470.28]  But it is some amount of measurement or proxy for popularity.
[2470.70 --> 2475.78]  And generally, if something is more popular, you'll generally have more eyes on it and more
[2475.78 --> 2480.40]  people depending on it and people to run into bugs before you do and that kind of thing.
[2480.66 --> 2484.86]  So that activity, that comes more into this forking idea.
[2485.32 --> 2490.60]  On GitHub, you can do what's called forking a repository, which is you basically make a
[2490.60 --> 2493.24]  copy of it in your own space.
[2493.40 --> 2498.00]  So that way you can edit code and modify it and fix whatever bug you ran into, for instance.
[2498.94 --> 2504.26]  And you can use those forks as a way of seeing how many people are actively working on this
[2504.26 --> 2504.68]  project.
[2506.02 --> 2506.14]  Yeah.
[2506.26 --> 2511.92]  Also, sometimes what I'll do is go to a repo and, you know, if I'm considering actually
[2511.92 --> 2517.02]  integrating it into a project, actually look at like the commit history.
[2517.02 --> 2521.70]  So like when you are working on a piece of code and you make a change, there's a commit
[2521.70 --> 2522.42]  that happens.
[2522.62 --> 2529.34]  And, you know, if the last one that happened was in like 2014 or something, probably less
[2529.34 --> 2532.96]  likely that, you know, the code is actually getting updated.
[2533.14 --> 2535.50]  Although that's not always a bad thing, right?
[2535.50 --> 2539.80]  If it's a simple package that doesn't need updating, you know, maybe that's something
[2539.80 --> 2540.40]  different.
[2540.66 --> 2541.36]  But yeah.
[2541.54 --> 2545.18]  So I guess we're kind of coming to the end of our chat here.
[2545.18 --> 2549.86]  But I know you mentioned like Jupyter and Scikit-learn are really great projects.
[2550.00 --> 2554.52]  Are there any sort of other projects that you'd like to highlight as we kind of wrap
[2554.52 --> 2556.06]  up here that people might want to check out?
[2556.46 --> 2556.76]  Oh, yeah.
[2556.84 --> 2558.94]  There's I mean, it's there's too many to name.
[2559.20 --> 2564.38]  One other that I will talk about that we haven't gotten to mention yet is Facebook has a library
[2564.38 --> 2567.70]  called Profit, which is really good if you run into time series data.
[2567.70 --> 2573.90]  As it turns out, time series data has some odd particularities that often show up.
[2574.20 --> 2580.14]  And you can leverage a lot of people's knowledge who understand those those particularities
[2580.14 --> 2581.70]  very well by using this package.
[2581.82 --> 2584.98]  And I think that's another one of those great things about open source software is that
[2584.98 --> 2588.56]  it often embeds the knowledge of a large group of people.
[2588.56 --> 2591.20]  So I got one last question for you.
[2591.26 --> 2592.92]  I'd like to I'm just kind of curious.
[2593.02 --> 2598.02]  And I ask people this all the time is what choices in terms of, you know, what software,
[2598.20 --> 2603.50]  you know, obviously people are like TensorFlow versus PyTorch, you know, and others along
[2603.50 --> 2603.86]  the way.
[2604.08 --> 2608.90]  What kind of workflow and what tooling to support that have you chosen for your own personal
[2608.90 --> 2609.28]  workflow?
[2610.24 --> 2610.80]  Absolutely.
[2611.20 --> 2617.08]  When you're choosing between different implementations or different packages, my opinion is that the
[2617.08 --> 2623.44]  best thing to do is to make a prototype of something in both and make sure you understand
[2623.44 --> 2626.74]  what the benefits and disadvantages are of each one.
[2626.90 --> 2631.30]  If you can, like ship both to production, have them behind some feature flag or something,
[2631.66 --> 2635.40]  test them in some way and try to see which one matches your use case better.
[2636.20 --> 2636.64]  Awesome.
[2636.84 --> 2641.36]  Well, thank you for sharing a little bit of your workflow, sharing a little bit about like
[2641.36 --> 2643.44]  what what you're passionate about in open source.
[2643.56 --> 2645.18]  It's been really great to have you on the show.
[2645.18 --> 2649.66]  I know we've mentioned a lot of open source things in the past, but it's been really great
[2649.66 --> 2654.56]  to have someone kind of just share their perspective on open source and machine learning in general.
[2654.82 --> 2660.04]  And we hope you have a great time at all things open and, you know, hope that the talk goes
[2660.04 --> 2663.50]  well and you have have just an awesome experience there.
[2663.60 --> 2665.16]  Thank you for taking time to talk to us.
[2665.42 --> 2665.88]  Thanks a lot.
[2666.44 --> 2667.04]  Yeah, of course.
[2667.14 --> 2667.54]  Thank you.
[2667.66 --> 2668.82]  I'm so glad that you enjoyed it.
[2668.84 --> 2670.12]  And I had fun talking to y'all too.
[2670.22 --> 2670.82]  Thank you so much.
[2670.82 --> 2673.80]  All right.
[2673.84 --> 2676.48]  Thank you for tuning into this episode of Practical AI.
[2676.74 --> 2678.18]  If you enjoyed the show, do us a favor.
[2678.30 --> 2678.88]  Go on iTunes.
[2679.02 --> 2679.70]  Give us a rating.
[2680.00 --> 2681.82]  Go in your podcast app and favorite it.
[2681.94 --> 2684.64]  If you are on Twitter or social network, share a link with a friend.
[2684.72 --> 2685.40]  Whatever you got to do.
[2685.62 --> 2687.08]  Share the show with a friend if you enjoyed it.
[2687.38 --> 2690.04]  And bandwidth for ChangeLog is provided by Fastly.
[2690.16 --> 2691.60]  Learn more at Fastly.com.
[2691.78 --> 2694.98]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[2695.20 --> 2697.60]  Check them out at Rollbar.com slash ChangeLog.
[2697.60 --> 2700.42]  And we're hosted on Linode Cloud Servers.
[2700.74 --> 2702.38]  Head to Linode.com slash ChangeLog.
[2702.46 --> 2702.94]  Check them out.
[2703.00 --> 2703.84]  Support this show.
[2704.24 --> 2707.42]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2707.86 --> 2709.94]  The music is by Breakmaster Cylinder.
[2710.34 --> 2713.78]  And you can find more shows just like this at ChangeLog.com.
[2713.86 --> 2715.90]  When you go there, pop in your email address.
[2716.20 --> 2722.22]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2722.62 --> 2723.38]  Thanks for tuning in.
[2723.54 --> 2724.26]  We'll see you next week.
[2727.60 --> 2728.28]  We'll see you next week.
[2728.30 --> 2728.62]  потом
[2728.62 --> 2734.02]  We'll see you next week.
[2737.86 --> 2738.76]  Bye.
[2742.76 --> 2743.02]  Bye.
[2743.06 --> 2743.70]  Bye.
[2743.70 --> 2744.56]  Bye.
[2744.56 --> 2745.08]  Bye.
[2745.08 --> 2745.26]  Bye.
[2745.26 --> 2745.62]  Bye.
[2745.62 --> 2746.40]  Bye.
[2746.40 --> 2746.60]  Bye.
[2746.60 --> 2746.98]  Bye.
[2746.98 --> 2747.28]  Bye.
[2747.28 --> 2747.50]  Bye.
[2747.60 --> 2748.54]  Bye.
[2748.60 --> 2748.72]  Bye.
[2748.72 --> 2749.60]  Bye.
[2749.64 --> 2750.68]  Bye.
[2750.86 --> 2751.14]  Bye.
[2751.96 --> 2752.66]  Bye.
[2752.74 --> 2752.76]  Bye.
[2752.78 --> 2752.82]  Bye.
[2752.90 --> 2752.94]  Bye.
[2753.16 --> 2753.24]  Bye.
[2753.26 --> 2753.28]  Bye.
[2753.28 --> 2753.54]  Bye.
[2753.78 --> 2754.34]  Bye.
[2754.36 --> 2754.94]  Bye.
[2755.36 --> 2755.90]  Bye.
[2755.92 --> 2756.74]  Bye.
[2756.76 --> 2757.44]  Bye.
