[0.00 --> 4.52]  When people think about massive amounts of data, they just say, oh, I just want as many
[4.52 --> 5.46]  images as possible.
[5.58 --> 7.80]  There's a saying by my CBO that I love.
[7.98 --> 11.30]  He says, guys, what I want is not to have the most images.
[11.86 --> 16.26]  I want to actually train most effectively on the least amounts of images if I can do
[16.26 --> 16.42]  that.
[16.62 --> 17.42]  And how do you do that?
[17.46 --> 19.66]  By selecting the right cases for optimization.
[19.98 --> 25.40]  So in medicine in general, annotation costs are sky high because you need physicians for
[25.40 --> 25.58]  that.
[25.86 --> 27.46]  So you really want to pick your battles.
[27.46 --> 30.96]  And the case selection methodology, even before saying about the biggest, which is
[30.96 --> 33.76]  something that I'm proud of, but he's saying like, you shouldn't be proud of that.
[33.86 --> 38.48]  I would ideally want to have the smallest Sanitated Imaging Database, but the most effective one.
[38.58 --> 42.44]  So the case selection, how do you pick the right cases to optimize the learning performance
[42.44 --> 43.60]  as much as possible?
[45.88 --> 48.42]  Bandwidth for Change Log is provided by Fastly.
[48.72 --> 50.60]  Learn more at Fastly.com.
[50.84 --> 53.12]  Our feature flags are powered by LaunchDarkly.
[53.42 --> 55.20]  Check them out at LaunchDarkly.com.
[55.20 --> 57.30]  And we're hosted on Leno cloud servers.
[57.46 --> 61.20]  Get $100 in hosting credit at Leno.com slash Change Log.
[61.36 --> 66.66]  Hey friends, this episode of Practical AI is brought to you by Kodish, a podcast from the
[66.66 --> 71.16]  team at Heroku that explores code, technology, tools, tips, and developer life.
[71.26 --> 75.44]  There's tons of great conversations on the Kodish podcast, so I would encourage you to check
[75.44 --> 76.42]  it out and subscribe.
[76.72 --> 82.24]  But in particular, I wanted to bring to your attention two episodes, episode 98 and 99,
[82.24 --> 86.68]  where Julian Duque explores the ethical and technical sides of deepfakes.
[87.04 --> 91.60]  The rise of manipulated pictures and videos and other forms of computer-generated media
[91.60 --> 95.72]  are able to cause uncertainty and doubt in what we see and hear online.
[95.86 --> 99.90]  So how are we able to use these tools for good, if at all?
[100.20 --> 100.92]  Here's a sneak peek.
[100.92 --> 107.76]  Let's say we want to do a deepfake of my voice and we train the model and we have enough data
[107.76 --> 108.34]  and everything.
[109.42 --> 117.78]  This will be also able to imitate my accent, for example, like how I pronounce English and
[117.78 --> 119.84]  the strong pieces of my accent.
[120.32 --> 122.10]  Or is not there yet?
[122.10 --> 123.36]  It really depends.
[123.54 --> 129.14]  If there would be a person with similar accent on the input, then it would be fine.
[129.28 --> 130.52]  But it's kind of cheating.
[131.06 --> 135.34]  You can think it's cheating because we're reusing accent of a different person that's similar
[135.34 --> 136.04]  to your accent.
[136.42 --> 142.42]  But if it would be like an American native speaker or a British person with a British accent
[142.42 --> 150.20]  or like whatever other accent, then it will kind of be a mixture on the output.
[150.20 --> 154.34]  So we're not there yet in terms of converting accents.
[155.06 --> 159.74]  It's a little bit more difficult than we initially anticipated because when we started the company,
[159.86 --> 163.78]  we thought it would be, you know, we'll kind of solve it in a year or something.
[163.90 --> 168.24]  But then it turned out that, oh, no, we're here for much longer.
[169.74 --> 170.78]  Check these episodes out.
[170.96 --> 176.70]  Links are in the show notes to both episodes or head to heroku.com slash podcasts to listen
[176.70 --> 177.52]  and subscribe.
[177.52 --> 182.48]  Again, check the show notes for links or go to heroku.com slash podcasts.
[195.42 --> 200.54]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[200.88 --> 202.62]  productive, and accessible to everyone.
[202.62 --> 207.04]  This is where conversations around AI, machine learning, and data science happen.
[207.46 --> 211.48]  Join the community and Slack with us around various topics of the show at changeodg.com
[211.48 --> 213.40]  slash community and follow us on Twitter.
[213.52 --> 215.14]  We're at Practical AI FM.
[221.78 --> 224.64]  Welcome to another edition of Practical AI.
[224.98 --> 229.40]  We are the podcast that makes AI practical, productive, and accessible to everyone.
[229.40 --> 230.98]  My name is Chris Benson.
[231.30 --> 235.08]  I am a principal emerging technology strategist at Lockheed Martin.
[235.22 --> 236.12]  I can't say my own title.
[236.72 --> 241.18]  And unfortunately, Daniel Whitenack, my illustrious co-host, is not able to join today.
[241.58 --> 242.32]  We'll miss him.
[242.48 --> 248.44]  But I am pretty excited because we have an interesting show ahead with me today.
[248.66 --> 255.14]  I have Elid Wallach, who is CEO of ADOC, joining me today and looking forward to learning
[255.14 --> 256.98]  all about ADOC and that industry.
[257.22 --> 258.46]  Welcome to the show, Elid.
[258.46 --> 260.66]  Yeah, thank you, Chris, for having me.
[261.44 --> 266.24]  So I guess to get us started, if you would kind of let us know about yourself, who you
[266.24 --> 270.36]  are, how you got to the point where you're at, and a couple of moments when we know you
[270.36 --> 272.60]  a little bit better, I'll ask about your company.
[272.86 --> 276.66]  But looking forward to finding out kind of how you arrived where you're at right now
[276.66 --> 278.32]  before we actually get to the topic at hand.
[278.72 --> 279.02]  Yeah.
[279.26 --> 281.28]  So again, thanks for having me.
[281.82 --> 286.34]  And I'm really excited about this Practical AI podcast because I come from the AI world.
[286.34 --> 289.16]  So my background is, I'm an Israeli.
[289.48 --> 292.12]  So everybody in Israel, we also serve in the military.
[292.78 --> 298.82]  I've had the pleasure of being in what's considered the most elite technology unit at the Ministry
[298.82 --> 300.42]  of Defense, a unit called Tal Piot.
[301.18 --> 304.86]  And as part of that, I headed the AI at the Israeli Air Force.
[305.26 --> 305.64]  Okay.
[305.64 --> 311.24]  So no healthcare, no knowledge about CP imaging or x-ray.
[311.58 --> 316.16]  And to be honest, I didn't even know what's the difference when we started back in the day.
[316.32 --> 321.78]  But what we were really passionate about is utilizing the skills we learn, which is basically
[321.78 --> 327.68]  applying artificial intelligence to real operational problems, solving real world issues, to the
[327.68 --> 328.36]  healthcare space.
[328.36 --> 333.38]  So before you even dive on, you started with something so cool that I don't want to let
[333.38 --> 334.12]  that get by.
[334.62 --> 340.14]  So when you talk about that unit with the Israeli Defense Force, could you tell us whatever you
[340.14 --> 341.18]  can a little bit about that?
[341.22 --> 343.00]  Because I've just never had someone say that before.
[343.36 --> 343.96]  It intrigued me.
[344.00 --> 346.24]  And then I want to keep going with your own history.
[346.34 --> 350.24]  But you can't start with something like that without talking a little bit about what it does.
[350.86 --> 351.10]  Yeah.
[351.24 --> 353.08]  So I'll say what I can.
[353.30 --> 353.56]  Okay.
[353.86 --> 354.50]  Fair enough.
[354.50 --> 355.46]  Say what you can.
[355.58 --> 357.48]  And I get that there's a point where you can't.
[357.60 --> 358.98]  I work for a defense contractor.
[359.10 --> 359.82]  So I understand that.
[360.46 --> 364.26]  So I'll start with the grand vision of the Tapio program.
[364.84 --> 368.04]  So in Israeli, there was a big war called the Yom Kippur War.
[368.48 --> 370.70]  And Israel was technologically surprised.
[371.76 --> 373.60]  And that was the key.
[373.72 --> 379.62]  So Israel decided strategically, we need to always have the technology on top.
[379.62 --> 384.30]  And their idea was, let's take 18-year-olds, right, when people are in their prime time,
[384.48 --> 388.22]  and let's make them like the innovators of the Israeli Ministry of Defense.
[388.36 --> 393.10]  So let's take the brightest 30, 40 people every year, screen them very rigorously,
[393.66 --> 397.00]  and give them a lot of benefits, but allow them, I would say, to serve their country.
[397.50 --> 400.38]  So when I was 18-year-old, I was screened for that program.
[400.88 --> 405.20]  And as part of that, I had to sign up for a decade at the Ministry of Defense.
[405.38 --> 406.74]  That's a service you have to perform.
[406.74 --> 412.10]  But the benefit is that they basically teach you everything there is to know about the military.
[412.28 --> 416.34]  So we kind of visit all units, and they give you this very rigorous training in both technology
[416.34 --> 416.82]  and leadership.
[417.32 --> 420.62]  And then they catapult you to leadership positions across the Ministry of Defense.
[421.12 --> 426.40]  And I was very fortunate to be at the Air Force in a time where AI was just starting to
[426.40 --> 431.92]  pick up in terms of applications, you know, computer vision, NLP, and what can be that.
[431.92 --> 437.76]  And it was just so much fun to look at the academy and all the innovation and trying to apply
[437.76 --> 441.24]  them for, you know, real projects that, you know, help save lives.
[441.78 --> 442.16]  Sounds good.
[442.28 --> 442.48]  Okay.
[442.52 --> 445.50]  Thank you for at least kind of getting us going on that.
[445.58 --> 448.56]  That sounds like a pretty cool start, pretty cool way of getting into this.
[448.70 --> 452.66]  So pick up, now that I've rudely interrupted you, go ahead and pick up and tell us about
[452.66 --> 454.16]  yourself, you know, from that point.
[454.56 --> 454.76]  Yeah.
[454.76 --> 459.68]  So when I finished the service after 10 years, I've met my two co-founders, which were both
[459.68 --> 460.92]  part of that program as well.
[461.60 --> 464.72]  One headed the department for the special forces.
[464.98 --> 466.48]  One had been in kind of the Israeli NSA.
[467.10 --> 469.74]  And we were just very passionate about the healthcare space.
[469.92 --> 474.30]  We saw that there was this massive pain point with increasing amounts of data.
[474.66 --> 475.80]  We can talk more about that.
[475.90 --> 481.38]  But we're just, we needed to know how we can use the tools that we got through our service
[481.38 --> 483.08]  to build a company.
[483.08 --> 486.42]  And we're passionate about healthcare space basically for two big reasons.
[487.00 --> 491.00]  The first is that it's really a deep tech area, right?
[491.02 --> 494.30]  So we didn't want to compete in, you know, three guys in a garage, right?
[494.30 --> 498.12]  We wanted like to build something that is, you know, higher barriers, very defensible.
[498.58 --> 501.34]  And the other reason is more of an emotional one.
[501.42 --> 503.98]  We just wanted to feel that direct connection.
[504.12 --> 508.26]  I think there are a lot of companies bring value, but to be honest, I love the fact that,
[508.32 --> 512.26]  you know, once a day we get a text message from a physician that tells us, hey guys,
[512.26 --> 513.92]  you just self-save somebody's life.
[514.56 --> 518.06]  And I think that's what we were looking for when we started the journey all those years
[518.06 --> 518.36]  back.
[519.02 --> 519.06]  Okay.
[519.30 --> 523.94]  I guess if you could tell us a little bit about what it is in terms of the company that
[523.94 --> 528.32]  you've started, what the vision is for that, you know, where are you going, you know, at
[528.32 --> 528.92]  a high level?
[529.40 --> 530.04]  Tell me what you're doing.
[530.56 --> 530.76]  Yeah.
[530.76 --> 535.34]  So we are utilizing artificial intelligence for radiology.
[535.72 --> 540.22]  Radiology, for those that don't know, is the science and art of interpreting medical
[540.22 --> 542.62]  images, CTs, x-ray, MRIs.
[543.06 --> 547.50]  And in recent years, we've seen a massive overflow of information.
[548.18 --> 549.46]  You have cheaper scanners.
[549.88 --> 551.14]  You have higher resolution.
[551.46 --> 552.42]  You have less radiation.
[552.54 --> 553.40]  So you do this more and more.
[553.40 --> 558.96]  And the problem is that each and one of those images has to be interpreted by an expert
[558.96 --> 560.98]  physician called a radiologist.
[561.28 --> 561.38]  Yep.
[561.80 --> 566.08]  And unfortunately, they are stagnant and have been stagnant for you in terms of number of
[566.08 --> 566.58]  radiologists.
[566.94 --> 569.00]  And the situation today is almost absurd.
[569.82 --> 575.12]  Mayo Clinic did research showing that today they have about two seconds to read an image.
[575.58 --> 576.08]  Think about it.
[576.08 --> 578.50]  A human has to look at an image, massive image.
[578.62 --> 579.26]  We're talking big images.
[579.76 --> 581.60]  Two seconds to detect if something's wrong with you.
[581.70 --> 581.94]  Right.
[581.94 --> 583.74]  Obviously, it's an error-prone process.
[583.90 --> 584.96]  Obviously, it's very difficult.
[585.14 --> 586.96]  And obviously, we're starting to get delays.
[587.58 --> 591.84]  And because radiology is so critical to all of healthcare, you know, now you do, you know,
[591.90 --> 594.24]  even for stubbed toe, you get radiology, right?
[594.46 --> 598.00]  So every delay, every error has massive downstream implications.
[598.16 --> 602.14]  And we see it impacts, you know, stay and errors and patient lives at the end of the day.
[602.88 --> 605.70]  So, yeah, pause here and see if that makes sense.
[605.98 --> 606.82]  It does make sense.
[606.90 --> 607.98]  It makes perfect sense.
[607.98 --> 608.96]  And it's interesting.
[608.96 --> 614.72]  Without specifics, I have heard about AI being used to do radiology in terms of the interpretation.
[615.00 --> 617.14]  You said the one thing, though, that I'm just curious about.
[617.50 --> 620.34]  It's totally a side note, but I can't help but ask.
[620.72 --> 624.32]  You mentioned that the radiologist has, like, a couple of seconds to make that.
[624.80 --> 630.88]  And is it just too costly, you know, given that they're doing rounds and they have many patients or something to spend the time?
[630.88 --> 633.94]  But, you know, they're just expected to obviously see it quickly.
[634.10 --> 648.08]  But I'm just kind of curious what's driving the metric about how little time they have to make that, given the fact that that human in the loop right there, as they're looking at that image, has a huge downstream, you know, cost to getting it wrong.
[648.58 --> 651.48]  Is it just too few radiologists for too many patients in general?
[651.48 --> 651.92]  Exactly.
[652.92 --> 654.64]  It's kind of supply of demand of images.
[655.16 --> 659.30]  And another big factor that comes in is more data per image.
[659.96 --> 665.66]  So if images were small, so like a CT exam, in the past they had, you know, 50 images, something like that.
[665.94 --> 669.54]  But they were talking about thousands for a single patient, for a single exam.
[670.26 --> 672.42]  So that obviously factors in as well, right?
[672.62 --> 673.76]  I don't think I realized that.
[673.90 --> 674.82]  I just learned something.
[674.82 --> 679.58]  I was thinking, you know, when I'm in and they throw two or three up, you know, and all that.
[679.64 --> 682.64]  But they have a whole lot more than that to deal with today is what you're telling me.
[682.98 --> 683.10]  Yeah.
[683.18 --> 686.12]  The analogy I heard from one of our customers, I love that.
[686.44 --> 688.28]  It's like phone cameras, right?
[688.36 --> 691.16]  So first of all, you have much higher resolution, right?
[691.68 --> 694.54]  And you have all the different filters now and you need to look at all that.
[694.88 --> 697.44]  And the other thing, you know, everybody's doing imaging today.
[697.52 --> 699.08]  You know, you have selfies all around.
[699.32 --> 702.58]  So CT images are like, you know, are like phone cameras.
[702.58 --> 705.42]  Now everybody's doing selfies and now you have a lot more resolution.
[705.70 --> 705.72]  Gotcha.
[706.08 --> 708.66]  It sounds like a good problem to scale with automation.
[709.00 --> 710.60]  That's what I have to say about that.
[710.84 --> 711.10]  Yes.
[711.34 --> 711.70]  Yes.
[712.20 --> 713.04]  Or augmentation.
[713.20 --> 713.56]  Fair enough.
[713.68 --> 715.84]  So why don't you tell us a little bit about that augmentation?
[716.02 --> 718.72]  What is the business model that you're addressing here?
[719.06 --> 720.46]  How do you fit into that process?
[720.96 --> 725.56]  So basically, our AI is a safety net to radiologists.
[726.14 --> 727.72]  So the AI constantly runs in the background.
[728.32 --> 730.94]  Nobody needs to activate it or anything like that.
[730.94 --> 735.50]  And searches for certain type of findings that require prioritization.
[735.82 --> 741.26]  So the big problem we try to solve, or at least the area we started with, is critical care.
[741.40 --> 748.00]  Because you have so many patients and, you know, the big thing if you have more data and less people is that those patients can get treated much later.
[749.14 --> 752.02]  And our AI runs in the background and searches for those critical findings.
[752.24 --> 755.14]  Stroke, bleed, pulmonary embolism, spine fracture.
[755.14 --> 764.16]  And if we find something, we basically alert the whole care team, the radiologist, to the existence, to the presence of a critical finding.
[764.32 --> 767.18]  And this can shorten the time to treatment significantly.
[767.34 --> 771.54]  We're talking about, you know, even in ED settings where time is really fast.
[771.60 --> 772.64]  We're talking about an hour or two.
[772.64 --> 778.12]  But for elective care, it could be sometimes, you know, days of reduction in terms of time to treatment.
[778.66 --> 779.94]  So what does that look like?
[780.02 --> 781.92]  What is the relationship?
[782.74 --> 785.68]  So you're doing the interpretation at this point with the AI.
[786.12 --> 786.90]  What does that look like?
[787.14 --> 789.52]  We are basically flagging cases for the radiologist.
[789.66 --> 791.56]  Still, the human is doing their interpretation.
[791.56 --> 798.16]  We're just helping him screen through the data, see where areas the radiologist is focused on first.
[798.78 --> 802.72]  And let me give an example of what it means without us or with us.
[803.26 --> 807.36]  So let's say you have one example is the emergency department.
[807.70 --> 810.64]  So typical emergency department, especially at night, very busy.
[810.74 --> 812.08]  You have dozens of patients coming in.
[812.56 --> 815.14]  And you really don't know which of them are really critical or not.
[815.64 --> 819.60]  So we have a patient, let's say, fell down a few stairs, coming to the ED.
[819.60 --> 824.02]  They're even doing CT imaging for that patient, trying to see if that patient has a brain bleed.
[824.74 --> 831.78]  But unfortunately, today, just because of the overload, that patient could wait hours before anybody interprets the exam.
[831.98 --> 834.98]  That's the key bottleneck, looking at the exam and seeing if there's a bleed.
[835.42 --> 838.58]  So today, you could wait, you know, a couple of hours.
[839.00 --> 842.72]  And we're talking about very time-sensitive pathology, right?
[842.78 --> 844.96]  Time is brain, you know, we all heard that.
[844.96 --> 850.54]  So we can basically reduce that time because we say we look at the image.
[850.64 --> 852.64]  We say, hey, there is a brain bleed here.
[853.00 --> 854.16]  Let's alert the radiologist.
[854.24 --> 856.02]  You should definitely take a look at that patient.
[856.10 --> 859.44]  Even though that patient is 15 in your list, that should be number one.
[859.52 --> 863.48]  Take a look right now and get the patient the treatment they need.
[863.48 --> 870.76]  And it's interesting, just to throw in, as you're describing this, I have a very specific context that I'm applying it.
[870.76 --> 879.30]  I have a stepdaughter who is a fourth-year med school student, and she is right now working in an emergency room at a hospital near us.
[879.36 --> 880.70]  And that's what she does.
[880.96 --> 886.18]  And so she relays a lot of her experience, you know, because I have no background in that.
[886.36 --> 887.76]  She likes to tell me these things.
[887.82 --> 888.78]  So it's very interesting.
[888.78 --> 893.10]  I'm envisioning how this fits into her world, as she's been describing to me over time.
[893.44 --> 904.84]  And she has talked about the fact that getting the image results can be a big delay in the ER when they're trying to move quickly, especially on like a Saturday night or something when things are coming in at a very fast pace.
[905.34 --> 910.46]  So I guess you still have the radiologist directly involved in the process.
[910.70 --> 918.24]  Is it essentially just speeding up their process to draw their attention directly to what they need to focus on to speed that up?
[918.24 --> 918.92]  Exactly.
[919.42 --> 919.68]  Okay.
[919.96 --> 928.60]  But you're anticipating, at least at this point in time, the radiologist is always the key to the picture still along with the technology that you're providing.
[928.72 --> 930.34]  The two are partnered essentially.
[930.90 --> 931.26]  Exactly.
[931.58 --> 931.94]  Exactly.
[932.22 --> 935.16]  And I think that's key, especially in this day and age.
[935.36 --> 937.84]  And right now, I think radiologists have to be involved.
[939.06 --> 941.18]  It's A, because it's really necessary.
[941.18 --> 941.26]  Sorry.
[942.22 --> 947.46]  Because at the end of the day, I wouldn't want to have AI interpreting my full images.
[947.90 --> 949.70]  And, you know, I'll add one more thought to that.
[950.12 --> 951.18]  The AI is really good.
[951.40 --> 953.64]  I trained him to be the best brain bleed detector I can.
[953.90 --> 956.78]  But we have thousands of diseases that we can have.
[956.78 --> 962.18]  And where radiologists, where humans are really good at is that comprehensive picture, right?
[962.24 --> 963.80]  They know how to aggregate information.
[963.90 --> 965.00]  They know how to look to this.
[965.14 --> 966.44]  Something here looks wrong, right?
[966.48 --> 968.14]  That's where humans are very good at.
[968.72 --> 972.30]  So we're not replacing them in any way, shape, or form.
[972.38 --> 980.02]  We're just providing this augmentation so they could focus, you know, if there is a critical finding, you know, let's focus on that right away.
[980.02 --> 983.98]  Let's make sure that we treat the patient very fast for the downstream impact.
[994.98 --> 996.90]  We deserve a better internet.
[997.12 --> 1000.08]  And the Brave team has the recipe for bringing it to us.
[1000.24 --> 1001.22]  Start with Google Chrome.
[1001.46 --> 1005.16]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1005.38 --> 1006.24]  Rip out the Google bits.
[1006.36 --> 1007.02]  We don't need them.
[1007.02 --> 1009.90]  Mix in ad and tracker blocking by default.
[1010.16 --> 1012.86]  Quick access to the Tor network for true private browsing.
[1013.16 --> 1017.56]  And an opt-in reward system so you can get paid to view privacy-respecting ads.
[1017.76 --> 1021.50]  Then turn around and use those rewards to support your favorite web creators like us.
[1021.82 --> 1026.44]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1037.02 --> 1038.84]  Okay, so that's really fascinating.
[1039.16 --> 1046.32]  We've kind of talked about how your technology fits in to that, you know, in this case the ER with the radiologist having to interpret that.
[1046.56 --> 1052.94]  Before we dive into the technology side, could you dive us kind of specifically through the process?
[1052.94 --> 1056.16]  You know, maybe describe a little bit about the radiologist.
[1056.16 --> 1061.14]  You know, we've talked about the radiologist trying to interpret and having to do that very, very quickly.
[1061.40 --> 1064.82]  How is the radiologist actually interfacing with your technology?
[1064.98 --> 1066.86]  What does that feel like to the radiologist?
[1067.18 --> 1069.98]  And how does that change their process, if you could describe that?
[1070.30 --> 1074.82]  And then after that, I'd love to dive into the specifics of the AI, whatever you're willing to share,
[1074.96 --> 1079.64]  to understand some of the cool underlying models that you're using to make all this work.
[1079.64 --> 1082.24]  Yeah, so I'll start with an anecdote.
[1082.66 --> 1088.44]  When we started the company, we had a conversation with a radiologist, a very known neuroradiologist.
[1089.20 --> 1091.96]  And we talked with him about the workflow.
[1092.56 --> 1096.32]  And he told us like, guys, look, radiologists are so bombarded with information.
[1096.80 --> 1099.28]  You have so little screen in real estate.
[1100.06 --> 1104.32]  You know, you really can't make us press buttons and, you know, click things.
[1104.44 --> 1105.30]  It has to be seamless.
[1105.30 --> 1108.12]  So, you know, reflect back to it all.
[1108.24 --> 1109.28]  You know, I get it.
[1109.32 --> 1110.86]  So great, great insight.
[1111.02 --> 1114.02]  So no more than one button click for the use of the product.
[1114.22 --> 1116.04]  He told me, no, I don't think you've got it.
[1116.56 --> 1118.24]  No button clicks for the use of the product.
[1118.60 --> 1122.68]  It has to be fully seamless, automatically appear whenever I want it.
[1123.16 --> 1127.74]  And that was kind of the challenge we faced when we started a company because there really are, you know,
[1127.80 --> 1131.58]  imagine that environment of the person that has 50 patients waiting for a critical,
[1131.58 --> 1133.96]  like getting phone calls, having to triple out.
[1134.08 --> 1136.38]  You really can't disrupt anything.
[1137.02 --> 1141.60]  So what we wanted to create is a very seamless workflow to them.
[1141.90 --> 1144.10]  So it would appear automatically in their own systems.
[1144.16 --> 1145.10]  They're using a work list.
[1145.42 --> 1147.56]  So it would just appear as a flag in their work list.
[1147.72 --> 1149.48]  You know, just like a small pop-up.
[1149.60 --> 1151.92]  Things are really, you know, easy for them.
[1152.92 --> 1156.90]  The challenge was, however, you know, we thought, well, great idea.
[1156.90 --> 1162.34]  But the problem was that in healthcare, there are so many legacy systems, right?
[1162.42 --> 1166.26]  So imagine a hospital using systems, sometimes, you know, 10 years old systems.
[1166.78 --> 1171.16]  I noticed that every time I do have to go to, you know, doctor's office or hospital or something,
[1171.16 --> 1174.24]  it feels like a step back in time if you're into technology.
[1174.94 --> 1175.62]  Oh, exactly.
[1175.96 --> 1176.44]  Exactly.
[1176.92 --> 1181.06]  And trust me, it's really no fun to integrate into all of those legacy systems.
[1181.06 --> 1181.72]  I could imagine.
[1181.72 --> 1184.46]  So that's basically the challenge we had.
[1184.56 --> 1188.32]  And a big focus for the company is actually, you know, we're an AI company,
[1188.54 --> 1193.44]  but half of my engineering is on creating a very seamless workflow.
[1194.18 --> 1197.96]  And what we did, we basically created this very cool integration engine
[1197.96 --> 1201.30]  that allows us to integrate directly into those different systems.
[1201.80 --> 1203.70]  So whenever a radiologist gets up in the morning,
[1204.40 --> 1206.94]  he starts seeing our results popping up within their own workflow,
[1207.02 --> 1207.98]  the same system we're using.
[1207.98 --> 1211.26]  So if they were using a specific work list in a certain viewer,
[1211.72 --> 1216.64]  we'll just start popping up within their existing systems to kind of highlight the findings.
[1216.78 --> 1221.10]  So what they do is they just do whatever they were used to doing to this day.
[1221.20 --> 1222.82]  So opening a work list and then clicking,
[1222.96 --> 1225.82]  guess we're just small flag appearing there saying,
[1225.98 --> 1230.16]  hey, you know, this is a critical case, small, small, like priority flag.
[1230.56 --> 1231.16]  Look at that first.
[1231.46 --> 1232.50]  Very, very seamless.
[1233.02 --> 1233.74]  To accomplish that.
[1233.80 --> 1237.18]  So it sounds like you're integrating not only at a software level,
[1237.18 --> 1239.40]  but also at a hardware level to some degree.
[1240.00 --> 1241.60]  Or am I misunderstanding that?
[1241.86 --> 1245.84]  Because you have this hot new AI that you're trying to integrate with this 10,
[1246.00 --> 1249.00]  15 year old system that the doctors are used to using.
[1249.20 --> 1250.20]  How does that look?
[1250.26 --> 1250.84]  How does that merge?
[1251.04 --> 1252.78]  You're talking about kind of moving into the workflow,
[1252.90 --> 1254.14]  but how do you affect that?
[1254.68 --> 1254.96]  Exactly.
[1255.12 --> 1255.98]  So the key is,
[1255.98 --> 1256.32]  it is,
[1256.40 --> 1257.90]  it's still in the software level,
[1258.28 --> 1259.56]  but it's in a lower level.
[1259.72 --> 1259.96]  You know,
[1259.98 --> 1262.80]  you have to really understand the different communication protocols
[1262.80 --> 1264.50]  and how they communicate between the systems.
[1264.88 --> 1268.38]  And there are some patterns that emerge once you kind of get understanding that.
[1268.38 --> 1270.86]  But if you do it naively and just try to integrate,
[1271.00 --> 1271.08]  you know,
[1271.10 --> 1271.66]  vendor by vendor,
[1272.00 --> 1272.28]  you really,
[1272.44 --> 1272.56]  you know,
[1272.60 --> 1273.06]  you can't,
[1273.24 --> 1274.18]  it's just impossible.
[1274.34 --> 1279.94]  It's finding those ways that are very scalable and that work very well across all systems.
[1279.94 --> 1286.36]  So you're basically kind of using networking stacks and software to try to integrate as best you can with these older systems
[1286.36 --> 1289.14]  so that you get the most seamless workflow you can.
[1289.64 --> 1289.92]  Exactly.
[1289.92 --> 1292.92]  Even though you're talking about really old stuff blending with very,
[1293.02 --> 1297.68]  very new modern stuff to affect a user experience that's adding value to that.
[1297.68 --> 1300.02]  How does that change for the radiologist?
[1300.38 --> 1301.88]  They now have presumably,
[1302.30 --> 1302.50]  you know,
[1302.54 --> 1304.42]  they have the image that they would have looked at anyway.
[1305.20 --> 1310.44]  What are you doing in that workflow that changes it for the radiologist in terms of how they're,
[1310.70 --> 1311.80]  I'm using the word use case,
[1311.88 --> 1312.14]  I guess,
[1312.24 --> 1315.10]  but how their workflow seems from their perspective,
[1315.56 --> 1316.66]  what's different for them?
[1317.18 --> 1317.86]  From their perspective,
[1318.18 --> 1319.38]  it's almost unnoticeable,
[1319.46 --> 1319.92]  I would say.
[1320.18 --> 1321.52]  And that I think that's the beauty of it,
[1321.56 --> 1321.70]  right?
[1321.76 --> 1323.00]  Don't want to disrupt too much.
[1323.14 --> 1325.42]  We want to just create value in a seamless way.
[1325.42 --> 1329.26]  So we actually had a customer that they didn't even show the alerts.
[1329.52 --> 1329.86]  They,
[1329.88 --> 1333.42]  they configured that in a way that automatically updates their prioritization stuff.
[1333.72 --> 1337.32]  So they just use this as a feed and they decided just to change the prioritization.
[1337.44 --> 1338.40]  But typically for a customer,
[1338.54 --> 1339.42]  they get up in the morning,
[1339.84 --> 1340.06]  you know,
[1340.08 --> 1343.16]  they come to the regular work list where they have participations.
[1343.28 --> 1345.98]  They just see flags of our results.
[1346.58 --> 1348.72]  And if they hover on a flag,
[1348.92 --> 1349.28]  so they just,
[1349.42 --> 1350.36]  in their normal work list,
[1350.42 --> 1352.52]  they see like this orange ADOC icons.
[1352.82 --> 1352.92]  Yeah.
[1352.92 --> 1354.32]  And if they hover on that,
[1354.32 --> 1357.12]  we could have showed them a preview image of what the AI detected.
[1357.30 --> 1360.42]  And then they can basically choose that case.
[1361.26 --> 1362.26]  If they see the,
[1362.46 --> 1362.68]  you know,
[1362.74 --> 1363.90]  look at a preview image,
[1364.02 --> 1365.28]  looks like a prioritized case,
[1365.36 --> 1367.48]  then they open the case and then diagnose it.
[1368.02 --> 1368.12]  Gotcha.
[1368.68 --> 1371.14]  So to turn it a little bit away from the,
[1371.14 --> 1375.04]  the practitioner using it now and talking a little bit about the underlying technology,
[1375.04 --> 1379.30]  I suspect we have a lot of people in the audience that are just craving to hear about what kind of,
[1379.58 --> 1379.74]  you know,
[1379.74 --> 1382.32]  which models you use or their CNNs is their NLP.
[1382.32 --> 1383.92]  There's probably all of this.
[1384.02 --> 1384.42]  I'm guessing.
[1384.64 --> 1384.76]  Yeah.
[1384.80 --> 1390.58]  If you could take us through a little bit of kind of high level architecture about what you're using and why,
[1390.68 --> 1394.00]  and maybe some of the choices that you had to make along the way.
[1394.16 --> 1396.02]  I realize that you have trade secrets and stuff,
[1396.08 --> 1399.66]  but I'm hoping that you can tell us as much as you can without giving us,
[1400.04 --> 1401.54]  giving the secret sauce completely away.
[1401.54 --> 1403.68]  Maybe a tiny taste of secret sauce.
[1404.28 --> 1404.50]  Yeah.
[1404.94 --> 1408.94]  So the guiding principle for us was that,
[1409.02 --> 1409.46]  you know,
[1410.14 --> 1411.46]  theoretically AI,
[1411.98 --> 1413.86]  you could build any AI best in your,
[1413.94 --> 1416.84]  just any fully connected layer to detect whatever you want.
[1416.90 --> 1417.06]  Right.
[1417.40 --> 1417.70]  Sure.
[1417.70 --> 1420.84]  But that doesn't really work that way.
[1421.04 --> 1421.16]  You know,
[1421.20 --> 1422.40]  if you want to create effective system,
[1422.50 --> 1423.58]  you have to create a,
[1423.92 --> 1424.08]  you know,
[1424.14 --> 1429.36]  you have to steer the learning process in a way that it's most efficient to learning that specific domain.
[1429.74 --> 1437.28]  So the question we ask ourselves is how to train AI most effectively to solve the specific problems of medical imaging.
[1437.74 --> 1438.98]  And what are those?
[1439.08 --> 1441.10]  I'm just going to give a few examples,
[1441.10 --> 1443.44]  and then I can talk about what elements are we using.
[1443.44 --> 1448.76]  So the first issue that you get when you go to medical imaging is data scarcity.
[1449.54 --> 1450.90]  And it's not one of the,
[1450.98 --> 1451.12]  so,
[1451.24 --> 1451.46]  you know,
[1451.48 --> 1452.48]  you think about image net,
[1452.64 --> 1452.80]  you know,
[1452.84 --> 1454.74]  you think millions of images annotated,
[1454.88 --> 1455.50]  very easy.
[1455.66 --> 1455.78]  You know,
[1455.82 --> 1458.26]  you do a mechanical torque or something.
[1458.36 --> 1459.90]  You can outsource people flagging.
[1460.02 --> 1461.36]  It's not the same for ideology.
[1461.96 --> 1466.12]  We have what we believe is the biggest annotated database in the world right now.
[1466.32 --> 1466.38]  And,
[1466.46 --> 1469.68]  and we have hundreds of thousands of images like that.
[1469.80 --> 1470.38]  That's basically,
[1470.38 --> 1473.06]  we're talking about roughly order of magnitude of hundreds of thousands.
[1473.44 --> 1475.22]  A million of studies.
[1475.44 --> 1476.78]  Each contains hundreds of images,
[1476.92 --> 1477.04]  right?
[1477.10 --> 1479.94]  But so it's tens of millions of slices of images,
[1479.94 --> 1481.80]  but a lot of the imaging is 3D stacked.
[1481.86 --> 1484.06]  So you have one patient with 500 images.
[1484.70 --> 1488.08]  So that's one big challenge that we had to tackle.
[1488.50 --> 1490.96]  The second is class imbalance,
[1491.76 --> 1491.98]  right?
[1492.10 --> 1493.30]  So you have,
[1493.64 --> 1497.34]  look at the small patient image is like a million pixels,
[1497.46 --> 1498.12]  something like that.
[1498.12 --> 1498.62]  Um,
[1498.62 --> 1500.70]  and a disease can be on,
[1500.82 --> 1501.10]  you know,
[1501.38 --> 1502.48]  a three by three by three.
[1502.58 --> 1504.76]  We're talking eight pixels out of a million.
[1504.90 --> 1506.60]  And that's a positive example,
[1506.70 --> 1506.92]  right?
[1507.34 --> 1509.34]  If I'm talking air force lingo,
[1509.34 --> 1509.88]  I would say,
[1510.00 --> 1513.02]  so if I'm creating an algorithm to detect,
[1513.02 --> 1513.96]  you know,
[1514.04 --> 1514.56]  bunkers,
[1514.72 --> 1515.32]  it's like,
[1515.34 --> 1518.34]  it would give you map of the world and tell you,
[1518.40 --> 1518.46]  Hey,
[1518.48 --> 1519.46]  there's a bunker in here,
[1519.46 --> 1519.78]  right?
[1519.90 --> 1520.30]  Somewhere.
[1520.68 --> 1521.26]  Go and have fun.
[1521.26 --> 1524.74]  So it's really trying to handle this really class imbalance.
[1524.84 --> 1526.16]  We have all these normal areas.
[1526.48 --> 1527.76]  That's like a big utter challenge.
[1528.48 --> 1532.10]  And the third challenge for us was that humans have a lot more information.
[1532.54 --> 1535.54]  Oftentimes that the system is accessible to,
[1535.60 --> 1536.98]  and I'm talking about the clinical context.
[1537.32 --> 1538.14]  So radiologists,
[1538.24 --> 1542.66]  they cheat in the sense that they look at historical exam to look at patient data,
[1542.80 --> 1545.92]  and it helps them kind of focus on what they really want to do.
[1545.94 --> 1548.22]  And that's another thing that we really want to focus on.
[1548.22 --> 1552.70]  And those are just three examples of how we basically built the underlying
[1552.70 --> 1555.62]  architecture to support those,
[1555.62 --> 1556.54]  those pain points.
[1557.26 --> 1558.42]  So basically what we're using,
[1558.50 --> 1559.54]  it's not totally different.
[1559.68 --> 1562.54]  It's convolutional neural network on the medical imaging,
[1562.68 --> 1569.42]  but what we really innovated is on the training process to handle the class imbalance on,
[1569.52 --> 1575.40]  on some of the specific layers in the network to try and replicate as much as possible,
[1575.98 --> 1577.66]  how a physician would look at the image.
[1577.66 --> 1580.78]  And we added a lot of clinical information from other imaging,
[1580.94 --> 1581.96]  so from other sources,
[1582.12 --> 1583.18]  under clinical sources,
[1583.68 --> 1588.94]  for the neural network to have as much information as possible when doing it.
[1589.04 --> 1591.04]  So before I dive any deeper,
[1591.16 --> 1594.02]  I want to pause here and see if you have any questions on that.
[1594.36 --> 1595.38]  No, that's very interesting.
[1595.64 --> 1596.34]  I'm just curious,
[1596.56 --> 1600.50]  when you're looking at the world of CNN architectures out there,
[1600.68 --> 1604.02]  what are some of the architectures that you like in general?
[1604.08 --> 1606.30]  And I'm not asking how you're using them in specific ways,
[1606.30 --> 1607.92]  but what is interesting because,
[1608.38 --> 1609.30]  and I ask with a reason,
[1609.40 --> 1612.12]  Daniel and I often talk about the fact that a couple of years ago,
[1612.24 --> 1612.42]  you know,
[1612.46 --> 1614.48]  we were seeing all the evolution of CNNs,
[1614.52 --> 1617.66]  but we've heard more recently more about NLP and,
[1617.72 --> 1618.14]  you know,
[1618.20 --> 1619.90]  transformers over the last year or two.
[1619.90 --> 1623.76]  And if you're looking at it from our perspective as doing interviews,
[1623.76 --> 1626.94]  we're hearing more about this other side of AI.
[1627.34 --> 1631.08]  I love the fact that you're taking us back into the CNNs and we haven't really
[1631.08 --> 1633.70]  heard how they've evolved as much from guests lately.
[1634.10 --> 1635.64]  I love to find out like,
[1635.72 --> 1640.00]  what do you think is fantastic out there in the CNN world in terms of useful
[1640.00 --> 1640.50]  stuff?
[1640.60 --> 1643.00]  Are there things that you think of are old and you wouldn't,
[1643.06 --> 1644.38]  you wouldn't mess with them at this point,
[1644.38 --> 1647.16]  having used them a lot in the last couple of years,
[1647.22 --> 1648.62]  just wherever your perspective is.
[1649.02 --> 1649.26]  Yeah,
[1649.40 --> 1650.30]  it's a great question.
[1650.62 --> 1653.62]  And I would say that it's funny when,
[1653.76 --> 1653.94]  you know,
[1653.96 --> 1656.08]  when we submit to the FDA even,
[1656.30 --> 1658.54]  so every one of our products has to be clear about the FDA.
[1658.94 --> 1659.14]  Yep.
[1659.42 --> 1662.12]  They asked us what architectures we're using as well.
[1662.18 --> 1663.14]  So it's important to them.
[1663.14 --> 1664.98]  And I always found it kind of,
[1665.14 --> 1666.56]  it wouldn't say funny,
[1666.78 --> 1666.80]  but,
[1666.90 --> 1669.56]  but when we look at our domain,
[1669.70 --> 1670.68]  we typically don't just,
[1670.76 --> 1670.94]  you know,
[1671.00 --> 1672.82]  download architecture from the,
[1672.82 --> 1675.04]  you know,
[1675.04 --> 1675.86]  I'm not downloading,
[1675.86 --> 1676.12]  you know,
[1676.12 --> 1680.54]  and implementing as is we're taking elements and we're experimenting with
[1680.54 --> 1680.86]  them,
[1680.86 --> 1682.78]  but it's relatively like I knew,
[1682.84 --> 1685.84]  I can't say it's even similar to anything,
[1685.92 --> 1686.16]  you know,
[1686.20 --> 1689.40]  anything specific because it's just so adapted to our domain.
[1689.54 --> 1690.14]  You know,
[1690.20 --> 1691.14]  we have 3d data.
[1691.30 --> 1691.84]  We have the,
[1691.84 --> 1691.90]  the,
[1691.90 --> 1692.16]  the,
[1692.16 --> 1692.94]  the link information.
[1693.54 --> 1694.92]  We do love attention.
[1695.08 --> 1695.36]  That's,
[1695.44 --> 1697.44]  I think is a big one for us again,
[1697.44 --> 1699.20]  because of the class imbalance and all that.
[1699.28 --> 1699.66]  So that's,
[1699.72 --> 1700.50]  that's a big thing.
[1700.72 --> 1702.80]  And the other thing we really like,
[1702.82 --> 1703.50]  is a,
[1703.50 --> 1706.24]  is tile transfer networks for data augmentation.
[1706.24 --> 1709.70]  So anything around data augmentation for data scarce elements,
[1709.78 --> 1710.74]  I love those as well.
[1711.00 --> 1711.52]  So it's like,
[1711.56 --> 1714.92]  if I can pick like two elements that I love and we use often,
[1714.92 --> 1715.82]  I would say those,
[1716.26 --> 1717.92]  but it's really hard for me to say like,
[1717.98 --> 1719.20]  this is an architecture I would,
[1719.54 --> 1721.08]  I would just use because it's so,
[1721.18 --> 1721.72]  so different.
[1721.78 --> 1724.36]  It's like they pick a few elements and you really experiment a lot.
[1724.88 --> 1725.08]  Gotcha.
[1725.32 --> 1728.32]  And that was a great explanation for kind of how you're seeing that.
[1728.50 --> 1729.08]  I like that.
[1729.08 --> 1734.06]  It really sounds like you're finding the competitive advantage there in terms
[1734.06 --> 1738.22]  of customizing a number of different things in a way that's unique to your
[1738.22 --> 1741.02]  business and which you mentioned barriers to entry earlier.
[1741.02 --> 1743.60]  And I would imagine that creates substantial barriers to entry.
[1743.76 --> 1747.50]  You also talked about the world's largest annotated data set for this.
[1747.50 --> 1750.62]  Are you able to tell us kind of how you develop that,
[1750.68 --> 1751.52]  where that came from?
[1752.06 --> 1752.20]  You know,
[1752.24 --> 1755.42]  at what point did you see the need for that and how did you approach that?
[1755.76 --> 1758.92]  And you could take it from the perspective of there are other people in
[1758.92 --> 1762.10]  other industries and other businesses out there that are trying to figure out
[1762.10 --> 1763.34]  how to solve it for their business.
[1763.54 --> 1764.94]  They know that they need the data.
[1765.04 --> 1765.98]  They're not sure how to do it.
[1766.04 --> 1771.02]  I'd love to hear how you got to that point where you could affect the
[1771.02 --> 1772.82]  solution that you were striving for.
[1773.54 --> 1773.72]  Yeah,
[1773.80 --> 1774.44]  absolutely.
[1774.44 --> 1778.82]  I want to add one more point regarding the last point we discussed in terms
[1778.82 --> 1780.04]  of customizing the networks.
[1780.56 --> 1781.74]  There is a cost to it,
[1781.82 --> 1782.18]  by the way,
[1782.24 --> 1786.92]  I just want to make sure that I'm sharing that transparently and that if
[1786.92 --> 1788.02]  you are experimenting,
[1788.16 --> 1791.42]  you need to have a very flexible experimentation infrastructure.
[1792.04 --> 1795.46]  And we've actually invested a lot in developing our cloud experiment
[1795.46 --> 1796.42]  experimentation.
[1796.74 --> 1796.76]  And,
[1796.88 --> 1800.28]  but even like the small challenges of how do you run a thousand experiments a
[1800.28 --> 1802.18]  day and track those and,
[1802.18 --> 1805.42]  and you do it on spot instead and recover experiments if they fail.
[1805.42 --> 1808.66]  Like that was a massive undertaking right now.
[1808.72 --> 1812.10]  I believe we're in a much better spot than we were and we can run thousands of
[1812.10 --> 1812.96]  experiments every day,
[1813.10 --> 1814.42]  which is fun as hell,
[1814.48 --> 1814.64]  you know,
[1814.64 --> 1816.90]  just have an idea and go crazy with it.
[1817.32 --> 1818.32]  Even me as a CEO,
[1818.42 --> 1818.68]  I can,
[1818.74 --> 1818.88]  you know,
[1818.90 --> 1820.38]  just ask them to implement like some,
[1820.64 --> 1820.78]  Hey,
[1820.92 --> 1821.12]  you know,
[1821.14 --> 1822.04]  we didn't do ABC.
[1822.30 --> 1822.60]  Let's try,
[1823.10 --> 1823.92]  but it's massive.
[1823.92 --> 1828.16]  It's one of those challenges we don't often hear about is the engineering of
[1828.16 --> 1829.38]  doing very efficient,
[1829.58 --> 1830.66]  scalable experimentation.
[1831.10 --> 1831.98]  Regarding the annotation.
[1832.36 --> 1833.24]  So as you can imagine,
[1833.32 --> 1834.32]  a lot of it is secret sauce,
[1834.38 --> 1835.48]  but I'll try and get the,
[1835.48 --> 1837.16]  the high level elements.
[1837.62 --> 1838.76]  So I want to share two things.
[1839.04 --> 1842.50]  The first is that when people think about massive amounts of data,
[1842.64 --> 1843.36]  they just say,
[1843.66 --> 1843.80]  Oh,
[1843.82 --> 1845.74]  I just want as many images as possible.
[1846.46 --> 1848.94]  There's a saying by my CTO that I love.
[1848.94 --> 1849.34]  Uh,
[1849.34 --> 1850.14]  he says like,
[1850.54 --> 1850.80]  guys,
[1850.90 --> 1853.58]  what I want is not to have the most images.
[1853.76 --> 1857.66]  I want to actually train most effectively on the least amounts of images.
[1857.66 --> 1858.62]  If I can do that.
[1859.20 --> 1859.64]  So,
[1859.64 --> 1860.80]  and how do you do that?
[1860.80 --> 1863.12]  By selecting the rice cases for optimization.
[1863.42 --> 1864.66]  So in medicine,
[1864.66 --> 1865.46]  in general,
[1866.02 --> 1868.98]  annotation costs are sky high because you need physicians for that.
[1869.24 --> 1872.72]  So you really want to pick your battles and the case selection methodology,
[1872.72 --> 1874.14]  even before saying about the biggest,
[1874.30 --> 1875.12]  which is something that,
[1875.12 --> 1875.54]  you know,
[1875.72 --> 1876.30]  I'm proud of,
[1876.32 --> 1876.92]  but he's saying like,
[1876.94 --> 1877.84]  you shouldn't be proud of that.
[1877.84 --> 1878.92]  I would ideally,
[1878.94 --> 1881.56]  you want to have the smallest data data imaging database,
[1881.64 --> 1882.56]  but the most effective one.
[1882.86 --> 1883.68]  So the case selection,
[1883.80 --> 1885.62]  how do you pick the right cases,
[1885.76 --> 1888.16]  optimize the learning performance as much as possible?
[1888.64 --> 1889.18]  And again,
[1889.24 --> 1891.06]  let's take a brain bleed.
[1891.12 --> 1891.74]  I think it's a great,
[1891.82 --> 1892.36]  great example.
[1892.92 --> 1893.02]  Are,
[1893.18 --> 1896.68]  am I taking a thousand pictures of patients with massive brain bleed,
[1896.74 --> 1897.46]  which are obvious,
[1897.46 --> 1900.40]  or am I taking maybe the only 50,
[1900.76 --> 1904.44]  but those 50 are those with like subtle brain bleeds that you can really
[1904.44 --> 1906.26]  train and improve the system with.
[1906.36 --> 1908.40]  So I would tackle that challenge.
[1908.40 --> 1915.00]  If more than I would tackle the challenge of annotating very efficiently and
[1915.00 --> 1916.28]  regarding efficient annotation,
[1916.28 --> 1920.76]  I would just say that the key we found is having everything very tight.
[1920.76 --> 1923.58]  So as outsource as much as possible,
[1923.58 --> 1927.54]  that the connectivity between the data teams and the AI teams and the annotators,
[1927.54 --> 1930.64]  and like the fact that we control all the bits and pieces,
[1930.74 --> 1931.90]  the annotation selection,
[1932.06 --> 1932.38]  everything,
[1932.52 --> 1935.26]  like everyone knows their parts and they can communicate.
[1935.38 --> 1936.38]  That was very efficient.
[1936.38 --> 1938.90]  I heard about Google doing something for,
[1939.00 --> 1940.82]  I believe it was for a dermatology,
[1940.92 --> 1941.20]  yes,
[1941.38 --> 1942.00]  for eye images.
[1942.00 --> 1945.70]  And they have like a thousand page manual for their annotators.
[1946.24 --> 1946.40]  Okay.
[1946.80 --> 1949.28]  That for me is ineffective.
[1949.46 --> 1949.64]  Right.
[1949.68 --> 1951.52]  And the problem was the annotators were outsourced.
[1951.64 --> 1955.68]  So just like going through all the information and helping them inefficient.
[1955.68 --> 1959.16]  What we believe is key is having like very high interactivity,
[1959.30 --> 1960.20]  a lot of feedback teams,
[1960.32 --> 1960.86]  a lot of,
[1960.86 --> 1961.12]  you know,
[1961.20 --> 1961.62]  AI people,
[1961.72 --> 1963.06]  I want this and data people,
[1963.22 --> 1963.34]  Hey,
[1963.40 --> 1964.56]  this is tough for me to annotate.
[1964.64 --> 1965.52]  Do you really need that?
[1965.60 --> 1969.88]  And all of those small bits and pieces we find really help accelerate the process.
[1969.88 --> 1972.24]  And I won't talk too much about how exactly we solve it,
[1972.30 --> 1973.44]  but I would say that's,
[1973.56 --> 1974.30]  that's a big element.
[1974.30 --> 1985.10]  Have you heard about knowable?
[1985.28 --> 1988.94]  It is an awesome new platform for learning from the world's best minds.
[1988.94 --> 1989.50]  Anytime,
[1990.16 --> 1992.84]  anywhere at your own pace through audio,
[1993.24 --> 1998.56]  learn about the performance benefits of a plant-based lifestyle from NBA all-star Chris Paul,
[1998.96 --> 2002.64]  or how to launch a startup from Reddit co-founder Alexis Ohanian.
[2002.64 --> 2006.28]  There's even a 10 lesson course from astronaut Scott Kelly.
[2006.64 --> 2007.46]  Here's a sneak peek.
[2009.10 --> 2010.52]  We learned a lot up there,
[2010.80 --> 2013.10]  but what can you learn from a life in space?
[2013.82 --> 2015.30]  The answers might surprise you.
[2015.74 --> 2017.24]  In this knowable course,
[2017.24 --> 2020.38]  I want to share some of the things I've learned that you might not expect.
[2021.54 --> 2026.48]  Lessons about leadership on a dark night on an aircraft carrier in the middle of a churning sea.
[2027.46 --> 2032.56]  Lessons about the fear you feel with 7 million pounds of thrust exploding underneath you.
[2033.64 --> 2034.82]  And most of all,
[2035.26 --> 2037.84]  there's an idea out there that astronauts are always perfect.
[2038.70 --> 2039.78]  Failure is not an option,
[2040.02 --> 2040.22]  right?
[2040.92 --> 2046.18]  That's why I want to take you through some of my life experiences to show you how that's just not true.
[2047.04 --> 2048.28]  I believe everyday,
[2048.56 --> 2049.98]  regular human failure,
[2050.32 --> 2051.36]  if we handle it right,
[2051.72 --> 2054.32]  can be one of our greatest opportunities to learn,
[2054.64 --> 2054.90]  grow,
[2055.06 --> 2055.78]  and succeed.
[2055.78 --> 2059.50]  Knowable is accessible on your phone and on the web,
[2059.72 --> 2062.78]  and each audio course is broken out into individual lessons,
[2063.00 --> 2064.32]  usually around 15 minutes long.
[2064.70 --> 2065.90]  As a ChangeLog listener,
[2066.16 --> 2069.28]  you can get an annual membership to Knowable for 20% off.
[2069.68 --> 2073.22]  Get unlimited access to every Knowable audio course right now.
[2073.46 --> 2080.66]  Just download the Knowable app or visit knowable.fyi and use code CHANGELOG for that 20% discount.
[2080.66 --> 2083.82]  We put a link in your show notes for easy clickings.
[2084.02 --> 2088.74]  Check out Knowable today and start learning from hundreds of top experts from around the world.
[2089.00 --> 2089.46]  Once again,
[2089.56 --> 2090.92]  that's knowable.fyi,
[2091.30 --> 2091.98]  code CHANGELOG.
[2091.98 --> 2106.14]  So,
[2106.26 --> 2109.34]  you mentioned something a moment ago that I'd like to go back to,
[2109.48 --> 2109.98]  and that's,
[2110.06 --> 2113.14]  you talked about kind of the ability to do your experiments,
[2113.50 --> 2115.70]  you referenced your own workflow internally,
[2115.84 --> 2117.32]  the infrastructure that you had,
[2117.32 --> 2122.82]  and I'd really love to hear kind of how you've approached that,
[2122.88 --> 2123.28]  because,
[2123.40 --> 2123.86]  you know,
[2123.92 --> 2126.10]  people tend to talk about the AI.
[2126.36 --> 2126.44]  It's,
[2126.52 --> 2126.62]  you know,
[2126.64 --> 2128.30]  it's the sexy thing to talk about,
[2128.30 --> 2129.76]  and what you're doing,
[2129.76 --> 2135.00]  but they miss the fact that it has to fit into a larger software process
[2135.00 --> 2137.64]  that can take you all the way from experimentation,
[2138.30 --> 2139.70]  and figuring out where you're going,
[2139.82 --> 2142.10]  and then integration into your other software,
[2142.54 --> 2143.00]  that it has to,
[2143.08 --> 2143.18]  you know,
[2143.22 --> 2145.26]  because it's a model has to sit inside a larger,
[2145.26 --> 2148.44]  a larger set of components that are software,
[2148.44 --> 2152.22]  and eventually has to be deployed out to be usable in the real world.
[2152.80 --> 2152.98]  And,
[2153.02 --> 2154.70]  and so how have you approached that?
[2155.04 --> 2155.40]  You know,
[2155.50 --> 2159.32]  there are everything from cloud to buying your own equipment to being,
[2159.68 --> 2160.00]  you know,
[2160.10 --> 2161.32]  which workflow,
[2161.70 --> 2162.28]  which vendor,
[2162.42 --> 2163.82]  which open source you're choosing.
[2164.02 --> 2166.12]  How do you approach these challenges,
[2166.28 --> 2168.56]  these considerations that you have to make,
[2168.56 --> 2173.00]  considering that each one has a fairly substantial impact if you,
[2173.08 --> 2173.88]  if you don't get it right?
[2174.68 --> 2174.86]  Yeah.
[2175.26 --> 2179.82]  So I think the first big element that is important to note is team structure.
[2180.40 --> 2183.42]  I think that was actually the first consideration to take into account.
[2183.50 --> 2184.26]  And our head of AI,
[2184.44 --> 2184.66]  Idan,
[2185.26 --> 2186.68]  did an amazing job.
[2186.72 --> 2187.28]  He actually,
[2187.46 --> 2187.70]  you know,
[2187.76 --> 2188.64]  interviewed a few companies,
[2188.76 --> 2189.44]  how they build it,
[2189.50 --> 2189.66]  you know,
[2189.70 --> 2190.78]  how Google does it,
[2190.82 --> 2191.66]  how other people do it.
[2191.94 --> 2197.88]  And we figured out a structure where the AI algorithm engineers are actually a small part of the team.
[2197.88 --> 2199.44]  And we have,
[2200.16 --> 2202.44]  so I'll go through the evolution we had.
[2202.44 --> 2205.88]  So we started with having algorithm engineers just focus on algorithms,
[2205.88 --> 2207.38]  but they weren't really focused on,
[2207.38 --> 2209.54]  on deploying and anything like that.
[2210.04 --> 2211.70]  We then figured out that was a mistake.
[2211.78 --> 2218.96]  One people that can take the product end to end and take full ownership and not like do cross because things get left and it's really inefficient.
[2218.96 --> 2222.66]  So we brought people in that are both very sharp algorithmically,
[2222.78 --> 2222.92]  but,
[2223.02 --> 2223.26]  you know,
[2223.32 --> 2224.60]  know how to project manage,
[2224.68 --> 2225.38]  know how to deploy,
[2225.46 --> 2226.36]  know the software side,
[2226.42 --> 2226.98]  are not afraid,
[2227.04 --> 2227.22]  you know,
[2227.28 --> 2229.08]  to have their hands dirty with,
[2229.16 --> 2229.34]  you know,
[2229.36 --> 2229.90]  implementation.
[2230.62 --> 2232.50]  Then we kind of started figuring out way,
[2232.62 --> 2234.12]  but that's not also not very scalable.
[2234.12 --> 2236.30]  We need people that are even better at software and infrastructure.
[2236.58 --> 2241.76]  So we created like a whole AI infrastructure team with a ratio of about two to one.
[2242.22 --> 2245.46]  So two infrastructure folks for every one algorithm engineer,
[2245.66 --> 2247.62]  and then they started working on the infrastructure.
[2247.80 --> 2249.04]  And it's exactly the thing you mentioned.
[2249.12 --> 2250.56]  There are so many of those challenges.
[2251.68 --> 2252.46]  Do you scale?
[2252.66 --> 2253.30]  How do you scale?
[2253.40 --> 2254.72]  And this is the cloud and experimentation,
[2254.84 --> 2255.46]  experimentation,
[2255.72 --> 2258.24]  infrastructure and deployment infrastructure and monitoring infrastructure.
[2258.24 --> 2259.02]  Also very important.
[2259.10 --> 2261.34]  How do you monitor accuracy in production?
[2261.34 --> 2263.26]  And then,
[2263.34 --> 2264.10]  then we,
[2264.60 --> 2266.72]  I would say that's kind of how,
[2266.90 --> 2268.02]  how the team is built today.
[2268.02 --> 2269.62]  And we're scaling at it the same way.
[2270.30 --> 2272.28]  We were always big fans of the cloud.
[2272.70 --> 2273.94]  We started on-prem,
[2274.52 --> 2275.06]  which was,
[2275.28 --> 2275.68]  I would say,
[2275.76 --> 2278.04]  I don't know if it was a mistake back then.
[2278.10 --> 2279.34]  We didn't have as many experiments,
[2279.34 --> 2284.06]  but for now it's for sure we can do it on-prem because it's just so much
[2284.06 --> 2284.48]  experiment.
[2284.64 --> 2286.06]  So if you really want to scale fast,
[2286.60 --> 2287.88]  you really have to solve the cloud.
[2288.36 --> 2291.04]  And it's even like stupid quote unquote challenges.
[2291.04 --> 2295.04]  Like one of our challenges is that we ran out of spotting sensors for GPUs.
[2295.32 --> 2296.42]  That's a challenge apparently.
[2296.68 --> 2296.82]  And,
[2296.90 --> 2297.00]  you know,
[2297.04 --> 2300.70]  solving that and how do you like make sure that you work on multiple
[2300.70 --> 2306.00]  regions and how can you potentially transfer experiments between.
[2306.16 --> 2306.80]  So all of that,
[2307.18 --> 2309.58]  all the small things in making it tight.
[2309.98 --> 2312.50]  I think it just like respecting the engineering side,
[2312.60 --> 2313.32]  that was a big,
[2313.44 --> 2314.32]  big thing that I learned.
[2314.38 --> 2315.10]  Just make sure that,
[2315.18 --> 2315.42]  you know,
[2315.48 --> 2320.80]  that's probably a bigger part of making it work in practice versus like science.
[2320.80 --> 2321.24]  Gotcha.
[2321.72 --> 2323.46]  There's so many different ecosystems.
[2323.80 --> 2325.52]  Each of the cloud providers has their own ecosystem.
[2326.26 --> 2329.16]  NVIDIA with GPUs has their own ecosystem and workflow.
[2329.98 --> 2331.80]  There are a number of tools that,
[2332.02 --> 2333.90]  that are cross ecosystem in terms of,
[2333.98 --> 2334.12]  you know,
[2334.30 --> 2338.20]  like TensorFlow will work in all these different places as well as,
[2338.20 --> 2339.28]  as PyTorch and others.
[2339.28 --> 2342.18]  How do you buy in to,
[2342.28 --> 2344.98]  or how do you evaluate a particular ecosystem or,
[2345.12 --> 2347.68]  or a combination of them to make that bet,
[2347.84 --> 2349.04]  to go down that road?
[2349.16 --> 2349.88]  Any thoughts,
[2349.96 --> 2351.60]  any guidance that you can provide us on that?
[2351.80 --> 2352.12]  For sure.
[2352.20 --> 2352.70]  So first of all,
[2352.78 --> 2356.04]  we took the path of AWS and we're very happy with it.
[2356.22 --> 2356.38]  Sure.
[2356.38 --> 2360.76]  And the main reason we chose AWS was that it is in medicine,
[2360.88 --> 2362.18]  we say standard of care.
[2362.28 --> 2362.62]  So that's,
[2362.66 --> 2363.26]  I would say the,
[2363.34 --> 2365.42]  the leader probably at this point in time still.
[2365.78 --> 2367.96]  And that makes it very easy to hire,
[2368.04 --> 2368.24]  you know,
[2368.32 --> 2370.04]  DevOps people that know how to do it.
[2370.04 --> 2372.50]  Like all the new tools go on that platform.
[2372.50 --> 2374.76]  So that was for us a big consideration.
[2375.48 --> 2376.98]  And the other is just your cost.
[2377.22 --> 2377.82]  So when I,
[2378.08 --> 2378.20]  you know,
[2378.26 --> 2378.74]  when we pick,
[2378.82 --> 2379.82]  those are the two biggest ones,
[2380.00 --> 2381.98]  like innovation speed and,
[2381.98 --> 2382.60]  and cost.
[2382.60 --> 2384.16]  And can we create the architecture?
[2384.64 --> 2387.16]  The other big element in terms of consideration is,
[2387.26 --> 2392.14]  is who is available and can help you work through those challenges.
[2392.44 --> 2393.46]  So again,
[2393.46 --> 2397.36]  I think there are several companies that were really accessible,
[2397.36 --> 2399.50]  but we really enjoyed the interaction with AWS.
[2399.50 --> 2402.22]  We had all the technical research to help us think through the challenges.
[2402.96 --> 2403.50]  And I think what,
[2403.54 --> 2404.98]  what I learned as,
[2405.14 --> 2405.48]  you know,
[2405.58 --> 2407.22]  as someone that was technical,
[2407.22 --> 2408.84]  but not technical on the cloud side,
[2409.24 --> 2410.72]  I learned there are so many different elements,
[2410.88 --> 2412.50]  so many ways to create your architecture.
[2412.60 --> 2416.08]  Architecture that you really want to have a partner and can help you think
[2416.08 --> 2416.76]  through those challenges.
[2417.46 --> 2421.50]  So that was super cool about how you're trying to evaluate the software.
[2421.68 --> 2426.02]  I love hearing how people make those hard choices.
[2426.30 --> 2428.32]  And clearly you have a,
[2428.32 --> 2431.26]  a kind of an approach to how you're evaluating the,
[2431.36 --> 2434.26]  the possibilities out there that has worked very well for your organization.
[2434.84 --> 2436.36]  So that really,
[2436.46 --> 2437.68]  as we look forward,
[2437.94 --> 2438.28]  you know,
[2438.68 --> 2441.34]  there are so many things I want to ask you and kind of whatever,
[2441.34 --> 2443.16]  wherever your thoughts are taking you on this,
[2443.52 --> 2446.86]  we have the growing world of AI with all the tools on that.
[2447.12 --> 2454.10]  You're in an industry that we know is in the process of being revolutionized and probably in the very early stages of this technology.
[2454.10 --> 2457.28]  And there are so many choices that you have to make.
[2457.28 --> 2459.54]  And both as a leader of your organization,
[2459.54 --> 2469.02]  in terms of where you're taking the group and how to evaluate a really complex landscape of what AI is in the world that we're at and all the tooling.
[2469.02 --> 2471.06]  Where do you see the world going at this point?
[2471.24 --> 2471.42]  You know,
[2471.46 --> 2475.34]  if we're looking over the next few years in the relative short term,
[2475.34 --> 2479.38]  and maybe even farther when we're talking about where we might arrive and,
[2479.52 --> 2479.68]  you know,
[2479.76 --> 2482.28]  obviously nobody can read the future accurately,
[2482.28 --> 2486.62]  but I'd love to hear kind of where you think the world might be going down the road.
[2487.14 --> 2487.30]  Yeah,
[2487.38 --> 2489.46]  it's a fascinating topic and we have to,
[2489.62 --> 2491.82]  because we're in such a fast moving industry,
[2491.82 --> 2493.82]  we really have to think about it all the time.
[2494.24 --> 2498.40]  And I'll start with taking us back into the evolution of AI this past,
[2499.02 --> 2499.60]  two years,
[2499.66 --> 2502.68]  just to understand what are we even talking about and the speed.
[2503.76 --> 2509.16]  AI in healthcare and medicine has been in this frozen period for a few years.
[2509.30 --> 2511.00]  So if you would go three years back,
[2511.58 --> 2512.70]  not talking a decade,
[2512.88 --> 2513.56]  three years back,
[2514.26 --> 2515.70]  really not knowing,
[2515.96 --> 2517.16]  almost no big clearances,
[2517.72 --> 2517.98]  you know,
[2518.04 --> 2518.50]  one to deploy.
[2518.58 --> 2518.64]  I mean,
[2518.70 --> 2519.34]  two years back,
[2519.34 --> 2523.46]  we're talking about 0.01 market share of AI.
[2523.72 --> 2525.48]  Like we're talking two years ago.
[2525.70 --> 2526.66]  And to date,
[2526.66 --> 2527.20]  you know,
[2527.26 --> 2527.98]  only us,
[2527.98 --> 2530.74]  we have hundreds of hospitals and,
[2530.90 --> 2531.00]  you know,
[2531.06 --> 2531.96]  the leading names that,
[2532.18 --> 2532.30]  you know,
[2532.32 --> 2534.42]  you would know are already utilizing AI.
[2534.56 --> 2537.38]  So we're talking about massive adoption in two years.
[2538.14 --> 2538.54]  And,
[2538.62 --> 2538.96]  you know,
[2538.98 --> 2540.60]  thinking ahead for the next two years,
[2540.60 --> 2544.00]  I think we're going to see really probably everywhere.
[2544.94 --> 2546.60]  You're going to see one AI or another,
[2546.76 --> 2547.76]  which I find fascinating.
[2547.92 --> 2549.32]  I love being an industry that is so,
[2549.32 --> 2549.92]  you know,
[2550.00 --> 2550.46]  fast moving,
[2550.54 --> 2553.98]  kind of like we broke that barrier and then it's starting to evolve.
[2553.98 --> 2556.18]  But I think that right now,
[2556.26 --> 2560.78]  AI is in that really first age of,
[2560.78 --> 2561.82]  of healthcare AI.
[2562.18 --> 2564.68]  And AI today is doing,
[2564.98 --> 2566.60]  I would call it workflow augmentation.
[2567.24 --> 2570.76]  So AI right now is only helping to do humans where they either way would do,
[2570.84 --> 2571.20]  but better.
[2571.56 --> 2572.56]  So in my case,
[2572.62 --> 2574.08]  it helps radiologists detect,
[2574.14 --> 2574.48]  you know,
[2574.84 --> 2576.08]  pulmonary embolism faster.
[2576.42 --> 2576.60]  Okay.
[2576.60 --> 2577.04]  So that,
[2577.16 --> 2577.74]  that's the assistant.
[2578.40 --> 2580.38]  But if you ask me three,
[2580.54 --> 2581.50]  four years from now,
[2582.14 --> 2584.94]  it's going to start going into the predictive space.
[2586.22 --> 2587.50]  And what do we mean by that?
[2587.54 --> 2587.78]  I mean,
[2587.86 --> 2588.08]  look,
[2588.24 --> 2590.96]  seeing things that humans cannot see with their naked eye,
[2591.02 --> 2591.20]  right?
[2591.20 --> 2591.68]  So if,
[2591.74 --> 2593.96]  if today you can detect stroke at point a,
[2594.14 --> 2594.30]  you know,
[2594.38 --> 2594.66]  if AI,
[2594.76 --> 2596.50]  you could detect it in a minus two,
[2597.06 --> 2597.70]  Alzheimer,
[2597.98 --> 2598.62]  early detection,
[2598.70 --> 2599.60]  early detection of cancer.
[2599.76 --> 2604.00]  And I think that's where really the promise of AI becomes really exciting.
[2604.00 --> 2606.20]  Where you're creating new diagnostic capabilities.
[2606.60 --> 2607.24]  It's like,
[2607.48 --> 2611.56]  initially you need to do a CT to even look at the bodies and understand this
[2611.56 --> 2611.80]  state.
[2611.98 --> 2614.24]  Right now we're talking about the next phase of that seeing,
[2614.34 --> 2614.76]  you know,
[2614.82 --> 2616.62]  patterns that no one of us could predict.
[2617.04 --> 2620.36]  And I think that's the exciting next evolution for AI.
[2620.50 --> 2622.86]  I think it's very challenging for that.
[2622.92 --> 2624.24]  You need very high levels of trust.
[2624.50 --> 2626.72]  You need to have mountains of data.
[2626.82 --> 2629.38]  We're talking about origin mag more than there is today.
[2629.92 --> 2631.76]  But I think once you get that,
[2631.96 --> 2632.50]  that's going to be,
[2632.50 --> 2634.40]  that's the Holy grail we're all aiming for.
[2634.46 --> 2635.76]  And I think it's not that far away.
[2635.76 --> 2638.96]  We're talking three to four years where I'm going to start seeing things and
[2638.96 --> 2643.16]  really impacting in a way that is really impossible by humans today.
[2643.84 --> 2644.98]  That's really interesting to me.
[2645.14 --> 2645.76]  I'm 50.
[2645.96 --> 2646.26]  I don't,
[2646.26 --> 2649.28]  I don't mind telling people that I'm kind of getting to that point where I'm
[2649.28 --> 2652.46]  thinking as a guy who doesn't care much about medicine in terms of my own
[2652.46 --> 2653.54]  body so much,
[2653.56 --> 2654.62]  I'm just doing my thing,
[2654.70 --> 2655.36]  getting out there,
[2655.50 --> 2656.34]  exercising,
[2656.54 --> 2656.66]  but,
[2657.16 --> 2661.14]  and I'm starting to think now about who I'm at an age where this is
[2661.14 --> 2661.86]  starting to matter.
[2661.86 --> 2662.26]  Yeah.
[2662.38 --> 2667.30]  And so it's really good to hear that as I move farther into my fifties,
[2667.42 --> 2669.64]  that those kinds of new diagnostics are coming out.
[2669.64 --> 2670.18]  Cause I am,
[2670.26 --> 2671.98]  I'm counting on you to keep me healthy,
[2672.06 --> 2672.28]  buddy.
[2673.18 --> 2673.98]  So anyway,
[2673.98 --> 2675.18]  thank you very,
[2675.28 --> 2677.00]  very much for coming onto the show.
[2677.30 --> 2678.86]  It's been a fascinating conversation.
[2678.86 --> 2680.58]  And like I said,
[2680.64 --> 2684.82]  for my own selfish purpose in terms of keeping myself healthy and also,
[2684.82 --> 2685.30]  uh,
[2685.30 --> 2689.20]  in the perspective of hearing these ER stories and hearing how you're changing
[2689.20 --> 2692.70]  that whole picture and changing how fast people can get care.
[2692.86 --> 2695.58]  I appreciate your work and what your organization does.
[2695.58 --> 2697.14]  And thanks for coming on the show.
[2697.48 --> 2698.32]  Thank you so much.
[2702.02 --> 2704.34]  Thank you for listening to practical AI.
[2704.94 --> 2706.34]  If this is your first time,
[2706.46 --> 2708.60]  make sure you subscribe so you don't miss a thing.
[2709.02 --> 2714.08]  Head to practical AI.fm to subscribe or find us in Apple podcasts,
[2714.30 --> 2714.86]  Spotify,
[2715.14 --> 2716.80]  or wherever you listen to podcasts.
[2717.60 --> 2719.42]  And if you get value from the show,
[2719.56 --> 2721.74]  please do share it with a friend or a colleague.
[2721.90 --> 2723.30]  We appreciate you spreading the word.
[2724.12 --> 2727.02]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2727.30 --> 2728.78]  It's produced by Jared Santo.
[2729.00 --> 2731.14]  And our music is provided by Breakmaster Cylinder.
[2731.56 --> 2733.82]  We are brought to you by some awesome sponsors.
[2734.38 --> 2735.16]  Shout out to Fastly,
[2735.52 --> 2735.92]  Linode,
[2736.06 --> 2736.84]  and LaunchDarkly.
[2736.84 --> 2738.90]  That is our show.
[2739.08 --> 2740.02]  We hope you enjoyed it.
[2740.22 --> 2741.58]  And we'll talk to you again next week.
[2741.58 --> 2771.56]  Thank you.
