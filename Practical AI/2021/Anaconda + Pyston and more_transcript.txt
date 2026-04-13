[0.00 --> 5.14]  I have maintained for quite some time that we're at one of those generational phase changes.
[5.48 --> 10.90]  With the introduction of the PC and personal computing from mini computers and Vaxes and
[10.90 --> 14.38]  mainframes, that was one shift that happened almost 50 years ago at this point.
[14.94 --> 18.70]  And a lot of technologies we use are still ones from the early days of the PC.
[19.24 --> 21.16]  Software, hardware, you name it, right?
[21.16 --> 25.48]  Our program models and architectures, languages, operating systems, all of those things are
[25.48 --> 27.88]  inherited from the long shadow of the 70s.
[27.88 --> 34.18]  And what we're seeing now, ubiquitous connectivity with supercomputers on demand and rentable
[34.18 --> 41.06]  by the hour, and with now algorithmic capabilities that are far beyond what we'd ever conceived
[41.06 --> 45.10]  possible before, all those come together to create a new landscape.
[45.58 --> 47.26]  We're entering this era of cybernetics.
[47.32 --> 48.76]  We're just the very beginning of it.
[49.00 --> 52.74]  And it's going to be completely different and so much more heterogeneous.
[53.22 --> 54.10]  It's a sea change.
[54.10 --> 59.50]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[59.90 --> 60.44]  We love Linode.
[60.52 --> 61.94]  They keep it fast and simple.
[62.08 --> 64.44]  Check them out at linode.com slash changelog.
[64.66 --> 66.74]  Our bandwidth is provided by Fastly.
[67.08 --> 70.64]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[70.90 --> 72.62]  Get a demo at LaunchDarkly.com.
[72.62 --> 80.24]  SignalWire is real-time video tech to help you create interactive video experiences previously
[80.24 --> 80.90]  not possible.
[80.90 --> 87.22]  It gives you access to broadcast quality, ultra low latency video that's proven and trusted
[87.22 --> 90.38]  by Amazon, Ring Doorbell, Zoom, and others.
[90.72 --> 94.76]  See why the future of video communication is being built on SignalWire.
[94.76 --> 100.90]  They have easy to deploy APIs, SDKs for the most popular programming languages, and expert
[100.90 --> 104.38]  support from the OGs of software-defined telecom tech.
[104.82 --> 110.38]  Try it today at SignalWire.com and use code AI for $25 in developer credit.
[110.96 --> 113.02]  Just visit SignalWire.com.
[113.22 --> 117.38]  That's SignalWire.com and use code AI to receive that $25.
[117.92 --> 121.60]  Once again, that's SignalWire.com, code AI.
[124.76 --> 135.98]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[136.30 --> 138.04]  productive, and accessible to everyone.
[138.44 --> 142.44]  This is where conversations around AI, machine learning, and data science happen.
[142.70 --> 146.94]  Join the community and Slack with us around various topics of the show at changelaw.com
[146.94 --> 148.82]  slash community and follow us on Twitter.
[148.98 --> 150.52]  We're at Practical AI FM.
[154.76 --> 159.72]  Welcome to another episode of Practical AI.
[160.10 --> 161.70]  This is Daniel Whitenack.
[161.82 --> 168.06]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[168.06 --> 171.38]  Benson, who is a tech strategist at Lockheed Martin.
[171.62 --> 172.26]  How are you doing, Chris?
[172.64 --> 174.02]  I'm doing very well, Daniel.
[174.18 --> 176.52]  It is a beautiful August day.
[176.76 --> 180.00]  At the point we're recording this, we just had Tropical Storm come through.
[180.20 --> 180.50]  Yeah.
[180.50 --> 186.12]  It was Fred, and so I'm just relieved that my house guest, Fred, decided to leave.
[186.30 --> 188.24]  I am joining this podcast from my rowboat.
[189.24 --> 194.00]  Well, speaking of interesting events, it has been one of those years, right?
[194.38 --> 200.64]  And if you remember last year, almost exactly a year ago, we were talking with Peter Wang
[200.64 --> 205.92]  from Anaconda about the state of data science report that Anaconda puts out.
[206.44 --> 207.90]  And we have Peter with us again.
[208.06 --> 208.60]  How are you doing, Peter?
[208.84 --> 209.24]  Hi.
[209.36 --> 209.74]  Hi, Daniel.
[209.74 --> 210.24]  Hi, Chris.
[210.90 --> 211.80]  I'm doing well.
[211.92 --> 212.44]  Good to be here.
[212.56 --> 212.72]  Excellent.
[213.00 --> 214.80]  Chris, I'm glad to hear that you are well.
[214.88 --> 215.90]  I don't know if you're in a rowboat or not.
[216.22 --> 218.08]  If you are, I hope that there's no holes in it.
[218.54 --> 219.84]  If you're not, I'm glad you're not sustaining.
[222.08 --> 223.04]  I'm above water.
[223.14 --> 223.78]  Things are good.
[224.14 --> 224.58]  Me too.
[224.74 --> 224.98]  Me too.
[225.04 --> 226.40]  We had a really good conversation last time.
[226.68 --> 227.56]  Yeah, for sure.
[227.68 --> 232.64]  Well, I mean, how have things been for Anaconda over the interesting year that we've had?
[233.02 --> 234.50]  It has been a really great year for us.
[234.62 --> 235.78]  Business is going well.
[235.88 --> 236.94]  We're hiring and growing.
[237.34 --> 238.88]  We're just firing away on all cylinders.
[238.88 --> 240.10]  So it's been a really great time.
[240.22 --> 241.90]  And I'm very excited about the future.
[241.90 --> 242.34]  Yeah.
[242.54 --> 248.24]  So maybe just remind the listeners, this state of data science report that you do, you just
[248.24 --> 251.12]  give us a sense of who contributes to that?
[251.34 --> 255.72]  What sort of audience is behind the graphs and the statistics that you gather?
[255.72 --> 256.16]  Yeah.
[256.16 --> 257.84]  So a brief rundown.
[258.00 --> 262.82]  It's something we've been doing for many years now, but it's a survey of our user base,
[262.96 --> 264.80]  but not limited to our user base.
[264.88 --> 268.38]  We put the call out, obviously, through the channels that we have the most access to.
[268.72 --> 271.90]  So it's going to be a lot of Anaconda users, but anyone's free to take it.
[271.98 --> 273.78]  We put the call out on social media and whatnot.
[274.30 --> 279.06]  This year, we had almost 4,300 participants from 140 countries.
[279.06 --> 279.50]  Yeah.
[279.50 --> 283.84]  We ran the survey for about a month, runs around April to May timeframe.
[284.46 --> 288.30]  So we had a third, not quite a third of our respondents were students.
[288.50 --> 288.98]  Oh, that's awesome.
[289.02 --> 290.04]  About 10% were academics.
[290.34 --> 294.94]  And the remainder, about 65%, were practitioners, I guess is what we would call them.
[295.52 --> 297.48]  But they come from, yeah, 140 different countries.
[297.70 --> 304.32]  The vast majority coming from North America, Brazil, and Australia, India, of course, Europe.
[304.56 --> 306.36]  But there's practitioners all over the world.
[306.36 --> 310.60]  So it's really great to see that the data science is a globally impacting movement.
[311.06 --> 311.08]  Yeah.
[311.22 --> 316.82]  And I know, so you mentioned it's your users, but my guess would be that vast majority of
[316.82 --> 322.20]  data scientists that are practicing out there at least have come across or utilized Anaconda
[322.20 --> 323.44]  at some point.
[323.62 --> 328.68]  So, I mean, that's pretty cool that you are sort of getting this slice across the whole industry.
[329.28 --> 336.34]  And has the geographic distribution of participants, has that changed over the years in terms of how
[336.34 --> 338.24]  international the audience is?
[338.36 --> 343.80]  Well, you know, we haven't done a lot of deep dive into that, but it seems to be pretty consistent.
[344.48 --> 349.46]  I mean, it generally follows population densities, actually, for the most part, from what we can
[349.46 --> 349.70]  tell.
[350.26 --> 351.70]  India is always very strong.
[351.84 --> 353.64]  There's a huge amount of data science happening there.
[353.64 --> 359.10]  South America is, I think, from what I can tell, South America is increasing a little bit more
[359.10 --> 359.94]  than the baseline.
[360.40 --> 361.64]  But really, it's global.
[361.74 --> 362.12]  It's everywhere.
[362.38 --> 365.04]  And there's a lot of users in Africa and in the Middle East.
[365.48 --> 369.96]  No, it's really wonderful to see that the language and the tools have spread globally.
[369.96 --> 374.38]  So I'm sure there's some questions that are carryovers and sort of are always there.
[374.72 --> 380.16]  How, if at all, did you modify the survey and what you were asking this year in light
[380.16 --> 383.26]  of the pandemic and all the things that have gone on?
[383.52 --> 384.10]  Yeah, yeah.
[384.16 --> 388.22]  We do carry over a lot of the questions, but then we also modify them a little bit.
[388.30 --> 393.62]  So a couple of years ago, we had a lot more of a deep dive into what tools, what platform
[393.62 --> 394.74]  kind of things are you using?
[394.84 --> 396.66]  And what is your orientation towards cloud?
[396.74 --> 397.74]  And have you heard of Kubernetes?
[397.92 --> 398.54]  Things like that.
[398.54 --> 404.34]  Now, this year, we did ask about COVID and we asked how it changed people's budgets and
[404.34 --> 406.18]  their organizations relative to data science.
[406.60 --> 413.10]  But this year, we also did a bit more of a deep dive into what are the roadblocks to production?
[413.42 --> 417.90]  Because that seems to be a topic that's at the forefront of everyone's minds now that
[417.90 --> 420.14]  people are learning data science, they're building useful models.
[420.50 --> 421.66]  Now they have to get them into production.
[422.14 --> 426.32]  And we asked those questions because we heard different stories from different kinds of people
[426.32 --> 427.22]  and different job functions.
[427.22 --> 429.40]  So we asked that broadly of the folks.
[429.80 --> 432.46]  We can talk about that a little bit later, some of the deep dive details there.
[432.66 --> 433.26]  It's interesting.
[433.40 --> 436.24]  There's actually some really interesting insights to be gleaned from that.
[436.46 --> 440.82]  But I think for me, one of the things that has changed year to year is we always ask people,
[441.02 --> 442.12]  what is your job function?
[442.58 --> 443.52]  What is your job level?
[443.64 --> 444.76]  Like, are you entry level?
[445.02 --> 446.04]  Are you individual contributor?
[446.78 --> 448.12]  Are you a director or VP?
[448.12 --> 456.42]  And this year, the vast majority of our respondents are senior or principal, manager, director, VP,
[456.62 --> 456.98]  C-suite.
[457.36 --> 462.58]  Like, less than 20% were either entry level or other, which is very strange to me.
[462.80 --> 467.60]  Now, that's only about 2,600 of the respondents answered the current job level question.
[468.04 --> 470.04]  But that one had to be scratching my head a little bit.
[470.04 --> 472.96]  So just as you're going through your thought process, what are you attributing that to?
[473.06 --> 474.88]  Or what's your theory about it?
[475.00 --> 480.80]  Well, a quarter of the folks identify themselves as being senior, a quarter are manager, and
[480.80 --> 483.36]  then, you know, 10% director, about 8% principal.
[483.48 --> 487.76]  So I think what's happening is there's a little bit of title inflation in data science roles.
[487.76 --> 493.20]  And some data scientists to be retained and to not get picked off by, like, big tech giants,
[493.64 --> 497.40]  they're maybe getting some titles and promotions and whatnot.
[497.72 --> 500.48]  And that might be what's affecting this.
[500.66 --> 504.06]  And it could also be that as teams are growing a little bit, you naturally have to, you know,
[504.30 --> 508.72]  bump up the title of the senior person in the team as you're hiring, you know, more entry
[508.72 --> 509.90]  level people behind them.
[510.06 --> 511.00]  That's my hypothesis.
[511.40 --> 513.44]  But, you know, I haven't validated that.
[513.44 --> 517.40]  But another thing that was really interesting is that, so we asked what your primary job function,
[517.40 --> 517.84]  right?
[518.20 --> 522.08]  Not what all the things you do, but really, what is your title or what is, you know, the
[522.08 --> 523.00]  primary job function?
[523.50 --> 529.22]  And over the years, the number of people who identify primarily as data scientists in our
[529.22 --> 533.42]  respondent pool, that number has been going down lower and lower and lower and lower.
[533.90 --> 540.30]  And we get more people from all walks of the business answering our polls.
[540.30 --> 545.78]  And they're using Anaconda in their jobs, but their titles are, you know, cloud engineer
[545.78 --> 547.98]  or a data engineer, I suppose data scientist.
[548.30 --> 552.40]  There's product managers, there's ML engineers, there's many other kinds of people, sysadmins.
[552.80 --> 556.66]  So data scientists this year, the number of people who had data scientists as their primary
[556.66 --> 559.80]  job function was only 11% in our respondent pool.
[559.80 --> 563.52]  I think that's the maturing of the industry is what it sounds like to me.
[563.72 --> 569.42]  Year by year is you're seeing, you know, more diversity in terms of job titles and different
[569.42 --> 572.16]  levels of people and not just everyone's a data scientist.
[572.68 --> 573.54]  Would you agree with that?
[573.66 --> 578.54]  Would you agree that data science is finally getting its fingers into every aspect of the
[578.54 --> 579.14]  global economy?
[579.52 --> 580.76]  Yeah, I do agree with that.
[580.88 --> 585.22]  I've held the opinion for a long time that this can't just be technology in its own little
[585.22 --> 586.70]  ivory tower, right?
[586.70 --> 592.08]  For data science and next generation of predictive analytics to be impactful, it has to spread
[592.08 --> 593.08]  across the organization.
[593.42 --> 594.40]  Everyone has to gain literacy.
[594.58 --> 596.32]  That's something we talked about in the previous podcast.
[597.02 --> 600.86]  And I think this is, you know, a positive signal that that is happening.
[601.40 --> 608.72]  Business analysts, VP of XYZ, product managers, sysadmins, cloud ops, DevOps people, all these
[608.72 --> 611.42]  different people are learning some of these technologies.
[611.64 --> 612.54]  I think it's a really good thing.
[612.54 --> 619.76]  Maybe it's also related to the fact that over the years, the data science tooling that we
[619.76 --> 625.08]  data scientists love and have been willing to put in the time to learn, in some ways
[625.08 --> 631.82]  that is becoming better documented, easier to manage sort of version dependency wise,
[632.14 --> 637.30]  like the tooling and the ecosystem is just a little bit easier to onboard into.
[637.30 --> 642.80]  I don't know if Anaconda, of course, is part of that ecosystem, but there's a lot of teams
[642.80 --> 648.06]  that are really working on having better documentation, having better software engineering practices
[648.06 --> 649.30]  around the things they're doing.
[649.44 --> 651.76]  So maybe engineers are a little bit less scared.
[651.92 --> 657.68]  I remember like my first data science position, DevOps Doug, if you're listening, you know, shout
[657.68 --> 658.66]  out to DevOps Doug.
[659.08 --> 662.00]  It was just like a nightmare to get my stuff.
[662.00 --> 666.24]  Like I would do this great thing and my Jupyter notebook and all of this.
[666.42 --> 672.28]  And then like he'd have to build like some Docker image with like pandas and all this stuff.
[672.36 --> 676.28]  And he hated it because it took like however long to build this image.
[676.28 --> 679.60]  And then it was like super bloated and huge.
[679.60 --> 686.56]  And maybe there's just like more understanding on the engineering side now and better tooling.
[686.68 --> 687.02]  I don't know.
[687.02 --> 692.04]  Any thoughts there, Peter, in terms of this intersection of the tooling we use in this
[692.04 --> 694.22]  DevOps world and workflow?
[694.80 --> 699.26]  I think I can say quite confidently there are more people using these tools and doing
[699.26 --> 700.92]  these things across the organization.
[701.46 --> 705.34]  I don't know that I want to go on the record to claim that they're having a better time of
[705.34 --> 708.28]  it or that it's gotten easier.
[708.76 --> 709.86]  I think that you're right.
[709.96 --> 711.44]  Some of the tooling has gotten better.
[711.64 --> 713.12]  You know, we keep pushing that boulder up the hill.
[713.28 --> 714.62]  We hope we're making some progress.
[715.04 --> 716.12]  And we're not the only ones.
[716.12 --> 717.18]  There's lots of people, right?
[717.22 --> 721.36]  There's the maintainer teams of individual projects themselves, as well as, you know,
[721.38 --> 724.94]  the broader Python community and the core Python developers and PyPA and people like
[724.94 --> 725.18]  that.
[725.68 --> 728.34]  But at the same time, the landscape's gotten more complex.
[728.94 --> 730.10]  There's more kinds of hardware out.
[730.10 --> 733.12]  There's more proprietary offerings for various cloud vendors.
[733.68 --> 739.12]  There's more different variants of GPUs that come out every year, every generation being
[739.12 --> 740.80]  so much better than the previous one.
[740.92 --> 743.68]  But you can't get rid of the old ones that you bought last year.
[743.86 --> 744.72]  You got to keep using them.
[744.72 --> 746.62]  And there's all these different things.
[746.72 --> 750.64]  So the landscape's getting more complex, even as some things are getting easier.
[751.14 --> 752.88]  And I think that trend will continue.
[753.58 --> 756.06]  So more people will be using this across the organization.
[756.32 --> 760.46]  There will be more people, I guess, motivated to try to solve the problem.
[760.68 --> 763.84]  But at the same time, everyone's busy, you know, and these problems are at the infrastructure
[763.84 --> 770.16]  level kind of below the radar or below the waterline of what DevOps Doug or software developer
[770.16 --> 772.40]  Sid are able to see.
[772.84 --> 774.50]  I'm trying to get the alliteration going there, you know.
[774.90 --> 775.62]  That was good.
[775.70 --> 776.12]  I liked it.
[776.20 --> 776.50]  Keep going.
[776.66 --> 780.96]  And so in any case, I think the spread across the organization means more people are probably
[780.96 --> 781.82]  feeling some of the pain.
[781.82 --> 787.28]  However, it also means that businesses are taking this seriously enough that despite the
[787.28 --> 789.36]  pain, they're still trying to roll forward with it.
[789.52 --> 791.42]  They're not abandoning it saying this is a bad idea.
[791.92 --> 792.70]  Oh, my God.
[792.76 --> 796.56]  We're going back to, you know, just using SaaS or we're going to stick with just Excel.
[796.78 --> 798.48]  No, everyone has to do this now.
[798.82 --> 801.90]  And it's just like, well, it's like lemmings jumping into the ocean.
[801.98 --> 804.02]  I'm still I'm sure it's cold, but they're all going to do it.
[804.08 --> 804.94]  You know, so.
[804.94 --> 809.00]  You made a point in there that I wanted to draw out for a second, and that's the fact
[809.00 --> 814.20]  that you said this is going to continue, meaning that the number of capabilities for doing
[814.20 --> 819.26]  DevOps and deploying and getting the things that we people in the data science world are
[819.26 --> 822.70]  interested in and bringing to the world and bringing to the markets.
[822.90 --> 826.58]  And yet the world itself is getting much, much more complicated.
[826.82 --> 830.30]  We're no longer always deploying onto some server in our data center.
[830.46 --> 834.16]  We're deploying edge devices and, you know, innumerable things.
[834.16 --> 836.66]  So do you think that's just an indefinite trend?
[836.78 --> 839.42]  Because we don't see the complexity going away anytime soon.
[839.66 --> 840.94]  Yeah, I think it's going to be indefinite.
[841.06 --> 844.08]  Well, nothing's indefinite, but I think it's going to be for the foreseeable future, at
[844.08 --> 846.26]  least the next five years, probably at least 10.
[846.66 --> 851.14]  If we kind of bump up a couple of levels here, zoom out to a 30,000 foot level above just
[851.14 --> 857.18]  the details of our survey results, I have maintained for quite some time that we're at one of those
[857.18 --> 859.18]  generational phase changes.
[859.76 --> 863.98]  You know, with the introduction of the PC and personal computing from many computers,
[864.16 --> 868.50]  and VAXs and mainframes, that was one shift that happened, you know, almost 50 years ago
[868.50 --> 868.96]  at this point.
[869.30 --> 873.26]  And a lot of technologies we use are still ones from the early days of the PC.
[873.86 --> 875.74]  Software, hardware, you name it, right?
[875.82 --> 880.06]  Our programming models and architectures, languages, operating systems, all of those things are
[880.06 --> 882.44]  inherited from the long shadow of the 70s.
[882.44 --> 889.30]  And what we're seeing now, ubiquitous connectivity with supercomputers on demand and rentable by
[889.30 --> 896.02]  the hour, and with now algorithmic capabilities that are far beyond what we'd ever conceived
[896.02 --> 897.08]  possible before.
[897.32 --> 903.08]  All those come together to create a new landscape that is completely different than sort of the
[903.08 --> 908.56]  Wintel duopoly kind of that's been sort of a monoculture that's persisted for 30 years
[908.56 --> 909.34]  in enterprise IT.
[909.88 --> 910.86]  We're now changing.
[910.86 --> 915.16]  And so it's at the point where these people with principal and senior and even the C-suite
[915.16 --> 920.16]  CIOs, they may not even remember like what it was like when they were cutting their teeth
[920.16 --> 922.82]  in the early 90s when they were like individual contributors.
[923.26 --> 925.32]  But we're now back in one of those modes.
[925.82 --> 929.38]  You think deploying onto a variety of different serverless and Kubernetes container things is
[929.38 --> 929.64]  hard.
[930.04 --> 932.78]  Think about all the different kinds of sensor platforms for industrial automation.
[933.50 --> 937.86]  Think about when you have to deploy models that then take sensor input, make inferences,
[937.86 --> 944.06]  tweak models, and then actually have a cybernetic control loop remote from the big iron computer.
[944.46 --> 947.10]  How do you even unit test something like that, right?
[947.36 --> 950.06]  Like first you got to get the code running and then you got to make sure the code's correct.
[950.32 --> 953.52]  How do you do those two basic things in that kind of deployment target?
[954.00 --> 956.78]  But you can't not because all your competitors are doing that, right?
[957.06 --> 959.22]  So we're entering this era of cybernetics.
[959.30 --> 960.72]  We're just the very beginning of it.
[961.06 --> 966.74]  And it's going to be completely different and so much more heterogeneous than the era of just
[966.74 --> 969.88]  personal computing, which settled up pretty quickly into x86.
[970.22 --> 972.00]  I mean, it was x86 versus Mac, right?
[972.26 --> 973.38]  And PowerPC and the Mac.
[973.60 --> 979.20]  But it's mostly x86 and Windows and DOS on the business computing side.
[980.02 --> 981.90]  And it's a sea change.
[982.20 --> 984.14]  So the changes will continue until morale improves.
[984.14 --> 1005.34]  We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1005.48 --> 1006.48]  Start with Google Chrome.
[1006.70 --> 1010.42]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1010.62 --> 1011.50]  Rip out the Google bits.
[1011.62 --> 1012.26]  We don't need them.
[1012.26 --> 1015.14]  Mix in ad and tracker blocking by default.
[1015.42 --> 1018.12]  Quick access to the Tor network for true private browsing.
[1018.48 --> 1022.82]  And an opt-in reward system so you can get paid to view privacy-respecting ads.
[1023.04 --> 1026.76]  Then turn around and use those rewards to support your favorite web creators like us.
[1027.08 --> 1031.68]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1031.68 --> 1060.74]  So, Peter, one of the things you mentioned was this question that you added in this year about how maybe budgets around data science have changed within a business due to changes related to the pandemic and all of the global things that are going on.
[1060.74 --> 1061.74]  What were the results there?
[1061.74 --> 1062.36]  What were the results there?
[1062.36 --> 1064.08]  And what are some of your thoughts on those?
[1064.30 --> 1064.46]  Yeah.
[1064.64 --> 1068.14]  So about a third of the folks said that their businesses decreased the investment.
[1068.52 --> 1070.22]  A quarter said the investment stayed the same.
[1070.50 --> 1072.32]  And a quarter said that investment increased.
[1072.56 --> 1075.24]  And then the remaining like, what, 12, 13% said they were not sure.
[1075.24 --> 1083.24]  So the majority of people seems like their business kept their data science spend, you know, at the same level or increased.
[1083.38 --> 1087.40]  But a third definitely did say that their businesses decreased investment.
[1087.76 --> 1087.86]  Yeah.
[1087.86 --> 1096.90]  And I mean, for my organization, it was like as soon as the pandemic hit, I mean, my organization deals with language related issues all around the world.
[1096.90 --> 1109.10]  And all of a sudden that became really, really difficult and prioritized at the same time, because now we've got all of this health information that needs to go all around the world in all of these different languages.
[1109.10 --> 1110.82]  People are more at home.
[1110.96 --> 1115.58]  So maybe connecting to them digitally is more important than in other venues.
[1115.80 --> 1123.50]  So I don't know how those translated across industries, but I definitely heard a lot of people saying, oh, I'm like, we're busier than ever.
[1123.92 --> 1129.20]  I don't know if that's because like, you know, it could be because they have less people to do the work.
[1129.20 --> 1140.52]  But I'm guessing it's because some of these issues around the data science really addresses well are those issues that, you know, are related to some of the things going on in the world.
[1141.06 --> 1142.16]  So, yeah, I don't know.
[1142.24 --> 1156.82]  Do you hear those sorts of stories at Anaconda about people using Anaconda to really address some of these issues and actually, you know, solving some of these complicated issues that we've been faced with uniquely over this past year?
[1156.82 --> 1159.82]  Yeah, I mean, it breaks down the way you phrased the question, right?
[1159.90 --> 1164.58]  One could say, well, some of the complicated issues are specifically medical in nature, right?
[1164.60 --> 1172.18]  So in the area of genetic research and pharma and sciences and all that, the Python data stack comes with Python scientific stack, right?
[1172.44 --> 1174.14]  So that stuff gets used all over those places.
[1174.26 --> 1179.86]  So there's sites that track like the evolution of the genome of SARS-CoV-2, coronavirus 2.
[1180.18 --> 1183.78]  And that site uses a number of the open source tools in our toolbox.
[1183.78 --> 1188.20]  And there's just so many, you know, epidemiological studies and all these other things.
[1188.68 --> 1191.20]  So those are areas that our stuff gets used in.
[1191.26 --> 1192.30]  And we see them mentioned.
[1192.42 --> 1194.12]  We see references or, you know, shout outs on Twitter.
[1194.42 --> 1210.46]  But the broader thing from an industry perspective, I think you make a good point that some businesses, they saw an opportunity to shift their business model to accelerate certain things that are digital in nature, digital engagement being one of those areas where it's like, yeah, you're going to have to do that or not have any engagement, right?
[1210.46 --> 1211.38]  Because everyone's locked down.
[1211.38 --> 1220.02]  So those areas were areas that then by its very nature of being a digital engagement, it creates so much data exhaust, right?
[1220.38 --> 1222.60]  And so then, of course, you want to analyze that.
[1222.68 --> 1226.62]  And of course, you would use that to feed back into improving the product and increasing engagement.
[1227.20 --> 1231.98]  So there is a natural kind of baseline, I would say, tailwind for some of that stuff.
[1231.98 --> 1234.64]  But we are used across a lot of industries.
[1234.82 --> 1243.92]  And so there's classic industry or not classic, brick and mortar or more sort of physical domain businesses where, yeah, their businesses were, unfortunately, negatively impacted.
[1244.08 --> 1245.14]  And there just wasn't budget available.
[1245.24 --> 1253.14]  So they had to cut some staff or we did drill in and ask, you know, if your organization decreases investment, in what way did it do so, right?
[1253.14 --> 1255.88]  And half the people said, well, we just lost some budget.
[1256.06 --> 1257.84]  Half the people said our team didn't grow.
[1258.40 --> 1261.30]  40% of people said, yeah, we actually laid off some people.
[1261.70 --> 1269.10]  And then about a third said that they had various project timelines put on hold indefinitely or for some extent period of time.
[1269.24 --> 1271.90]  So that's kind of the way that that came down.
[1272.36 --> 1281.96]  But on the exact flip side, the people whose organizations increased investment, they had increased budget, they were actively hiring, they had way more projects and additional projects, and they could buy more tools.
[1281.96 --> 1284.52]  So maybe there's not any information there.
[1284.90 --> 1286.30]  It's kind of what you'd expect, right?
[1286.74 --> 1302.30]  What I'm hearing you describe, if I'm right, is kind of innovation being driven by the circumstances of this bizarre last year and a half that we've had, where people are recognizing that they are in a constrained environment, and they can either rise to it or not.
[1302.30 --> 1307.44]  I know it wasn't a specific question you're asking, but do you think there might have been any of that in the response?
[1307.58 --> 1318.98]  Like the organizations that are seeing big results from data science in a productive way probably are investing, they're innovating, they're saying, if we can't go to the office, we're going to find better ways of doing data.
[1319.04 --> 1320.02]  We're going to change our workflows.
[1320.22 --> 1324.32]  We're going to change our pipelines and bring value to our customers in a different way.
[1324.32 --> 1331.44]  Do you think there's any correlation between that kind of innovation-driven mindset and levels of investment or lack thereof?
[1331.56 --> 1333.10]  And you can speculate as well.
[1333.48 --> 1333.88]  Yes.
[1334.02 --> 1342.66]  I would say speculatively, based on the anecdotes and data that I have, I think there's some paths that you could see people going down, right?
[1342.66 --> 1352.56]  So if it's a business that's just dabbling or just getting started with using data science techniques, you could sort of see it like, oh, this was kind of a, it was an elective or sort of experiment.
[1352.82 --> 1355.50]  And we just don't have an experiment budget this year, so I'm sorry, right?
[1355.60 --> 1357.06]  And we decreased our investment there.
[1357.48 --> 1368.04]  For others, the attitude generally that I saw in business was everyone kind of initially, at least in the Q2 to Q3 timeframe, that summer timeframe, everyone was sort of holding their breath to see what would happen.
[1368.52 --> 1371.30]  But no one really thought it was going to be literally the end of the world.
[1371.30 --> 1384.18]  It was clear we're going to have to get through it, and we'd find new modalities of working, of feeding people, of just being, whether it was pod schools or whether it was, you know, camping space 20 feet apart or something.
[1384.46 --> 1385.80]  People were finding out new ways to live.
[1385.90 --> 1390.06]  So with that mentality, businesses recognize that they're going to be data-driven.
[1390.46 --> 1394.02]  It's just which projects should they put those data scientists on, right?
[1394.02 --> 1406.80]  So if you have some data scientists who've done some work and they're familiar with the business and your data structures and your data management, it didn't make sense to let them go only to onboard new people nine months down the road that they have no clue, right?
[1406.90 --> 1413.56]  So I think in this way, it was more of a, that would explain the 25% where they were just like on hold, right?
[1413.60 --> 1415.22]  Hey, keep doing some of these things that we know are critical.
[1415.78 --> 1419.02]  Let's not greenlight any new projects till we see kind of how this thing lands.
[1419.02 --> 1422.90]  That's kind of the anecdata that I would say, speculatively, that I saw.
[1422.90 --> 1433.00]  Something you mentioned a little while back was a focus on understanding why and how it's hard for people to get things into production.
[1433.24 --> 1447.76]  Maybe seeing some trends and some discussions, and I've even seen some, you know, over the past few months, blog posts and other things talking about, hey, you know, we're however long into this data science and AI thing, and it's so hard to get things into production.
[1448.10 --> 1448.18]  Right.
[1448.18 --> 1457.46]  So I don't know what you asked specifically in the state of data science survey, but maybe you could share with us some of your thoughts on that front.
[1457.52 --> 1459.34]  I mean, we have been doing this for so long.
[1459.60 --> 1466.50]  Is it all due to those sort of complicated environments and targets that we're deploying to, or are there other things at play here?
[1466.96 --> 1468.10]  There are other things.
[1468.34 --> 1470.42]  So we gave people a list of options.
[1470.42 --> 1472.40]  They could check one or more of the things.
[1472.66 --> 1477.02]  And then when we looked at the data, we faceted it based on the people's roles.
[1477.02 --> 1487.74]  So the most sort of the leading or most popular answers for folks were 27% of people said meeting IT security standards.
[1487.74 --> 1490.26]  That was the most popular of all the responses.
[1490.46 --> 1497.70]  There was no single one that was the biggest among all cohorts, but that one was the most common and it certainly had the highest ranking.
[1497.70 --> 1507.66]  And then right after that, at 24%, 24% of respondents said recoding models from Python and R to another language was a roadblock to production.
[1507.98 --> 1511.04]  And then 23% said managing environments and dependencies.
[1511.04 --> 1514.90]  23% said recoding models from another language into Python and R.
[1515.66 --> 1519.32]  So this like language recoding thing is interesting.
[1519.90 --> 1525.50]  I mean, I caught wind of this stuff eight years ago when Python wasn't taken seriously as a production language.
[1525.50 --> 1528.92]  And people were like, well, it's a scripting language and we're a serious Java shop.
[1529.28 --> 1531.54]  You must recode all of your scikit-learn and some Java stuff.
[1531.96 --> 1534.00]  And so, you know, I was aware of this kind of thing going on.
[1534.00 --> 1541.20]  But for 23% of the respondents to say, no, no, this is a problem we have at our organization, that seemed large to me.
[1541.46 --> 1543.06]  I'd like to ask you a question about that.
[1543.12 --> 1548.60]  Like Daniel, I cross both in the data world and in more of the software development world.
[1548.84 --> 1552.86]  And we see like Python owns the data side of things.
[1552.86 --> 1559.92]  And yet we see these other languages that have been on the rise for a while, Go and Rust and such, that are out there.
[1559.92 --> 1564.22]  And, you know, you see containers being in whole ecosystems being written in them.
[1564.42 --> 1572.06]  And I am finding in practice, there's this, I kind of move back and forth between my data mode and my software development mode.
[1572.06 --> 1575.34]  And there is that context shifting associated with that.
[1575.40 --> 1577.40]  And in some cases, performance shifting as well.
[1577.40 --> 1590.08]  And I, having snuck into your report before we got to this point and looked at your data, I was looking at the uptake on Go and Rust at the very bottom of that.
[1590.32 --> 1591.94]  You know, you know the graph I'm talking about?
[1592.00 --> 1592.22]  Yes.
[1592.22 --> 1593.16]  It was all the languages.
[1593.30 --> 1594.16]  All languages, right.
[1594.34 --> 1596.30]  And I was dismayed by that a little bit.
[1596.32 --> 1598.62]  I'm kind of wondering, and I'd love your insight.
[1598.80 --> 1602.00]  Are those two going to come together over time?
[1602.04 --> 1603.62]  Are you seeing that in the longer trend?
[1604.00 --> 1605.26]  Do you think they stay the same?
[1605.26 --> 1611.54]  And I just need to settle into the fact that we have specific purpose languages for specific functions and I need to own that.
[1611.68 --> 1614.12]  What would you advise me to do in my thinking going forward?
[1614.44 --> 1618.18]  There's definitely different families of languages trying to solve different kinds of problems.
[1618.54 --> 1622.72]  And every language design decision is a compromise from what I've seen.
[1623.00 --> 1630.86]  So as you start making collections of compromises that are coherent in some way, shape, or form, you mold a language for a particular set of use cases.
[1630.86 --> 1639.72]  Python, by making so many design trade-offs for readability, sort of ease of getting started and things like that, it was easy to get started.
[1640.00 --> 1644.62]  You know, a lot of people learned it and it sort of has this executable pseudocode thing, nature, which people like.
[1644.88 --> 1645.84]  And so it got that.
[1645.96 --> 1652.64]  And then there were another set of design decisions that said we should make the VM as simple as possible so we can integrate with C libraries.
[1652.78 --> 1654.96]  That's an important C and C++ interop was an important thing.
[1654.96 --> 1658.96]  Okay, well, that's a really, really big design decision to stick through for like 25 years.
[1659.34 --> 1671.34]  And if you do that, what happens is you end up being like one of the best languages to script or integrate or embed into a C, C++ runtime environment, which includes all of those like numerical libraries that people have been developing for forever.
[1672.08 --> 1678.74]  So, oops, you happen to be like a really great scientific computing and numerical language all of a sudden, even though you are not anywhere near.
[1678.80 --> 1683.76]  I mean, Python was designed to be a more friendlier bash, you know, and maybe slightly more readable Perl.
[1683.76 --> 1689.90]  And so these collections of design decisions sort of put you into a particular niche or maybe a very large niche.
[1690.36 --> 1698.90]  And so when you look at the design decisions behind Go and Rust, right, there are very sharp pointed opinions as to, you know, Rust is about that type safety.
[1699.00 --> 1701.98]  Like, let's not have any more buffer overflows on streams.
[1702.10 --> 1703.68]  Like, let's just not have that anymore, right?
[1704.16 --> 1706.02]  Surely we should get there in 2020.
[1706.02 --> 1716.20]  And so I think that design decision and optimizing for some of those usability and developer quality of life things, it puts you into a particular spot.
[1717.00 --> 1718.08]  Go, you know, it's different.
[1718.18 --> 1721.96]  Go is like, you know, we want to be multi-threaded out the wazoo, super fast spin up.
[1722.08 --> 1727.04]  And then we're going to vendor the world, make everything into a single binary, really big binary, but a single binary.
[1727.46 --> 1731.00]  So there's just different design decisions that puts you into different places.
[1731.00 --> 1743.34]  And for that reason, I think that it is more likely in the future for these things to interrupt with each other over APIs or over data sets or maybe over shared data abstractions like Arrow or things like that.
[1743.58 --> 1749.32]  That's probably the more likely long-term scenario because it's about separations of concern of who's writing the code.
[1749.80 --> 1757.32]  The person writing the infrastructure code to spin up kernels and containers and manage all these kind of low-level system things, their boundary of concern kind of ends there.
[1757.32 --> 1760.46]  Once you have a use land process running, they don't really care what you're running in it.
[1760.72 --> 1763.92]  So they're going to write their infrastructure stuff and go, and it's going to be tight, fast.
[1764.06 --> 1767.00]  It's going to be like, you know, all this great stuff that Go or Rust offers.
[1767.60 --> 1773.00]  But once you get up here into numerical data science, I don't know what I'm doing, but I'm running a data script in Jupyter Notebook kind of land.
[1773.40 --> 1778.36]  Then use abilities of usability and then, you know, like the iteration cycle of trying different ideas.
[1778.62 --> 1781.96]  All of that becomes a dominant concern and it's a different design space, right?
[1781.96 --> 1790.18]  There's one other tiny little thing I wanted to append on is you mentioned the concern about putting models into other languages for deployment purpose, for production.
[1790.42 --> 1791.14]  Recoding them.
[1791.36 --> 1793.10]  Could you address that a little bit real quick?
[1793.22 --> 1794.18]  Yeah, recoding them.
[1794.42 --> 1800.44]  Literally taking Python code and saying, nope, we as a shop are not going to deploy Python into production.
[1800.68 --> 1806.56]  You have to rewrite this in C++ or you have to rewrite this in Java or .NET or maybe Rust or Go.
[1806.82 --> 1808.44]  I have heard of some things being recoded in Go.
[1808.44 --> 1816.66]  So I think the C++ thing is a lot of TensorFlow happens to go that way because it has a C++ API as well as the Python one.
[1816.76 --> 1817.84]  Has a Go one too, actually.
[1818.06 --> 1818.36]  Yes.
[1818.92 --> 1819.54]  Okay, right.
[1819.66 --> 1820.36]  For inference.
[1820.54 --> 1821.16]  Yeah, yeah.
[1821.24 --> 1824.80]  Because the inference stuff is so much like it's more lightweight, right?
[1824.82 --> 1824.94]  Yeah.
[1824.96 --> 1826.84]  So there's no reason you can't have a lot of front ends for that kind of thing.
[1826.94 --> 1831.32]  So I think that recoding, I don't think anyone relishes having to do it.
[1831.50 --> 1834.40]  Hence, it's considered a roadblock, but it's a thing that people are doing.
[1834.58 --> 1835.56]  And it's something we should be thinking about.
[1835.60 --> 1836.98]  How do we make it so people don't have to do that?
[1836.98 --> 1838.52]  What are the issues?
[1838.62 --> 1840.12]  Is it that they don't know?
[1840.28 --> 1845.04]  IT does not really know how to deploy Python in a safe way that they can manage, right?
[1845.10 --> 1853.36]  Some of our products certainly help with that, trying to give people a good governed vendor of record to give them signed binaries they can deploy to production.
[1853.76 --> 1855.30]  But that's only one of the hurdles.
[1855.72 --> 1856.90]  There may be others as well, right?
[1856.96 --> 1858.96]  Cultural knowledge gaps, things like that.
[1858.96 --> 1863.56]  Just to follow up on that previous discussion about recoding models into other languages.
[1863.56 --> 1867.16]  Do you find speed of execution, efficiency, latency?
[1867.38 --> 1870.32]  These are sorts of things that people are quoting.
[1870.74 --> 1876.24]  And I wonder that because I often wonder myself, like, am I really good at writing fast Python?
[1876.24 --> 1878.40]  I'm not really sure I am.
[1878.50 --> 1886.62]  Like, I'm good at writing fast Python in the sense of, like, I can code something up super quick and get it to execute, like, end to end.
[1886.88 --> 1890.04]  But the execution might be really slow.
[1890.46 --> 1891.54]  So I don't know.
[1891.60 --> 1901.90]  Do you see that as a trend in terms of, like, because I'm thinking, like, if people are recoding their things into C, C++, you know, maybe they have that on their mind or something.
[1902.32 --> 1906.02]  That's certainly one of the concerns is performance aspect of it.
[1906.16 --> 1914.34]  When it comes to, you know, the numerical computing stuff in Python, the code, once it gets to the numerical part, it tends to run pretty darn fast.
[1914.78 --> 1918.18]  I mean, you can maybe improve it a little bit, but that's not where your bottlenecks are.
[1918.18 --> 1928.24]  If you have a lot of pure Python code moving things around and you're passing a lot of data back and forth and you're accidentally taking lots of memory as you move things around, then that's where you get slowdowns.
[1928.30 --> 1931.66]  But the core algorithms themselves are tightly optimized Fortran or machine code.
[1931.90 --> 1936.46]  And it's interesting, you know, you are a data scientist and you might be concerned about performance.
[1936.46 --> 1947.58]  But when we look deeper at the respondents and we facet by job, the data scientists are not the ones that predominantly identify recoding models as being a roadblock to production.
[1948.14 --> 1953.76]  Data scientists, among data scientists, that is the next to least popular concern.
[1953.76 --> 1960.38]  The biggest concern the data scientists had was a skills gap in their organization, whether it's data engineering or Docker or something like that.
[1960.38 --> 1966.58]  And then managing environments dependencies and then meeting IT security standards is another one.
[1966.66 --> 1967.70]  Getting access to compute resources.
[1967.82 --> 1968.88]  Those are all the things.
[1969.30 --> 1972.12]  Recoding models wasn't their big blocker.
[1972.44 --> 1975.00]  I'm just curious which role is most important about that.
[1975.00 --> 1977.58]  What's really interesting is it's the ops role.
[1977.72 --> 1981.98]  So cloud engineer, cloud security manager, cloud ops, MLOps people.
[1982.70 --> 1988.56]  When you look at the histogram of their responses of, you know, which things are impediments, all of them look the same.
[1988.98 --> 1997.28]  So if you're actually to do a cohort clustering based on the shape of the histogram of their pain points to production, all those four roles will look pretty much identical.
[1997.28 --> 2006.38]  And out of those four roles, MLOps, cloud ops, cloud security manager, and cloud engineer, for them, skills gap in the organization was the least of their concerns.
[2006.78 --> 2009.56]  You know, whereas that was the biggest concern for data scientists, that's the least concern for them.
[2009.86 --> 2015.04]  For them, the biggest roadblock to production was recoding models from Python and R to another language.
[2015.04 --> 2029.24]  So when you say the skills gap bit, is that the perception of the skills that I have in my role are either in deficit in our organization or inversely the people on the ops side are saying we have that?
[2029.48 --> 2030.60]  We were not specific in that.
[2030.72 --> 2034.72]  The little one-line response you could check there was a skills gap in my organization.
[2034.72 --> 2045.00]  And we didn't ask if it was a skills gap, like they need more of me in the organization, or if the organization or if my data science team needs more of this kind of expertise.
[2045.20 --> 2051.46]  We just left it kind of open, I guess, to interpretation to say talent and skills gap is the biggest impediment.
[2051.46 --> 2060.80]  And my read on this is that these folks who are in the MLOps, MLOps engineering kind of roles, they kind of know what they need to do.
[2060.80 --> 2066.82]  So in their organization, in the IT organization usually is where they're housed, they kind of know what they need to do.
[2066.90 --> 2067.58]  They got the skills.
[2067.74 --> 2070.94]  It's just a huge pain in the butt to do some of these things that they have to do.
[2071.88 --> 2076.92]  Chief among them, recoding models from Python and R into other languages or vice versa.
[2077.02 --> 2078.46]  Those two are the top concerns.
[2079.10 --> 2086.12]  And what's really interesting is we also ask people, because it's a hot hiring market right now, we ask people, what is your job satisfaction, right?
[2086.26 --> 2088.40]  How long do you plan to stay with your current employer?
[2088.40 --> 2093.80]  And the MLOps, the Cloud Ops, Cloud Engineer folks, those are the least happy.
[2094.26 --> 2101.30]  They're the ones where I believe three quarters are saying that they're going to be looking for a new job in six to 12 months.
[2102.20 --> 2109.18]  So maybe the moral of the lesson there is the more you make your people recode models from one language to another, the more likely they are to churn.
[2109.44 --> 2112.66]  Or it could also be that that's just a really in-demand role and skill set.
[2112.66 --> 2126.14]  But that being said, you know, if they feel like that recoding thing is a impediment and it's like a frustration for them in their job, and also they're a very in-demand skill set, you should maybe think of other ways to make them happy to retain them.
[2126.50 --> 2128.94]  So anyway, that was another really super interesting find.
[2129.00 --> 2129.72]  I mean, it was stark.
[2130.02 --> 2130.96]  No other role.
[2131.36 --> 2132.36]  No other sets of roles.
[2132.40 --> 2133.74]  You think data scientists are in demand.
[2134.20 --> 2135.30]  Maybe there's a higher thing there.
[2135.30 --> 2142.52]  No, data scientists, they're 50% of them are like, yeah, I'm either here for the foreseeable future or I might start looking in two to three years.
[2143.00 --> 2143.36]  50%.
[2143.36 --> 2150.44]  But when it comes to the ML Ops and Cloud Ops folks, 3% said that they would stay at their current firm for the foreseeable future.
[2150.84 --> 2156.78]  Another 25% to 30% said they will start looking in two to three years and the rest of them were all within the next six to 12 months.
[2157.06 --> 2157.86]  Or I'm currently looking.
[2158.00 --> 2158.56]  That's crazy.
[2158.56 --> 2168.82]  So you mentioned this sort of contrast between what the data scientists were concerned with and what these cloud ML Ops, data ops people were concerned with.
[2169.04 --> 2173.68]  On that spectrum was this element of efficiency and also recoding models.
[2174.30 --> 2183.72]  I know if I'm not wrong, Anaconda has some sort of recent news in terms of some things related to optimized Python and efficiency.
[2184.14 --> 2185.52]  You want to share that with the listeners?
[2185.88 --> 2186.40]  Yeah, yeah.
[2186.48 --> 2187.44]  It's very exciting news.
[2187.44 --> 2190.50]  We just announced that basically we have hired the Piston team.
[2191.00 --> 2197.46]  And for those who don't know, Piston is an open source alternative Python interpreter that runs on your unmodified Python code.
[2197.60 --> 2201.28]  It can go 20 to 50% faster as an interpreter.
[2201.28 --> 2201.80]  That's crazy.
[2202.12 --> 2202.78]  Which is cool.
[2203.04 --> 2204.14]  Now it's Amdahl's law.
[2204.24 --> 2207.94]  So like what percentage of your code is pure Python code?
[2208.34 --> 2211.34]  And that's the percent that we would be squeezing kind of the air out of, right?
[2211.68 --> 2213.30]  The rest of it is a numerical code.
[2213.42 --> 2215.98]  Then Piston won't help very much because that's already quite optimized.
[2215.98 --> 2220.78]  And if you want to optimize that further to fuse loops or things like that, then you would use something like Numba.
[2221.12 --> 2225.96]  And in fact, it was really our Numba compiler project that led us down this path.
[2225.96 --> 2229.88]  We had many different kinds of users coming to us saying, hey, Numba's great.
[2230.06 --> 2232.60]  I want to do Numba for like my whole program.
[2233.32 --> 2235.28]  And we're like, no, that's not what it's for.
[2235.66 --> 2238.14]  It's there to hit like the hot numerical loops.
[2238.34 --> 2245.70]  It's to allow you to write Fortran-ish like element-wise stuff without having to go and break out like C extensions for NumPy, right?
[2245.70 --> 2247.42]  That's what Numba's good at.
[2247.78 --> 2253.14]  But then as we looked to see, can we extend some of the ideas in the Numba optimization toolkit?
[2253.40 --> 2255.46]  Can we extend those into broader program analysis?
[2255.84 --> 2257.72]  And then we realized that it's almost as a different project.
[2258.04 --> 2260.94]  And Piston is essentially a project in that vein, right?
[2261.00 --> 2265.18]  Can we just make the interpreter itself much faster at a lot of these common things that people do?
[2265.18 --> 2270.56]  And then there's a 1% or 2% improvement here, 1%, 2% there.
[2270.66 --> 2272.62]  You start shaving off 1% or 2% all over the place.
[2272.78 --> 2274.96]  And you can start making something that's quite fast.
[2275.26 --> 2279.18]  Again, without making people have to recode, rewrite any of their code.
[2279.34 --> 2280.74]  So we're really, really excited about that.
[2280.94 --> 2282.30]  And of course, it's an open source project.
[2282.64 --> 2284.04]  We're going to keep it open source.
[2284.40 --> 2285.58]  That's kind of how we do.
[2286.22 --> 2288.58]  And yeah, I'm really excited about the team and the really sharp guys.
[2288.58 --> 2291.10]  And we're really excited about what's to come.
[2291.24 --> 2291.62]  Congratulations.
[2292.02 --> 2292.36]  Thank you.
[2292.62 --> 2293.30]  Yeah, that's awesome.
[2293.30 --> 2298.30]  And for those listeners out there that maybe they're thinking they might want to try something
[2298.30 --> 2303.08]  with Piston, could you describe what do you have to change about your workflow as a Python
[2303.08 --> 2305.22]  developer to start utilizing Piston?
[2305.50 --> 2308.68]  How does it, where does it factor in and how does it change your workflow?
[2308.94 --> 2311.30]  Well, it is an alternative Python interpreter.
[2311.86 --> 2315.44]  So instead of typing Python, you type Piston.
[2316.08 --> 2320.98]  And so if you go to the website, it's Piston, P-Y-S-T-O-N.org.
[2321.08 --> 2322.16]  It's really, really simple.
[2322.16 --> 2327.06]  There's good docs there that basically you just run Piston on your code and there it
[2327.06 --> 2327.28]  is.
[2327.62 --> 2332.12]  So the goal of the project is to make it as easy as possible to just drop in a replacement
[2332.12 --> 2332.58]  interpreter.
[2332.96 --> 2335.54]  Now, of course, the elephant in the room is, well, what about all those wonderful extension
[2335.54 --> 2336.98]  modules that everyone loves to use, right?
[2337.44 --> 2342.66]  And so we are looking into what it takes to make sure that all of that is covered well
[2342.66 --> 2343.14]  as well.
[2343.34 --> 2346.50]  There is recompilation necessary for some of that stuff, but we're in a condo.
[2346.58 --> 2348.84]  We're pretty good at building libraries and compiling them.
[2348.84 --> 2352.82]  So, yeah, we're really excited about trying to deliver something very, very awesome there
[2352.82 --> 2353.24]  for people.
[2353.52 --> 2353.98]  That's so cool.
[2354.16 --> 2354.28]  Yeah.
[2354.34 --> 2357.34]  Really excited to follow that and try some things out on my own.
[2357.96 --> 2363.08]  So I guess to kind of close us out here as we're wrapping out the conversation, predicting
[2363.08 --> 2365.88]  the future, you know, you're always going to be wrong.
[2365.98 --> 2366.82]  That's my experience.
[2366.82 --> 2371.74]  But when you come back and see us next year for the State of the Data Science Report, any
[2371.74 --> 2374.48]  predictions for what we might be seeing over the coming year?
[2375.00 --> 2376.70]  Over the coming year?
[2377.34 --> 2377.64]  Wow.
[2377.76 --> 2377.88]  Yeah.
[2377.96 --> 2379.48]  Lots of interesting things.
[2379.60 --> 2380.46]  Lots of interesting things.
[2380.86 --> 2388.44]  I think that the information warfare and technological warfare between U.S. and China is going to start
[2388.44 --> 2393.22]  having the first few drops of rain are going to start hitting our ecosystem from that.
[2393.42 --> 2394.28]  I do believe that.
[2394.28 --> 2399.50]  I think that, well, depending on the amount of political capital the Biden administration
[2399.50 --> 2404.60]  has to spend on these things, I think regulation of tech is going to certainly, of course, have
[2404.60 --> 2409.46]  implications in our industry because so much of what people use these data processing tools
[2409.46 --> 2414.92]  for are around user behavior and data analysis of a lot of that kind of stuff.
[2414.98 --> 2420.22]  So I think as an industry, we're going to have to get more political sooner rather than
[2420.22 --> 2420.50]  later.
[2420.50 --> 2425.00]  Now, one of the other things that came out of the survey is that a lot of practitioners
[2425.00 --> 2427.04]  are concerned about ethics.
[2427.54 --> 2428.62]  They are concerned about bias.
[2428.98 --> 2430.54]  They're not naive about this, right?
[2430.62 --> 2435.26]  Their upstream business stakeholders and budget holders might be somewhat naive, but the heartening
[2435.26 --> 2439.98]  thing is that the practitioners, at least, fingers on keyboard folks, those folks are aware
[2439.98 --> 2441.74]  that it's garbage in, garbage out.
[2442.22 --> 2443.44]  Bias in, bias out, right?
[2443.44 --> 2450.14]  So I think we need to, as a industry, as a community, we should make sure we're constantly
[2450.14 --> 2452.46]  aware about that and that we're intentional about our practices.
[2452.92 --> 2457.32]  So I think over the next year, we're going to see incidents and we're going to see some
[2457.32 --> 2461.70]  of these kind of things that really force us to have a conversation around data management,
[2462.00 --> 2466.62]  privacy, bias, ethics, use of proprietary APIs, prediction, and what that means.
[2466.80 --> 2467.68]  A lot of these things.
[2467.96 --> 2468.12]  Yeah.
[2468.44 --> 2469.72]  That's what I think is going to happen over the next year.
[2469.72 --> 2477.18]  Well, if any of that does happen, you'll hear about it here on Practical AI next year.
[2477.36 --> 2478.10]  So stay tuned.
[2478.46 --> 2480.44]  Peter, it's always a pleasure to talk to you.
[2480.64 --> 2485.52]  Really appreciate you taking time and the work that Anaconda puts into not only this
[2485.52 --> 2489.80]  report, but to the Python and data science ecosystem in general.
[2490.08 --> 2490.70]  You're appreciated.
[2491.06 --> 2493.12]  And yeah, just want to pass along that.
[2493.26 --> 2494.96]  Thanks and keep up the good work.
[2495.22 --> 2495.58]  Absolutely.
[2495.98 --> 2496.68]  Thank you guys so much.
[2499.72 --> 2502.24]  Thank you for listening to Practical AI.
[2502.78 --> 2507.98]  We have a bundle of awesome podcasts for you at changelog.com, including our brand new
[2507.98 --> 2513.56]  show, Ship It with Gerhard Lezou, a podcast about getting your best ideas into the world
[2513.56 --> 2514.80]  and seeing what happens.
[2515.16 --> 2519.04]  It's about the code, the ops, the infra, and the people that make it happen.
[2519.34 --> 2523.06]  Yes, we focus on the people because everything else is an implementation detail.
[2523.40 --> 2528.12]  Subscribe now at changelog.com slash ship it or simply search for Ship It in your favorite
[2528.12 --> 2528.78]  podcast app.
[2528.78 --> 2529.36]  You'll find it.
[2529.50 --> 2532.76]  Of course, the galaxy brain move is to subscribe to our master feed.
[2532.88 --> 2538.14]  It's all changelog podcasts, including Practical AI and Ship It in one place.
[2538.48 --> 2543.22]  Search changelog master feed or head to changelog.com slash master and subscribe today.
[2543.68 --> 2548.42]  Practical AI is hosted by Daniel Whitenack and Chris Benson with music by Breakmaster Cylinder.
[2548.62 --> 2551.14]  We're brought to you by Fastly, Vaughn Starkly, and Linode.
[2551.48 --> 2552.14]  That's all for now.
[2552.36 --> 2553.30]  We'll talk to you again next week.
[2553.30 --> 2583.28]  We'll talk to you again next week.
