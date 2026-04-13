[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.32]  Learn how at Fly.io.
[40.42 --> 48.54]  You know, when we started podcasting back in 2009, an online store was just the furthest
[48.54 --> 49.56]  thing from our minds.
[49.90 --> 55.12]  Now we have merch.changelog.com, and you can go there right now and order some t-shirts,
[55.12 --> 56.86]  and that's all powered by Shopify.
[57.52 --> 58.96]  What did we do before Shopify?
[59.16 --> 60.22]  I'll tell you, we did nothing.
[60.36 --> 61.06]  We couldn't sell.
[61.34 --> 64.30]  There were other ways, of course, but they were very hard, very difficult.
[64.82 --> 70.60]  Shopify let us build out an entire front end, obviously branded like Change Log is.
[70.84 --> 71.74]  It's amazing.
[72.00 --> 73.66]  Merch.changelog.com.
[73.86 --> 78.58]  And our favorite feature is we use their API to generate a new coupon code, a personalized
[78.58 --> 84.30]  coupon code for every guest that comes on our podcast, and they get a free t-shirt from
[84.30 --> 85.30]  our merch store.
[85.54 --> 86.30]  And that's so cool.
[86.58 --> 87.70]  They choose the shirt they want.
[88.04 --> 89.22]  They use the coupon code.
[89.36 --> 91.16]  It arrives free of charge to them.
[91.36 --> 93.08]  And life is amazing.
[93.08 --> 99.90]  But also, you can go there right now to merch.changelog.com and buy some threads yourself.
[100.18 --> 101.00]  And that's awesome as well.
[101.36 --> 105.00]  So upgrade your business and get the same checkout we use with Shopify.
[105.54 --> 112.58]  Sign up for your $1 per month trial period at shopify.com slash practical AI, all lower
[112.58 --> 113.12]  case.
[113.46 --> 117.02]  Go to shopify.com slash practical AI to upgrade.
[117.20 --> 118.22]  You're selling today.
[118.22 --> 122.22]  Again, shopify.com slash practical AI.
[139.74 --> 143.72]  Welcome to another episode of the Practical AI podcast.
[144.20 --> 146.12]  My name is Daniel Whitenack.
[146.12 --> 152.18]  I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[152.18 --> 155.88]  a principal AI research engineer at Lockheed Martin.
[156.22 --> 156.86]  How are you doing, Chris?
[157.22 --> 158.58]  I'm doing very well today, Daniel.
[158.76 --> 160.08]  It's happy holidays.
[160.20 --> 160.96]  We're in that season.
[161.24 --> 166.68]  I happen to be recording outside, kind of looking at the birds around me and stuff and
[166.68 --> 168.44]  seeing them fluttering around the yard.
[169.26 --> 170.20]  That's amazing.
[170.70 --> 174.96]  Thinking about AI drones or something, probably.
[174.96 --> 176.50]  I can't stop that.
[178.02 --> 178.96]  That's great.
[179.70 --> 186.06]  Well, I'm super intrigued to have the conversation we're going to have today because I think people
[186.06 --> 193.12]  will find this super interesting and connecting on a variety of levels, both emotionally and
[193.12 --> 197.22]  technically, as is the topic that we'll be talking about.
[197.40 --> 202.02]  But we have with us Jeff Smith, who is founder and CEO at Chirp.
[202.46 --> 203.42]  How are you doing, Jeff?
[203.42 --> 204.46]  I'm great.
[204.64 --> 205.18]  Thank you.
[205.26 --> 207.54]  Thank you, Daniel and Chris, for having me on the show.
[207.78 --> 209.34]  Really appreciate being here.
[209.72 --> 211.16]  Yeah, it's great to make the connection.
[211.46 --> 213.40]  We have several mutual connections.
[213.70 --> 217.14]  So it's awesome to get connected through one of those.
[217.30 --> 219.66]  Shout out to Greg Enos if you're out there.
[220.02 --> 224.28]  Awesome connector in the Indianapolis area and good friend.
[224.28 --> 227.62]  Yeah, so Chirp, C-H-R-P.
[228.14 --> 228.94]  So no I.
[229.54 --> 235.66]  And I see when I look at your profile, Jeff, one of the things you kind of the call out
[235.66 --> 242.78]  categories that you have are AI, mental health and music, which all kind of come together
[242.78 --> 248.52]  in Chirp and are all super intriguing to me of how they come together.
[248.52 --> 254.48]  But I guess maybe start out by just helping us understand how these things intersected
[254.48 --> 255.62]  in your own life.
[256.16 --> 257.04]  No, I'd be glad to.
[257.68 --> 263.06]  As you mentioned, those three things, it is the perfect storm, especially for topics today.
[263.06 --> 266.26]  And it was a journey to get here.
[266.56 --> 271.78]  And I can give you a little bit about my journey and how we ended up with AI and mental health.
[272.22 --> 278.76]  I would say my background, I'm a corporate guy gone good, a classically trained entrepreneur.
[279.30 --> 281.32]  I built six companies, three nonprofits.
[282.06 --> 283.08]  It's where I find the joy.
[283.54 --> 287.82]  You know, identify a problem in the world, create a unique solution, wrap a company around
[287.82 --> 288.86]  it and build it to scale.
[288.86 --> 293.86]  And this one's called Chirp, named from the story of the canary in the coal mine.
[294.34 --> 296.38]  When that bird stops chirping, you get the heck out.
[297.34 --> 302.40]  It can send signals that we cannot, methane, carbon monoxide, and so it becomes an early
[302.40 --> 304.02]  indicator for health and wellness.
[304.88 --> 309.02]  And we've created a platform harnessing that and using music.
[309.90 --> 316.72]  And so to go even further back on myself and how I even got in this business, for years,
[316.72 --> 321.30]  I was the go-to guy for most ad agencies in New York to do all their social impact branding,
[321.46 --> 322.74]  corporate social responsibility.
[323.50 --> 328.64]  Became an expert on weaving purpose into the brand narrative and bringing people alive at
[328.64 --> 331.80]  work and through the products and the brands and these global campaigns.
[332.18 --> 338.02]  And along the way, found a significant disconnect, I would say, between the leadership, leadership
[338.02 --> 338.68]  that cares.
[338.82 --> 339.64]  They care about purpose.
[339.78 --> 340.70]  They care about their employees.
[341.26 --> 346.34]  They're throwing millions at perks, rewards, telehealth, but their employees aren't feeling it.
[346.34 --> 347.76]  You know, they're not feeling seen.
[347.84 --> 348.62]  They're not feeling heard.
[348.70 --> 349.84]  There's work-life enmeshment.
[349.96 --> 350.50]  They're depressed.
[350.62 --> 351.18]  They're anxious.
[351.32 --> 352.22]  They're looking for jobs.
[352.42 --> 355.06]  And so a few of us decided, hey, let's take that on.
[355.54 --> 360.60]  You know, we created a small company to come up with solutions to address workplace flourishing.
[361.32 --> 362.86]  And I thought, that'd be kind of cool.
[363.08 --> 364.74]  Let's bring people alive in the workplace.
[365.00 --> 369.58]  And we started there and said, hey, what's this disconnect between leadership and employees?
[370.16 --> 370.80]  What's the problem?
[370.84 --> 374.00]  If there's intent and there's resource, but not results, where's the breakdown?
[374.00 --> 376.22]  And we found that it was an information problem.
[376.60 --> 378.74]  We found it was the corporate survey, the quarterly pulse.
[378.80 --> 379.46]  How are you feeling?
[380.04 --> 380.98]  Nobody answers it.
[381.04 --> 383.76]  They lie in their responses, you know, fear of reprisal.
[383.96 --> 385.46]  And they're just making blind bets.
[385.76 --> 390.08]  You know, the data they're getting back is full, mainly because people hate surveys.
[390.52 --> 391.62]  You know, they want to fill them out.
[392.16 --> 393.04]  And so we said, let's start there.
[393.10 --> 398.54]  Let's come up with a better diagnostic tool so people can feel seen and heard and where they're
[398.54 --> 399.26]  truly at.
[399.26 --> 400.62]  And how do we do that?
[400.84 --> 405.62]  And we set out to improve the survey, the survey tool, different modalities, different
[405.62 --> 411.60]  lengths, maybe even the happy faces you see in the bathrooms at airports.
[412.06 --> 414.02]  You know, just make it super simple.
[414.58 --> 416.72]  And none of those are really tracking after a few months.
[416.90 --> 419.40]  And I was training for a Spartan race.
[419.76 --> 423.40]  You know, one of those crazy things that we do to keep ourselves alive.
[423.40 --> 425.96]  And I found my mood changing with my music.
[426.64 --> 431.12]  You know, I switched to, I think it was Motley Crue, Kickstart Your Heart, and just found
[431.12 --> 436.62]  my energy level shifting and started thinking as I was running, you know, what's happening
[436.62 --> 436.88]  here?
[436.98 --> 438.40]  Am I being affected by the music?
[438.54 --> 443.30]  Am I making certain choices in my music's lesson that's a reflection of this?
[443.50 --> 447.82]  And that was where I had the aha moment and say, hey, is music the signal that we've been
[447.82 --> 448.34]  looking for?
[448.34 --> 451.46]  Is that a reflection of how I feel?
[451.94 --> 456.26]  And so we dug into that, looked at music science, listening behaviors, research, AI, and found
[456.26 --> 459.88]  a direct link as music is a mirror for your mood.
[460.34 --> 465.04]  In the simplest form, Chris, if you're driving in the car and you're listening to the radio
[465.04 --> 468.76]  and you change, change, change until you find a song you like, that's just your mirror
[468.76 --> 470.64]  neurons lining up your emotion with that song.
[471.40 --> 473.90]  You know, it's how you're feeling or how you want to feel.
[474.12 --> 476.30]  It's very hard to listen to music you're not feeling.
[476.30 --> 478.34]  You know, it's that grind.
[479.22 --> 482.62]  And so we thought, okay, if we can bottle this up, we've got a rocket ship.
[482.92 --> 486.60]  If not, we'll sell the algorithm and, you know, move on to the next task.
[487.18 --> 492.54]  And so fast forward, raised a bunch of capital, surrounded myself with brilliant people, technologists,
[492.96 --> 494.92]  HR leaders, music.
[495.18 --> 499.58]  So a buddy of mine, Suman Debroi, we built some amazing things together.
[499.78 --> 503.58]  As a doctor in machine learning, he jumped in to help figure out the models.
[503.58 --> 508.26]  HR leaders from enterprise companies, managing hundreds of thousands of employees, speaking
[508.26 --> 511.60]  into what does that experience need to look like inside of the company.
[512.04 --> 516.94]  Music industry, songwriters, musicians, former execs from the big music streaming company
[516.94 --> 520.10]  saying, hey, this is the data that's available to you.
[520.24 --> 522.92]  Or even the intent from the musicians.
[523.10 --> 526.68]  And that was phenomenal to understand what did they, what were they feeling when they wrote
[526.68 --> 527.04]  a song?
[527.10 --> 528.68]  What did they want to put out in the world?
[528.68 --> 530.48]  And so that was fascinating.
[530.68 --> 535.60]  And then even the attorneys, legal counsel, you know, we've got the former privacy chief
[535.60 --> 539.34]  of Homeland Security, you know, really look at what are the privacy blockers?
[539.42 --> 541.78]  How do we hold integrity in this conversation?
[541.78 --> 543.96]  Because music is so personal.
[544.28 --> 546.90]  And so brought them together and said, hey, let's solve this problem.
[547.56 --> 548.44]  Music is our answer.
[548.44 --> 555.32]  And like any, I guess now a new tech company, you're testing it across an alpha group, looking
[555.32 --> 560.42]  at everything, adoption, you know, the science, end up with a black box on the table, works
[560.42 --> 560.86]  beautifully.
[561.10 --> 563.52]  And so that was like end of last year.
[563.66 --> 566.22]  Now you shift into product market fit.
[566.66 --> 568.08]  Who is this best built for?
[568.54 --> 568.84]  Right.
[568.92 --> 572.12]  A healthcare company at 2,500, a sports team, automotive company.
[572.12 --> 577.30]  So that's, that's where the, um, I'd say the rubber hits the road and where we're at today
[577.30 --> 580.04]  and just, um, incredible leaders.
[580.04 --> 583.22]  Like you mentioned, Greg Nienis and others just looking at this saying, Hey, here's a
[583.22 --> 583.68]  direction.
[584.10 --> 586.24]  Let's really look at that, how we can apply it.
[586.94 --> 592.18]  I got a, I got a question or so for you, but for listeners, they can go to Jeff's LinkedIn
[592.18 --> 593.02]  profile.
[593.02 --> 598.42]  And I believe that's you, uh, in a, in one of these Spartan races, if I'm based on what
[598.42 --> 598.86]  you said.
[598.86 --> 602.50]  That is, that might've been the one, um, that it all goes back to.
[602.62 --> 607.60]  And that's a picture of my now nine-year-old, um, that we're holding as you get the medal.
[607.82 --> 612.46]  But, uh, it's those fun races, you're bloody muddy and it's a great body hates you, but
[612.46 --> 613.26]  you love doing it.
[613.78 --> 619.14]  As you came up with this hypothesis and in those early stages, you're socializing the
[619.14 --> 624.26]  notion around and kind of explaining that, what kinds of different reactions did you get
[624.26 --> 626.34]  from people and how were they different?
[626.34 --> 632.10]  And I'm curious if there were any reactions people gave you to your idea as you were just
[632.10 --> 637.50]  getting started that surprised you in a positive or negative way, either one, you know, how
[637.50 --> 640.04]  did people take it in and process it themselves?
[640.72 --> 644.58]  I would say the initial reaction is the eyebrows go up and they lean in.
[644.80 --> 645.98]  Music is ubiquitous.
[646.20 --> 647.52]  It's, it's all around us.
[647.54 --> 648.44]  It's, it's amazing.
[648.72 --> 650.32]  Um, and it touches our lives.
[650.32 --> 653.22]  And so you have this emotional currency that we all get.
[653.34 --> 655.46]  So they lean in and say, that's amazing.
[655.84 --> 660.42]  And then they'll kind of sit back and say, Ooh, what does my music say about me?
[660.94 --> 665.02]  You know, if I'm listening to nine inch nails, does that mean I'm depressed or, you know,
[665.02 --> 666.82]  what, what's going on here in my heart?
[667.04 --> 671.26]  And, um, and then it's, so they go through that and then they lean forward again and say,
[671.26 --> 672.36]  Oh, this is amazing.
[672.54 --> 675.04]  You know, how do I incorporate this in my life, in my profession?
[675.42 --> 680.84]  And I would say the surprise or the unique things that came out of those conversations
[680.84 --> 683.02]  is really these tributaries that were created.
[683.18 --> 687.68]  So we built, you know, we built the tech, you patented, you applied to a sector that
[687.68 --> 693.48]  you understand of influence in, has a large enough, uh, addressable market, good liquidity.
[693.84 --> 697.56]  There's a budget item for engagement measurement, you know, if you apply it in there,
[697.98 --> 700.46]  I didn't expect then where this would take us, right?
[700.46 --> 704.12]  It's you, we've got mental health professionals saying, Hey, we wanted the screening tool to
[704.12 --> 709.96]  get ahead of certain things in, in our clinics, as well as creating a profit center for them.
[710.06 --> 713.60]  We have athletes and sports psychologists looking at it for performance.
[713.60 --> 719.54]  We have the U S military, um, needing to address suicide rates and say, Hey, if we could just
[719.54 --> 724.12]  know more about how they're doing, it's all about that early detection, early indicator on
[724.12 --> 724.84]  how they're doing.
[724.94 --> 727.24]  And again, I want to stress it's a screening tool.
[727.32 --> 729.68]  It's not a diagnostic or an assessment tool.
[729.68 --> 735.20]  So inside of therapy clinics, you know, it'll just get them to that BDI or GAD, you know,
[735.20 --> 737.96]  the, the formal assessments quicker, which is kind of cool.
[737.96 --> 743.12]  And so, um, I think that was the biggest surprise for me is I've launched a lot of companies and
[743.12 --> 746.52]  it's around the innovation or the relationships or the opportunity.
[746.82 --> 749.20]  This one was just, I use the word ubiquitous.
[749.28 --> 752.54]  It just, it's emotional, it's primal, it's historic.
[752.54 --> 753.96]  It's just in people's lives.
[754.16 --> 759.10]  You know, you look at the, we come to learn that, um, average person listens to 22 hours
[759.10 --> 761.88]  of music a week, you know, that just, it's all around us.
[761.88 --> 763.10]  And so that's just really cool.
[763.10 --> 765.86]  So I would say that was, uh, that was a big surprise.
[766.32 --> 771.88]  And by the way, uh, I just want to say nine inch nails still rocks after all these, I just
[771.88 --> 772.84]  got to say that before.
[772.84 --> 775.38]  I know Daniel has a question, but I had to say that.
[775.88 --> 777.06]  Yeah, fair enough.
[777.34 --> 782.92]  Um, and of course we're going to get into kind of the, the AI intersection here, which I I'm
[782.92 --> 786.84]  sure is sort of how some of the, these insights are, are developed.
[786.84 --> 791.38]  Maybe before that though, one of the things that I'm thinking about, and maybe you were
[791.38 --> 796.00]  starting to get into this as you were kind of mentioning the different types of scenarios,
[796.00 --> 802.80]  like in, in sports or in various verticals or, or therapy contexts or whatever that
[802.80 --> 808.84]  is, one of the things on my mind is like, there's a whole variety of ways that music
[808.84 --> 814.52]  is adopted in, in a person's daily life in particular at, at work.
[814.52 --> 821.16]  Like I am, I am imagining my wife's, uh, you know, candle manufacturing company, there's
[821.16 --> 825.14]  safety issues if everybody has, you know, noise canceling headphones on.
[825.44 --> 825.58]  Right.
[825.68 --> 828.80]  But they have music playing in the environment, right.
[828.80 --> 830.20]  That everyone can listen to.
[830.20 --> 836.16]  And then there's, you know, I imagine the, the programmer with his, you know, Bose headphones
[836.16 --> 842.56]  on just like grinding away, listening to whatever, almost, you know, all day, maybe in an environment
[842.56 --> 844.06]  where he's in a home office.
[844.06 --> 844.40]  Right.
[844.56 --> 850.26]  So as you've kind of delved into this and, you know, we will get to kind of the, the AI
[850.26 --> 856.90]  stuff, but how does that influence your, your approach, I guess, or your, your thought
[856.90 --> 860.20]  on kind of the, the value that can be added here?
[860.20 --> 864.70]  Cause I could imagine certain employers being all, well, what music do I play in this common
[864.70 --> 866.44]  environment or even in a retail setting?
[866.44 --> 872.64]  Like what music makes people want to buy things or in that more intimate setting, the music
[872.64 --> 874.38]  that I'm listening to all day.
[874.60 --> 880.86]  What, what does that signal about kind of things that I need to be understanding and need people
[880.86 --> 882.80]  to kind of know and see about me?
[883.26 --> 885.94]  Well, as you said, we can dive deeper into the mechanics.
[887.32 --> 893.02]  But more of a use case, just kind of share that this is a passive pulling technique that
[893.02 --> 895.06]  taps into your current music streaming.
[895.66 --> 898.90]  So it's not during the work that it could be if you're listening to it, but it's also in
[898.90 --> 900.48]  your commute and when you're at home.
[900.74 --> 904.30]  And, and so it was men, we wanted to design something that didn't change your behavior,
[904.30 --> 910.30]  but just kind of tapped into it and, and then take that data and then analyze it and everything
[910.30 --> 910.94]  from there.
[910.94 --> 915.80]  And so it's an opt-in technique based on their current, you know, music listening habits.
[916.56 --> 917.94]  And so it's interesting you bring that up.
[918.00 --> 922.10]  I mean, working with architectural design firm, landscapers, I didn't realize they listen
[922.10 --> 923.70]  to music under the big headphones.
[923.94 --> 930.10]  So for them, great all day long or manufacturing, but we can sense and analyze the data just on
[930.10 --> 934.66]  your relationship to music and I can get into how that differs and so on.
[935.30 --> 939.90]  But it's a lot of learning for us right now too, which has been, which has been exciting.
[940.04 --> 944.50]  People's approach to music, what it not only says about them, means about them, but just
[944.50 --> 950.66]  over time that you bring up about retail and there are some of those areas that we have
[950.66 --> 954.96]  intentionally said, let's hold up on, you know, let's first just master the science.
[955.28 --> 957.64]  Let's make sure that is high integrity.
[957.64 --> 963.32]  It is human centric and we take care of people and it is for their wellbeing and flourishing.
[964.16 --> 967.94]  You know, there, we have had a few folks saying, yeah, but if we can help sell another sweater
[967.94 --> 970.22]  by changing up the music, maybe.
[970.50 --> 974.72]  But you know, at the end of the day, um, that would be data that is completely stripped of
[974.72 --> 976.66]  any personal information and all that.
[976.80 --> 982.88]  So I think over time there are all sorts of use cases and we just have that true north as
[982.88 --> 989.06]  far as how is this truly improving lives, um, and improving lives is, um, improving businesses
[989.06 --> 992.36]  and they are more profitable and sustainable and everything else.
[992.36 --> 996.78]  And so, uh, there may be a place for that, but, uh, yeah, I don't know if that, that helps.
[996.78 --> 1012.68]  What's up friends?
[1012.84 --> 1014.48]  I love my eight sleep.
[1014.58 --> 1015.00]  Check them out.
[1015.12 --> 1016.36]  Eight sleep.com.
[1016.46 --> 1018.16]  I've never slept better.
[1018.30 --> 1020.10]  And you know, I love biohacking.
[1020.22 --> 1021.74]  I love sleep science.
[1021.74 --> 1028.44]  And this is all about sleep science mixed with AI to keep you at your best while you sleep.
[1028.88 --> 1032.32]  This technology is pushing the boundaries of what's possible in our bedrooms.
[1032.90 --> 1036.50]  Let me tell you about eight sleep and their cutting edge pod for ultra.
[1036.76 --> 1038.96]  So what exactly is the pod?
[1039.12 --> 1046.14]  Imagine a high tech mattress cover that you can easily add to any bed, but this isn't just
[1046.14 --> 1047.02]  any cover.
[1047.02 --> 1052.68]  It's packed with sensors, heating and cooling elements, and it's all controlled by sophisticated
[1052.68 --> 1053.94]  AI algorithms.
[1054.58 --> 1060.26]  It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into
[1060.26 --> 1061.26]  one single device.
[1061.82 --> 1067.62]  And the pod uses a network of sensors to track a wide array of biometrics while you sleep.
[1067.86 --> 1072.82]  It tracks sleep stages, heart rate variability, respiratory rate, temperature, and more.
[1072.82 --> 1074.66]  And the really cool part is this.
[1074.84 --> 1078.34]  It does all this without you having to wear any devices.
[1078.94 --> 1083.60]  The accuracy of this thing rivals what you would get in a professional sleep lab.
[1084.02 --> 1085.88]  Now, let me tell you about my personal favorite thing.
[1086.06 --> 1086.92]  Autopilot recap.
[1087.12 --> 1091.82]  Every day, my eight sleep tells me what my autopilot did for me to help me sleep better
[1091.82 --> 1092.26]  at night.
[1092.58 --> 1093.50]  Here's what it said last night.
[1093.96 --> 1097.82]  Last night, autopilot made adjustments to boost your REM sleep by 62%.
[1098.46 --> 1099.30]  Wow.
[1099.80 --> 1100.60]  62%.
[1100.60 --> 1107.22]  That means that it updated and changed my temperature to cool, to warm, and helped me
[1107.22 --> 1112.18]  fine tune exactly where I wanted to be with precision temperature control to get to that
[1112.18 --> 1113.92]  maximum REM sleep.
[1114.34 --> 1118.12]  And sleep is the most important function we do every single day.
[1118.42 --> 1121.52]  As you can probably tell, I'm a massive fan of my eight sleep, and I think you should
[1121.52 --> 1121.90]  get one.
[1121.90 --> 1129.46]  So go to eightsleep.com slash changelog and use our code changelog, and you'll get $350 off
[1129.46 --> 1132.28]  your very own pod for ultra.
[1132.60 --> 1134.92]  You can try it free for 30 days, but I am confident.
[1135.08 --> 1136.40]  I sleep on this thing every night.
[1136.64 --> 1138.86]  I'm confident you will not want to return it.
[1139.00 --> 1139.46]  Trust me.
[1139.70 --> 1145.62]  Once you experience this AI optimized sleep, you'll wonder how you ever slept without it.
[1145.74 --> 1146.28]  How do I know?
[1146.50 --> 1148.00]  Because that's exactly how I feel.
[1148.00 --> 1152.34]  They're currently shipping to the US, Canada, United Kingdom, Europe, and Australia.
[1152.88 --> 1159.56]  Once again, eightsleep.com slash changelog and use our code changelog and get $350 off
[1159.56 --> 1161.34]  your very own pod for ultra.
[1161.34 --> 1187.16]  Well, Jeff, we are starting to get into this around the kind of mechanics of this.
[1187.16 --> 1194.34]  And I don't think we have to drill into all of this, all the details and the implementation,
[1194.82 --> 1199.66]  but it would be interesting, like some of the things on my mind, and I'll be vulnerable
[1199.66 --> 1206.00]  in this context and reveal some of my music habits over even the past few days.
[1206.00 --> 1213.12]  Well, so I think yesterday when I was trying to get something done at work, I was streaming
[1213.12 --> 1216.96]  Gregorian chants, which is normally my go-to.
[1217.78 --> 1221.46]  I'm not going to be distracted while I work with lyrics.
[1221.78 --> 1223.48]  I just want something in there.
[1224.16 --> 1230.96]  I think as I was driving in the evening, I was listening to Mastodon, Leviathan, and maybe
[1230.96 --> 1235.62]  I don't know what that reveals about my post-work feelings.
[1235.98 --> 1237.96]  Maybe you would have that interpretation.
[1237.96 --> 1242.08]  And then I think like in other cases, I'm listening to...
[1243.08 --> 1246.54]  I love old-time Appalachian fiddle music.
[1246.82 --> 1248.64]  So that's kind of my general go-to.
[1249.32 --> 1250.96]  And so there's a lot of variety there.
[1251.12 --> 1254.72]  And so one of the things on my mind is, well, if I'm thinking about...
[1254.72 --> 1260.08]  Let's say you just gave me the songs that were played in my playlist or your playlist
[1260.08 --> 1266.90]  over the past however long, and the behavior related to that, it does seem like a tall...
[1266.90 --> 1270.92]  I mean, there's a connection there to maybe well-being, how I'm feeling.
[1270.92 --> 1276.04]  But the connection is difficult for me to think about as a human because there's such variety
[1276.04 --> 1277.38]  that you would experience.
[1277.60 --> 1284.60]  So I'm wondering, maybe even before what you've developed now, what were some of those challenges
[1284.60 --> 1290.86]  or surprises as you actually thought about the technical scope of this and what was and
[1290.86 --> 1291.70]  wasn't possible?
[1292.06 --> 1298.48]  Well, I think music is very personal, and how you approach Gregorian chants is different
[1298.48 --> 1299.46]  than how I do.
[1300.16 --> 1307.24]  And what we designed was a system that's looking for how you approach music and creates a baseline.
[1307.38 --> 1311.30]  You're looking for deviation, and I can kind of go into all of that, but it gets to know
[1311.30 --> 1311.78]  you over time.
[1311.86 --> 1316.60]  Creating that persona is that, okay, you're making certain choices in your music selections
[1316.60 --> 1318.66]  that are unique to you.
[1319.02 --> 1321.70]  So you've got all this incredible data coming through.
[1323.12 --> 1328.36]  It's danceability, it's lyrics, chord progression, balance, happiness, beats per minute.
[1328.44 --> 1330.74]  I mean, there's all this raw data that's coming in.
[1330.86 --> 1335.34]  And if in a vacuum, you're looking at that saying, okay, well, this is my mirror neurons lining
[1335.34 --> 1335.52]  up.
[1335.58 --> 1336.00]  I get it.
[1336.02 --> 1336.78]  This is how I'm feeling.
[1336.86 --> 1337.78]  So I'm choosing that.
[1338.10 --> 1340.40]  Then you look at certain choices you're making.
[1340.40 --> 1341.82]  I'm fast-forwarding through this song.
[1341.90 --> 1342.58]  I'm skipping this.
[1342.64 --> 1343.62]  I'm adding this to the playlist.
[1343.84 --> 1344.82]  I'm playing this again.
[1345.14 --> 1347.94]  My beats are going up in the afternoon because I'm working out.
[1348.00 --> 1353.42]  And there's all of this usage data that then you're looking at in comparison to that.
[1353.52 --> 1354.90]  And then it looks at it over time.
[1355.70 --> 1359.00]  And so what you're looking for is, great, here's your baseline, and you're trending.
[1359.16 --> 1361.18]  Now, all of a sudden, you're deviating in a certain direction.
[1361.66 --> 1363.04]  And so what does that mean?
[1363.04 --> 1368.64]  And so I'd say that one of the surprises, I think you asked that, in our discovery was,
[1369.10 --> 1374.38]  although music is incredibly personal and individualized, majority of people still get
[1374.38 --> 1376.74]  hit the same way with the same song.
[1377.20 --> 1380.26]  Like you get 60% of people listening to the song Happy Will Feel Happy.
[1380.40 --> 1381.84]  I mean, it's just something like that.
[1381.88 --> 1386.56]  And then you'll get that extra 20%, 30% accuracy because of your individualizing it.
[1386.56 --> 1390.90]  But I thought that was really cool that we could screen a majority of population against
[1390.90 --> 1393.56]  a certain album genre, songs.
[1394.52 --> 1395.54]  So that was one surprise.
[1395.68 --> 1400.16]  And the other was the flip it around and how the music industry starts supporting us saying,
[1400.28 --> 1401.00]  oh, this is interesting.
[1401.14 --> 1405.64]  Can we use your algorithm to write songs to achieve the emotion that the brands want to
[1405.64 --> 1407.32]  accomplish in these commercials or these movies?
[1407.78 --> 1410.46]  I thought, okay, that's a whole different line of work.
[1410.62 --> 1415.62]  And so I think it's fun to explore that, the individualization, understanding how we're
[1415.62 --> 1420.76]  addressing that through AI and everything, but also surprised by these other opportunities
[1420.76 --> 1421.86]  for the masses.
[1422.46 --> 1426.62]  I'm wondering if you can, just to kind of make it tangible, because this is fascinating
[1426.62 --> 1427.92]  what you're talking about here.
[1428.38 --> 1433.76]  If they're extending what Daniel was talking about, one day I might be working and listening
[1433.76 --> 1436.78]  to Queen Greatest Hits and doing that.
[1437.32 --> 1442.78]  And on another day, and God, I hope the audience doesn't beat me up on this, but I might be listening
[1442.78 --> 1445.46]  to musicals in the background.
[1445.66 --> 1446.80]  And there are things that I already know.
[1446.88 --> 1450.42]  I already have the lyrics down, so I can kind of ignore that and just appreciate it.
[1450.76 --> 1455.38]  What kind of insights, with those being two very different genres, but maybe for the same
[1455.38 --> 1459.16]  activity, I'm just curious, do you have any examples of what's like an outcome?
[1459.60 --> 1459.90]  Yeah.
[1460.12 --> 1460.24]  Yeah.
[1460.24 --> 1465.08]  Like, do you have any examples of like some of the things that you've learned about that
[1465.08 --> 1466.66]  or how, at least how you look at it?
[1466.66 --> 1472.24]  I'm just trying to, I'm trying to kind of ground the, you know, that into some kind
[1472.24 --> 1475.20]  of reality that you've discovered through this research.
[1475.62 --> 1476.48]  It's fascinating.
[1476.76 --> 1477.46]  So let me do two things.
[1477.54 --> 1479.96]  I'll take you through the use case.
[1480.22 --> 1484.76]  And so I'm not cherry picking certain data points and addressing it.
[1484.80 --> 1489.38]  But I mean, the short answer on your question is it depends on your baseline, repeated listening,
[1490.34 --> 1493.92]  tilt your mood in a direction, you know, based on certain behavior you're doing.
[1493.92 --> 1499.04]  So I would say short answer is it depends and I can kind of walk you through how it works
[1499.04 --> 1502.08]  and then it'll be fun to get your response on it.
[1502.42 --> 1507.14]  And then of course, I mean, that can go into the AI and what, you know, let's start high
[1507.14 --> 1507.46]  level.
[1507.70 --> 1507.80]  Sure.
[1508.28 --> 1515.24]  Music like AI, artificial intelligence, it's limited inputs, exponential outputs.
[1515.94 --> 1517.90]  You know, if you look at a music, there are 12 notes.
[1518.18 --> 1522.78]  You've got seven letters, you got major minors, but in the end you got 12 notes and that gives
[1522.78 --> 1524.68]  you everything from Mozart to Megadeth.
[1525.14 --> 1526.50]  You know, then you look at music behavior.
[1526.66 --> 1526.86]  Okay.
[1526.90 --> 1530.86]  People on average, like I said, listening to so much music, but then they're, how they're
[1530.86 --> 1534.30]  doing it, when they're listening to it, their playlist, repeat and everything else.
[1534.36 --> 1535.62]  And so all that data is there.
[1536.10 --> 1542.06]  And we built the engine to capture that and then AI to analyze, interpret, decode for well-being.
[1542.06 --> 1547.26]  And if you look at, I guess on the AI side, you've got the traditional to discern the mood
[1547.26 --> 1551.20]  of the user from the acoustic features, a lot of what I described from the songs and
[1551.20 --> 1553.06]  then generative to customize messaging.
[1553.22 --> 1554.46]  And so what that output is.
[1554.52 --> 1560.38]  But if you look at a experience inside of a company, a use case, so you're an employee
[1560.38 --> 1562.22]  at a company, you get an email from HR.
[1562.36 --> 1565.50]  Hey, we partner with these rock and rollers of corporate wellness, care about your personal
[1565.50 --> 1566.12]  wellness journey.
[1566.32 --> 1570.70]  Opt in with your Spotify, Apple, YouTube, get free perks along the way.
[1570.70 --> 1571.72]  Learn more about yourself.
[1571.86 --> 1573.12]  All data is anonymized.
[1573.66 --> 1577.06]  We're looking for trends on how to better serve you, your job and your wellness.
[1577.70 --> 1581.76]  And so, like I said before, we wanted to tap into their current music listening, not create
[1581.76 --> 1584.88]  another app they had to download, but it's just say, hey, this is the behavior.
[1584.98 --> 1590.18]  This is how you're listening to, I think you said, Gregorian chants and what's going on
[1590.18 --> 1590.60]  in the background.
[1590.86 --> 1593.72]  And so what happens is when that user opts in, there are two paths.
[1594.10 --> 1598.14]  One's for the organization and the data is anonymized, clustered.
[1598.56 --> 1599.58]  They're looking for trends.
[1599.58 --> 1604.36]  This way, an executive leadership team can look at dashboards, report outs, company level,
[1604.46 --> 1605.94]  department, division, down to team.
[1606.28 --> 1609.68]  You don't want to get to the individual to avoid any liability of selection.
[1609.94 --> 1612.66]  Hey, Johnny and HR is listening to Kid Rock and you got fired.
[1613.14 --> 1618.38]  You want to avoid the one-to-one, but they want a better solution for insights that are
[1618.38 --> 1618.96]  one-to-mint.
[1619.32 --> 1624.40]  And then you have bespoke recommendations for how to actually intervene or serve those teams.
[1624.48 --> 1628.50]  On the individual side, they're offering more intel about their emotional buoyancy.
[1628.50 --> 1632.96]  After a few weeks, they get a weekly email encouraging them to check out their e-score.
[1633.56 --> 1636.34]  So think of a whoop band for mental health, your sleep score.
[1636.72 --> 1638.16]  What does that data point on you?
[1638.20 --> 1639.18]  What does it say about you?
[1639.30 --> 1642.00]  Because your interaction in music is unique.
[1642.40 --> 1645.44]  And they love that because it's a data point in their life and well-being.
[1645.44 --> 1649.88]  And then we throw in that little added perk because we do want them to feel seen and heard.
[1649.98 --> 1652.66]  Hey, looks like you're feeling a little melancholy this week.
[1652.74 --> 1654.82]  Here's a pre-dark roast, your favorite coffee spot.
[1655.32 --> 1657.90]  You know, it's a, you know, how do you actually take that data?
[1658.32 --> 1661.90]  Not only to be self-aware, but given tools for self-regulation and everything.
[1661.90 --> 1669.32]  And so when you look at that model, it's very personal, yet anonymized on the organization side.
[1669.50 --> 1673.04]  And so we've always had that tension to make sure we have a strong firewall.
[1673.22 --> 1677.88]  But then as we work with them and as they listen more and more, it just gets smarter, smarter, smarter.
[1678.18 --> 1678.98]  It's fascinating.
[1678.98 --> 1688.20]  So to answer your question, I personally don't know, you know, if you were listening to Taylor Swift this afternoon and then the Wiggles in the morning, how you're feeling.
[1688.28 --> 1694.20]  But I could tell you by running through a trip for a few weeks, you will see a mirror of your emotion, which is fascinating.
[1695.24 --> 1698.12]  How long does it take to kind of form that baseline?
[1698.24 --> 1704.62]  You mentioned a few weeks, like how much is needed for that kind of cold start of, you know, problem?
[1704.62 --> 1710.32]  Or maybe is there more as more people use the system, there's less of that cold start problem?
[1710.44 --> 1712.18]  Or I don't know how that works.
[1712.52 --> 1721.02]  Well, again, as more people listen, we get more data and you're seeing the trends that are part of that natural grouping of the song data.
[1721.54 --> 1725.26]  But you still want to refine it, refine it for that personal answer.
[1725.44 --> 1731.46]  And so we say three to four weeks, it's closer to two, but everybody listens to different amount of music.
[1731.46 --> 1736.90]  So we say the average is 20 some hours, but this week you might be four hours or eight hours.
[1737.08 --> 1740.68]  And so how much data is being ingested is important.
[1741.22 --> 1744.68]  And then also it pulls in podcasts and audio books.
[1744.86 --> 1746.54]  And so that helps with contextual markers.
[1747.16 --> 1751.90]  You know, you might be driving more melancholy, but you're reading a lot about grief, you know.
[1751.92 --> 1755.44]  And so what are the things along the way that can just make the engine even smarter?
[1755.44 --> 1767.54]  I'm curious, and you started to answer that a little bit, but when you mentioned, you know, podcasts and, and, you know, books on audio and that kind of thing, which I do a lot of both of those in addition to music.
[1767.94 --> 1773.86]  Have you, is there any kind of contextual difference with people in that?
[1773.86 --> 1778.12]  I mean, like, and, and how do you account for natural mixes that people have?
[1778.20 --> 1783.34]  Like my mix is probably somewhat different in some ways from Daniel's mix, from your mix.
[1783.64 --> 1792.82]  How do, how do those different types of things that are coming into your experience change, you know, how you, how you evaluate someone in that way?
[1793.12 --> 1797.14]  You know, the podcasts and audio books, I use them as contextual markers.
[1797.28 --> 1798.42]  I'd say they're, they're additive.
[1798.42 --> 1803.36]  They're not nearly as accurate as music and music choices, but they tell a lot.
[1803.80 --> 1809.72]  And, you know, there are so many attributes that we pull in these acoustic features that you have tons of data.
[1810.02 --> 1818.74]  And I can talk about how that's churned on the podcast, audio book side, you have transcriptions, you can listen, you know, but they, they deviate a lot.
[1818.74 --> 1822.88]  And so you can look at certain choices that people are making, Hey, I'm going to listen to this.
[1823.20 --> 1824.00]  I'm going to read this book.
[1824.08 --> 1824.20]  Okay.
[1824.20 --> 1826.02]  I'm halfway done with this, but I switched to this other book.
[1826.26 --> 1835.20]  So you look at behaviors are not as I'd say accurate to really know a point in time, how somebody is doing, but you put that into the mix with their music.
[1835.20 --> 1837.78]  And now you start to see a really colorful picture.
[1837.78 --> 1840.84]  Maybe you could touch briefly on this.
[1840.94 --> 1852.86]  You alluded to it earlier in terms of your, the way in which you're going about this technology towards kind of human flourishing and wellness, because this is one of those things.
[1852.86 --> 1859.98]  And I'm sure listeners out there thinking about this, you know, you can think about really good uses of facial recognition, right?
[1859.98 --> 1864.04]  Or even the technology that is used in deep fakes, right?
[1864.04 --> 1871.62]  You can also think about really harmful usage of that or, or manipulative uses of, of that technology.
[1871.84 --> 1878.50]  And I think, you know, this scenario, I love how you've talked about it with that kind of standpoint from the very beginning.
[1878.68 --> 1884.86]  And you've even kind of mentioned some of these things, Hey, let's hold off in this area for a while or other things.
[1884.86 --> 1887.58]  How have you kind of come to grips with that?
[1887.58 --> 1894.42]  And how have you thought about that kind of trustworthiness and care for the users within what you're building?
[1894.42 --> 1908.80]  Well, I think it's incredibly important to keep the human at the center of it, you know, and just look at the integrity of the data, look at the integrity of the communications, you know, how we're really working with them, treating with them.
[1908.88 --> 1909.64]  What are they seeing?
[1909.72 --> 1916.76]  Even in the E score, we couldn't say that, Hey, you're a 85 and I'm a 75, because that might make me feel like I'm not optimized, you know?
[1916.76 --> 1918.54]  And so what are all the little things?
[1918.54 --> 1924.10]  And we even have some of the team that developed the aura ring and, you know, the visuals there to, to look at it.
[1924.44 --> 1935.10]  I would just say, I mean, we are a purpose built company, you know, we are all capitalists, but our true north goes a lot deeper in our purpose, our faith and we're in how we're driven.
[1935.10 --> 1946.98]  And so from our standpoint, seeing this as a tool for human flourishing, I think it's just, is super important and sacred matching with how sacred and epic music is, you know, it's, it's just historic.
[1947.06 --> 1947.88]  It speaks to our soul.
[1947.96 --> 1948.68]  It goes so deep.
[1948.68 --> 1951.60]  And so we want to make sure we steward that well.
[1951.82 --> 1961.68]  Now in this process, you've got all the, all the baggage, all the, the red flags, the landmines you have to look for, you know, inside of companies, it is privacy.
[1961.68 --> 1964.48]  It is, you know, data integrity and security.
[1964.48 --> 1968.16]  And you look at the user experience and the rate of adoption and then the whole way.
[1968.20 --> 1970.56]  And if you stick to that true north, you're going to get there.
[1970.62 --> 1971.44]  You're going to get the numbers.
[1971.54 --> 1972.68]  You're going to get people participating.
[1972.68 --> 1975.50]  The moment that you violate that, you've lost them.
[1975.88 --> 1980.82]  And that's just not something we're willing to do as a company, as a team and, and where we're headed.
[1980.98 --> 1985.50]  And so it's just been fascinating to see that for us, that's normal.
[1985.60 --> 1992.68]  Even how we built the company, it's say, we want to do life with people we love and, you know, at the investor level and the clients and everything.
[1992.90 --> 1997.34]  And, and what we're finding inside of companies is trust is so important.
[1997.82 --> 2002.40]  We've turned away some C-suite that have come to us saying, Hey, we want you to bring this in and fix our culture.
[2002.68 --> 2003.88]  Because our culture sucks.
[2004.24 --> 2009.16]  And then you realize it's because they do, you know, it's just, they just want to get more out of the apple.
[2009.16 --> 2013.42]  And so we want to work with companies that care about their people.
[2014.10 --> 2014.30]  Yes.
[2014.68 --> 2017.02]  Retention is important and productivity is important.
[2017.70 --> 2022.36]  And if you have flourishing companies, you're flourishing cultures, but you know, who's at the helm.
[2022.48 --> 2030.82]  And so I think we've just going to use that language and vernacular and never know in these environments if that's foreign or, or regular.
[2030.82 --> 2038.60]  But I know even from your own leadership and your direction, our relationships that I feel comfortable sharing that purpose is at the core.
[2038.60 --> 2055.36]  There's a lot of your personal data out there on the internet.
[2055.56 --> 2057.72]  And you know this, anyone can see this stuff.
[2058.12 --> 2059.22]  There's more than you think though.
[2059.22 --> 2066.16]  Your name, your contact info, your social security number, your home address, your various addresses, your past addresses.
[2066.58 --> 2068.98]  There's even information about your family members.
[2069.30 --> 2070.90]  Maybe even the name of your cat.
[2071.36 --> 2074.94]  This is all being compiled by data brokers and is being sold.
[2075.24 --> 2078.50]  Now these data brokers, they make a profit off your data, obviously.
[2078.90 --> 2079.40]  So they do it.
[2079.40 --> 2083.98]  Your data is a commodity and anyone on the web can buy your private details.
[2084.20 --> 2085.52]  They can identity theft you.
[2085.60 --> 2086.30]  They can fish you.
[2086.44 --> 2088.10]  They can attempt to fish you.
[2088.20 --> 2089.20]  They can harass you.
[2089.46 --> 2090.70]  They can send you unwanted spam.
[2090.78 --> 2092.54]  They can call you nonstop.
[2092.80 --> 2094.34]  And this is something I get lots.
[2094.86 --> 2098.42]  But now you're able to protect your privacy online with Delete Me.
[2098.78 --> 2106.28]  As a person who exists publicly for some time now, especially someone who shares their opinions online quite frequently,
[2106.28 --> 2110.34]  I'm aware, hyper aware of safety and security.
[2110.60 --> 2111.46]  And I take it seriously.
[2111.62 --> 2116.42]  And it's easier than ever to find personal information about anyone online, really.
[2116.76 --> 2122.22]  All this data is just hanging out on the internet and can have actual consequences in the real world.
[2122.52 --> 2125.28]  That's why I was excited about finding this recent solution.
[2125.68 --> 2127.44]  And as sponsor of this show, Delete Me.
[2127.80 --> 2133.10]  Delete Me is a subscription service that removes your personal information from hundreds of data brokers online.
[2133.10 --> 2136.98]  When you sign up, you can provide Delete Me with exactly what information you want deleted.
[2137.46 --> 2139.02]  And their experts take it from there.
[2139.40 --> 2144.14]  They send you regular personalized privacy reports showing what information they found on the internet about you,
[2144.34 --> 2146.76]  where they found it, and what they removed.
[2147.20 --> 2149.88]  And Delete Me isn't just a one-time service.
[2150.42 --> 2157.84]  They are always working for you, constantly monitoring, constantly removing your personal information that you don't want on the internet.
[2157.84 --> 2164.04]  And to put it simply, Delete Me does all the hard work of wiping your data, your family's personal information,
[2164.04 --> 2167.76]  and all these things you don't want out there from those data brokers' websites.
[2168.34 --> 2174.36]  Now, the next step is to take control of your personal data and keep it private forever by signing up for Delete Me.
[2174.68 --> 2179.26]  Now, at a special discount rate for our listeners, of course, this is awesome.
[2179.26 --> 2186.64]  Get 20% off your Delete Me plan by texting PRACTICAL to 64000.
[2187.70 --> 2192.78]  Again, text the word PRACTICAL to 64000.
[2193.76 --> 2197.56]  And, of course, you may know this already, but message and data rates may apply.
[2197.88 --> 2199.62]  Check the terms, all that good stuff.
[2199.88 --> 2206.46]  Once again, text the word PRACTICAL to 64000 and get 20% off Delete Me.
[2206.90 --> 2207.12]  Enjoy.
[2207.12 --> 2207.18]  Enjoy.
[2209.26 --> 2210.26]  Enjoy.
[2223.76 --> 2235.16]  So, Jeff, as we kind of jump fully into the AI aspects here, could you describe, without giving away any secret sauce, obviously, anything like that,
[2235.16 --> 2245.62]  but kind of describe which AI technologies have been important to help get you go and some of the things that you're most interested in in terms of, you know,
[2245.66 --> 2252.90]  because there's a – we've been talking so much about, you know, about generative AI and large language models in recent years,
[2252.90 --> 2266.36]  and I'm sure that's part of the mix, but one of the things that we're starting to do at this point is kind of understand how people are using those and also what other things they might be interested in that are not necessarily, you know,
[2266.36 --> 2268.56]  straight out of the line at another LL.
[2268.62 --> 2273.70]  I'm curious if you kind of share how you've built the business around different types of technologies a bit.
[2274.62 --> 2274.80]  Sure.
[2274.98 --> 2281.74]  And I can continue on the user journey and talk about the case in which it's being applied.
[2281.74 --> 2291.14]  You know, so if we look at, as we said, when a user signs up, we spend three to four weeks analyzing their data before we create that baseline profile for the user.
[2291.54 --> 2296.82]  Then based on their listening, we estimate that delta change of the user from their natural baseline.
[2297.46 --> 2306.70]  So, when Chirp looks at the music or song, it uses the acoustic features from the song to map it to, I guess, the term multidimensional vector, right?
[2306.70 --> 2313.80]  So, the vector sits in one or multiple clusters where at the center, it represents the first level of emotions.
[2314.52 --> 2317.60]  So, we inside, we call them L1s, level one emotions.
[2317.92 --> 2319.78]  It's energetic, melancholy, aggravated.
[2319.86 --> 2322.62]  So, what are those core emotions that we're uncovering?
[2322.70 --> 2328.58]  And the distance of the vector from the center indicates its closeness in the membership of that L1 group.
[2328.58 --> 2337.58]  Now, once these are defined, so the relationships are defined, a combination of them with the specific weightages ends up with L2s.
[2338.14 --> 2340.46]  Now, the L2s, again, might just be an internal term.
[2340.56 --> 2343.64]  They're second-level attributes that are relevant inside of the workplace.
[2344.60 --> 2351.72]  So, executives, they were less interested in baseline emotion, kind of, you know, are you happy, sad, or sideways?
[2351.72 --> 2360.04]  But really, how does it affect a person's balance, their motivation, their stress, and knowing the correlation between those to get ahead of burnout?
[2360.28 --> 2363.40]  And so, we had to really define those organizational attributes.
[2363.64 --> 2373.06]  And I'd say, your point on secret sauce, it really is knowing the L1 group memberships for a song and then knowing the weight is necessary for each combo to generate those L2s.
[2373.06 --> 2375.58]  So, to get an accurate level there.
[2375.58 --> 2380.56]  So, then, based on further listening, estimate the change from the baseline.
[2380.84 --> 2390.26]  Since the baseline is unique to each user, as you said, Daniel, we can do a better job knowing who they are, I'd say, fingerprinting it to them week on week.
[2390.48 --> 2393.66]  And so, measuring that data every week.
[2393.84 --> 2397.30]  And then, from there, pulling in the podcast, audiobooks, you know, for context.
[2397.30 --> 2402.84]  But what they end up with is the organization ends up with actionable insights to serve their people.
[2403.12 --> 2405.18]  People are equipped with their emotional data point.
[2405.68 --> 2413.26]  You've got the extrinsic motivation of rewards and perks, getting them in, the intrinsic motivation of data point, understanding how they're feeling.
[2413.64 --> 2417.84]  And so, you've got self-awareness, self-regulation, and leads to reward.
[2417.84 --> 2425.10]  But, you know, as far as the generative versus traditional, the traditional side is what's analyzing it.
[2425.50 --> 2430.10]  The generative will show up in the messaging back to the individual.
[2430.34 --> 2436.00]  So, if you look at, you've got an e-score, and, hey, this is what's changing your life, and your motivation is going up, and your balance.
[2436.18 --> 2441.06]  And so, you're getting an idea for the fluidity of how you're feeling and your emotional well-being.
[2441.42 --> 2445.66]  And then, you'll have a little copy area that speaks to that, you know.
[2445.66 --> 2448.58]  And that is unique to their situation.
[2449.32 --> 2454.92]  And then, we'll do the same for the organizations on, you know, their tips, trends, triggers, and how to understand it.
[2454.96 --> 2461.24]  But I would say that's really where the generative comes in, and it becomes unique to them.
[2461.72 --> 2465.50]  And then, the third element being that it individualizes the perks.
[2465.66 --> 2471.96]  Again, like I said about dark roast, coffee, or whatever that is, getting to know you, and how does it spit that out.
[2472.82 --> 2474.48]  That's really diving under the hood.
[2474.48 --> 2479.50]  And like you said, without giving out too much, you know, but understanding the science behind it.
[2479.98 --> 2493.28]  On the actual business user side, I could imagine, you know, you even mentioned a little bit of this as getting, of getting the right people in the room that could think about how to visualize this for the business user.
[2493.28 --> 2502.80]  Because I can imagine if you have an organization with 5,000 people, 10,000 people, you know, 100,000 people.
[2502.80 --> 2516.36]  Some of this can be broken down by team or group or project or other things like that, even, in addition to kind of overall or at the kind of interactions with the individual level.
[2516.36 --> 2525.12]  So, yeah, how do you think about that at a more consuming side of this and the utility of that?
[2525.38 --> 2536.84]  And how have you kind of found the right level of detail that kind of balances insight, privacy, utility for the individual, you know, kind of opted-in user?
[2537.46 --> 2537.60]  Yeah.
[2537.60 --> 2538.68]  Any thoughts there?
[2538.94 --> 2546.60]  To speak to the original business case as we said it, so carving out the military, pro-sport team, therapists, and so on.
[2546.60 --> 2561.00]  But looking at that HR tech, it was fascinating as we're working with CEOs, CHROs, head of people, chief administrative officer, to really understand their charge inside of these organizations or agencies.
[2561.32 --> 2563.20]  And you're right, the size of the company matters.
[2563.90 --> 2569.16]  You know, we were going with enterprise companies, CHROs are saying, thank God you didn't come to me with solutions.
[2569.80 --> 2571.68]  I have an entire library of solutions.
[2571.82 --> 2572.94]  I just need better insights.
[2573.24 --> 2574.72]  How do I deploy them better?
[2574.72 --> 2580.26]  Who do I serve with these leadership development, with perks, you know, with executive coaching and so on?
[2580.74 --> 2587.78]  So, you kind of have that where they're saying, we just want better diagnostic tools, better insights to work with.
[2588.18 --> 2595.88]  You know, one said, hey, I spent last year $250,000 on a single survey that took 90 days to get the results back and then nine months to talk about it.
[2596.12 --> 2599.88]  For a moment in time that we weren't in anymore, you know, the company had changed.
[2599.88 --> 2604.48]  And so, this gives me regular insights that I can really look at.
[2604.84 --> 2606.44]  And then I can call up that manager.
[2606.56 --> 2609.18]  Hey, this team is looking on the verge of burnout.
[2609.48 --> 2610.72]  You know, what's going on down there?
[2610.78 --> 2612.00]  Your team's crushing it.
[2612.52 --> 2614.28]  Hey, how can I provide you with more resources?
[2614.44 --> 2615.70]  And they all segment differently.
[2615.84 --> 2616.12]  You're right.
[2616.18 --> 2616.90]  It's regional.
[2616.90 --> 2619.94]  It's by business unit, different teams.
[2620.20 --> 2623.54]  And so, you figure out that segmentation and then they run with it.
[2623.94 --> 2629.94]  The smaller companies I was finding are saying, great, thank you for this information, but what do I do with it?
[2630.36 --> 2635.26]  You know, is that can you help us better understand what this means inside of our organization?
[2635.26 --> 2643.00]  So, what we did was we ended up with our data scientists, behavioral scientists, organizational health, sitting down with these companies saying, hey, this is what I see.
[2643.46 --> 2644.92]  I mean, already they're looking at the data.
[2645.38 --> 2646.40]  Everything's coming back.
[2646.50 --> 2647.22]  They're looking at it.
[2647.26 --> 2647.48]  Great.
[2647.56 --> 2648.44]  Let me tweak this.
[2648.50 --> 2653.32]  Let me change this before the reporting goes out because they have a dashboard and the report outs on teams.
[2653.72 --> 2660.48]  And then at 90 days, we sit down with the client and with the behavioral scientists say, okay, this team is showing these signs of this.
[2660.48 --> 2664.40]  I would provide more, you know, fuel in the fire, rewards, perks.
[2664.48 --> 2665.66]  Let's really, you know, hone in on this.
[2665.92 --> 2667.46]  This is an area you might want to check on.
[2667.88 --> 2679.06]  And so, we're in that phase right now to understand, did the large enterprise companies say they had the tools and just projecting that they had everything, but they really need help or not?
[2679.14 --> 2679.96]  And we don't know yet.
[2680.04 --> 2682.32]  So, I think it's been fascinating to walk alongside them.
[2682.78 --> 2686.50]  We said, hey, what is our role in remediation, intervention, solution?
[2686.50 --> 2693.00]  Let's first be the best in the world diagnostic tool using music as a signal for emotional health and well-being.
[2693.12 --> 2693.30]  Great.
[2694.00 --> 2697.16]  Then, where do we step into the solutions and recommendations?
[2697.90 --> 2699.38]  And so, we have a full report out.
[2699.48 --> 2701.94]  Say, hey, you know, this team, motivation's up.
[2702.08 --> 2702.86]  Stress is up.
[2702.96 --> 2704.10]  Balance is okay.
[2705.10 --> 2705.78]  Collaboration's good.
[2705.84 --> 2706.76]  It means they're crushing it.
[2706.82 --> 2707.86]  Let's provide these.
[2708.18 --> 2709.78]  Looks like collaboration's going down.
[2709.92 --> 2710.94]  Stress is remaining high.
[2711.06 --> 2712.08]  Balance is a little bit off.
[2712.38 --> 2713.48]  Okay, they're on the verge of burnout.
[2713.48 --> 2721.24]  So, to understand behavior and what's truly happening there and how it influences and impacts companies is important.
[2721.46 --> 2723.78]  And so, that's why we have the team look at that.
[2723.96 --> 2730.46]  And we're providing this HR intelligence center to these clients to say, hey, do you want to tap into this?
[2730.54 --> 2731.20]  Can we help?
[2731.36 --> 2734.08]  And I'm finding that they like that.
[2734.16 --> 2736.64]  They like, you know, being led to water.
[2736.86 --> 2739.82]  It's not a reflection of whether they're doing a good job or not.
[2739.82 --> 2744.38]  Let's just say, hey, here are some resources that you might want to consider because we created for that reason.
[2744.80 --> 2745.70]  They do care.
[2746.12 --> 2747.98]  But, and they're throwing resources at employees.
[2748.32 --> 2751.52]  Let's just help them better deploy those resources so they land.
[2751.94 --> 2753.90]  You know, so people stay in their jobs.
[2754.00 --> 2758.60]  And companies are growing and people feel excited to come to work every day.
[2758.60 --> 2763.78]  As you kind of address that HR leader profile, you know, on your website there.
[2763.90 --> 2767.00]  And you have these others and you've alluded to them earlier in the conversation.
[2767.52 --> 2770.18]  Therapy practices, sports, military, university.
[2770.58 --> 2779.22]  I'm curious is when you're positioning this capability to these different groups, is it all more or less the same?
[2779.22 --> 2792.16]  Or are there very distinct ways that they perceive the value that is, for instance, you know, the HR that you've talked about versus military or versus university that is distinctly different in those groups?
[2792.30 --> 2794.52]  And if so, could you kind of describe what that is?
[2794.98 --> 2795.10]  Sure.
[2795.34 --> 2802.52]  I was with a friend at an event and he was explaining to his wife what Chirp is.
[2802.52 --> 2808.46]  And she sharply elbows him in the ribs and says, see, my music knows where I'm at, you know?
[2808.56 --> 2810.36]  And it just was the funniest like moment.
[2810.48 --> 2813.60]  And I'd say that is the consistency across those verticals.
[2813.82 --> 2817.26]  So how they apply it, the value they're getting out of it varies.
[2817.42 --> 2822.38]  But at its core, it's all the same to really understand people's emotional state there.
[2822.78 --> 2825.50]  Now, when we, like I said, built it for HR, great.
[2825.62 --> 2826.26]  There's a need.
[2826.46 --> 2831.72]  As we start to go in the others, it's been interesting because you're getting more into mental health and performance.
[2831.72 --> 2836.00]  We start with organizational health by addressing, you know, emotional well-being.
[2836.62 --> 2842.42]  And then on the mental health side, we have several hundred therapists that are starting to sign up and use it and everything.
[2842.62 --> 2846.82]  We're figuring out, okay, how do you craft this as a tool inside of their agency, inside of their clinics?
[2847.42 --> 2851.68]  And what they want to use it for is better patient care.
[2851.88 --> 2854.54]  They're more connected to their clients.
[2855.06 --> 2857.14]  And then also, it's a revenue model.
[2857.26 --> 2861.06]  It's an added assessment tool that is helping them build their practices.
[2861.06 --> 2864.70]  Now, they're coming out of COVID being overtaxed, at capacity.
[2864.92 --> 2866.98]  How do you build by practice without adding work to me?
[2867.06 --> 2867.56]  It's like, great.
[2867.86 --> 2870.30]  Let's help you build your business by caring for your people better.
[2870.78 --> 2872.36]  And so that's a unique tool.
[2872.76 --> 2874.00]  So you think about their mindset.
[2874.64 --> 2877.78]  That's different than the HR leader, which is different on the military.
[2877.88 --> 2884.90]  Where the military came in, you know, we've got one base who it's 4,200 troops under their command.
[2884.90 --> 2888.30]  120 of them, you know, we're looking at piloting with.
[2888.50 --> 2893.04]  And that 120 has had three suicides and three suicidal ideations in the last year.
[2893.58 --> 2894.96]  I mean, that's insanely high.
[2895.50 --> 2901.96]  And so the colonel's saying, hey, I want to use anything, whatever it takes, you know, to really know where my troops are at.
[2901.96 --> 2904.40]  I want to, you know, keep them alive, keep them healthy.
[2905.00 --> 2906.86]  And so that's a different use case.
[2906.86 --> 2913.84]  And on the sports side, where that started was the universities are saying, hey, we want to use this for our college.
[2914.28 --> 2915.90]  And I challenge the president and say, why?
[2916.36 --> 2918.40]  They say, well, you know, student retention.
[2918.72 --> 2923.14]  If students are emotionally, socially, emotionally healthy, then they stay in school.
[2923.36 --> 2924.12]  They pay their tuition.
[2924.32 --> 2925.74]  I mean, that makes a lot of sense to me.
[2925.80 --> 2925.96]  Great.
[2926.04 --> 2926.76]  That's student retention.
[2926.90 --> 2927.32]  That's revenues.
[2927.40 --> 2928.20]  That's a business issue.
[2928.20 --> 2932.82]  And so as we start to look at that, you've got organizational health inside.
[2932.94 --> 2934.60]  Then you start to look at campus wide.
[2934.70 --> 2939.18]  But then the athletics director started to call saying, hey, this is interesting.
[2939.60 --> 2941.00]  Can we do it in sports?
[2941.52 --> 2943.34]  You know, this is something with student athletes.
[2943.64 --> 2948.32]  We haven't dealt with this level of anxiety and stress and depression that we had before.
[2948.40 --> 2951.12]  So could this be a resource so I can better help them?
[2951.52 --> 2955.16]  And then one athletic director said, can I also optimize behavior?
[2955.60 --> 2956.86]  Help us win some championships.
[2956.86 --> 2960.98]  I mean, so you start to look at, okay, now we're getting into behavioral health and performance.
[2961.64 --> 2962.90]  And that gets exciting.
[2963.32 --> 2967.42]  But it's just, it's figuring out that balancing act without feeling like the entrepreneur that's
[2967.42 --> 2968.26]  trying to boil the ocean.
[2968.90 --> 2974.40]  You know, it's so each one of them, I'd say has that underlying belief that music knows
[2974.40 --> 2975.92]  where I'm at, you know?
[2976.00 --> 2980.02]  And so by better understanding people's emotional ability, I can serve them.
[2980.10 --> 2980.74]  I can heal them.
[2980.84 --> 2981.72]  I can improve them.
[2981.76 --> 2982.70]  I can optimize them.
[2982.70 --> 2986.64]  But all kind of on that core tool using this engine.
[2986.64 --> 2993.60]  As we kind of get close to the close here, I've just kind of struck with the kind of nature
[2993.60 --> 3001.08]  of what you're building here, which is using AI in a way that's driving more human connection
[3001.08 --> 3006.98]  and human connection to resources, hopefully that improve their wellness, help them flourish.
[3006.98 --> 3013.00]  That's super encouraging to me as I think about the future, you know, rather than AI solutions
[3013.00 --> 3019.58]  that kind of increase isolation and have us interacting more just with AI agents.
[3020.24 --> 3026.54]  But I'm wondering, as you look towards the future, you know, maybe in terms of what Chirp
[3026.54 --> 3032.14]  is going to do, but maybe more broadly is kind of, you know, what's possible with this technology
[3032.14 --> 3037.90]  in these ways that are actually, you know, positive and restorative.
[3038.26 --> 3039.56]  What are you excited about?
[3039.64 --> 3040.88]  What's encouraging to you?
[3041.00 --> 3044.94]  What are you thinking about as you're going into this next phase of your journey?
[3045.36 --> 3049.70]  Well, I'm very excited about some of these tributaries that I mentioned, you know, going
[3049.70 --> 3055.80]  upstream on the mental health side, saving lives downstream on sports and performance.
[3055.80 --> 3057.88]  Still with music at the core.
[3058.36 --> 3062.84]  I would say you mentioned it is not taking the human out of the picture.
[3063.44 --> 3065.04]  You know, we are relational beings.
[3065.28 --> 3068.48]  And so, first, you know, let's heal the soul.
[3068.62 --> 3069.36]  Let's use music.
[3069.46 --> 3070.20]  Let's speak to them.
[3070.26 --> 3070.96]  Let's bring them alive.
[3071.06 --> 3071.40]  Great.
[3071.86 --> 3073.94]  Then, is there a way to connect people around music?
[3074.58 --> 3080.08]  You know, is there a way that this then takes you a step further that is greater connectivity
[3080.08 --> 3083.62]  with others around the music you listen to, around how you're feeling?
[3083.62 --> 3086.20]  And so, I think that would be great to explore.
[3086.34 --> 3091.94]  Again, not to put more directions on this company, but I would say let's master the organizational
[3091.94 --> 3093.90]  health, the mental health, and the performance.
[3094.40 --> 3096.74]  And then look at community formation.
[3097.04 --> 3098.96]  You know, music is a connector.
[3099.12 --> 3099.94]  It always has been.
[3100.44 --> 3105.28]  And so, how do we make people feel part of something greater, keeping the human at the
[3105.28 --> 3105.52]  center?
[3106.06 --> 3107.78]  And AI is a complement to that.
[3108.28 --> 3108.52]  Great.
[3108.74 --> 3108.94]  Yeah.
[3109.00 --> 3110.54]  Thank you for that perspective.
[3110.54 --> 3112.92]  I think that's an amazing way to close out here.
[3113.16 --> 3114.94]  Thank you so much for joining us, Jeff.
[3114.98 --> 3116.68]  This has been a real pleasure.
[3116.90 --> 3122.00]  So happy we got connected and look forward to analyzing some of my own music.
[3122.14 --> 3127.84]  I believe that you mentioned kind of getting some people into the system and in having them
[3127.84 --> 3131.22]  understand a little bit from their own music playlist.
[3131.38 --> 3133.98]  I believe there's a link that you can share, right?
[3134.06 --> 3138.72]  That if people are interested, they can take a look and understand some of these insights.
[3138.72 --> 3139.44]  You want to share that?
[3139.44 --> 3140.36]  No, we'd love to.
[3140.58 --> 3146.44]  So we have a, I would say, an alpha group, friends, families, practitioners, experts that
[3146.44 --> 3148.40]  are joining in this movement with us.
[3148.56 --> 3154.10]  And so that's a separate link at mychirp.ai, M-Y-C-H-R-P.ai.
[3154.52 --> 3159.14]  We put it in the show notes, but it's really just, you want to know what it says about you.
[3159.42 --> 3162.06]  It's free, it's fun, and it provides a feedback loop for us.
[3162.06 --> 3168.50]  And I would honor the technical savviness of your audience to really teach me something.
[3168.82 --> 3170.98]  And so to play with it and test drive it.
[3171.06 --> 3171.62]  Awesome.
[3171.90 --> 3172.58]  Thanks for sharing.
[3172.70 --> 3174.10]  We'll link that in the show notes.
[3174.44 --> 3176.30]  And yeah, thanks again for joining, Jeff.
[3176.34 --> 3177.08]  Really appreciate it.
[3177.08 --> 3178.18]  I appreciate you both.
[3178.18 --> 3186.22]  All right.
[3186.56 --> 3188.40]  That is our show for this week.
[3188.90 --> 3194.72]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[3194.94 --> 3197.18]  There you'll find 29 reasons.
[3197.40 --> 3200.76]  Yes, 29 reasons why you should subscribe.
[3200.76 --> 3202.60]  I'll tell you reason number 17.
[3203.26 --> 3205.96]  You might actually start looking forward to Mondays.
[3206.12 --> 3208.82]  Sounds like somebody's got a case of the Mondays.
[3209.22 --> 3213.76]  28 more reasons are waiting for you at changelog.com slash news.
[3213.96 --> 3219.66]  Thanks again to our partners at Fly.io, to Breakmaster Cylinder for the Beats, and to you for listening.
[3220.06 --> 3222.72]  That is all for now, but we'll talk to you again next time.
[3230.76 --> 3231.86]  ChangeLog.
