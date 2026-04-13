[0.00 --> 5.82]  you may be able to get more cards that are not linked with Envy Switch,
[5.82 --> 11.54]  but are like the later gen architectures that will actually perform faster
[11.54 --> 17.94]  than last generation top tier cards that are connected with Envy Link or Envy Switch.
[18.10 --> 18.84]  That's interesting.
[19.16 --> 23.46]  Yeah, so it's not just like if you're doing multi GPUs,
[23.48 --> 26.00]  you need this special interlink infrastructure.
[26.00 --> 31.92]  You kind of have to also weigh in the generation of cards that you're looking at,
[31.92 --> 36.92]  because like if you go down to one GPU on the Lambda benchmarks,
[37.12 --> 43.06]  you can see like that the 3090, which is a consumer card and is very cheap as far as car,
[43.32 --> 51.56]  you know, GPU cards go gets you halfway to the training on that throughput as the A100 that's listed there.
[51.72 --> 51.84]  Really?
[52.04 --> 55.16]  And so like that's pretty incredible, actually.
[55.50 --> 55.76]  Right.
[56.00 --> 56.44]  It is.
[58.38 --> 61.10]  Bandwidth for ChangeLog is provided by Fastly.
[61.40 --> 63.30]  Learn more at Fastly.com.
[63.52 --> 65.82]  Our feature flags are powered by LaunchDarkly.
[66.10 --> 67.90]  Check them out at LaunchDarkly.com.
[68.14 --> 69.98]  And we're hosted on Leno cloud servers.
[70.38 --> 73.92]  Get $100 in hosting credit at Leno.com slash ChangeLog.
[75.92 --> 80.84]  ChangeLog++ is the best way for you to directly support practical AI.
[80.84 --> 85.74]  Join today and unlock access to a private feed that makes the ads disappear,
[85.94 --> 91.74]  gets you closer to the metal and help sustain our production of practical AI into the future.
[92.46 --> 100.62]  Simply follow the ChangeLog++ link in your show notes or point your favorite web browser to ChangeLog.com slash plus plus.
[100.62 --> 105.00]  Once again, that's ChangeLog.com slash plus plus.
[107.00 --> 108.76]  ChangeLog++ is better.
[108.76 --> 124.68]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[124.68 --> 129.10]  This is where conversations around AI, machine learning, and data science happen.
[129.34 --> 134.10]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash community.
[134.48 --> 135.44]  And follow us on Twitter.
[135.60 --> 137.22]  We're at Practical AI FM.
[137.22 --> 148.90]  Welcome to another fully connected episode of Practical AI.
[149.32 --> 154.98]  This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[155.26 --> 159.98]  We're going to take some time to discuss some of the latest AI news that we've run across.
[160.20 --> 164.68]  And we'll dig into some learning resources to help you level up your machine learning game.
[164.68 --> 171.88]  I'm joined as always by my co-host Chris Benson, who is a principal emerging technology strategist at Lockheed Martin.
[172.24 --> 175.80]  And I'm Daniel Whitenack, a data scientist at SIL International.
[176.16 --> 177.56]  How are you doing today, Chris?
[178.06 --> 179.36]  I am doing very well.
[179.66 --> 186.08]  We are kind of surviving the last bits, I think, of winter as a winter storm blows across the nation.
[186.42 --> 191.02]  Yeah, it's a crazy time here in the U.S. weather-wise.
[191.02 --> 195.96]  So for those maybe international listeners, you may have heard about it, may not have.
[196.04 --> 199.64]  There's been a lot of winter storms in the U.S. lately.
[199.96 --> 205.86]  So for those listening in the future, we're in February of 2021.
[206.74 --> 215.78]  And so I know further south, some places in the U.S., they're getting like weird, you know, freezing rain and that sort of things.
[216.12 --> 219.56]  Texas is having like the worst weather in decades right now.
[219.56 --> 222.40]  Yeah, so they don't have and I mean, I get it.
[222.44 --> 232.22]  They don't have sort of any infrastructure in terms of like plow trucks and big stockpiles of ice or salt to put on the ice on the roads.
[232.46 --> 235.64]  So it's yeah, it's just a giant disaster in there.
[235.72 --> 240.08]  It's so odd for that area that nothing is prepped, you know.
[240.34 --> 248.68]  People further up north, I mean, we got so where I'm at, we got probably between a foot and a half of snow, which is a lot for here.
[248.68 --> 251.38]  But we also, you know, there's always snow.
[251.52 --> 261.60]  So we have snow plows and, you know, they were working long hours, but it wasn't like they didn't know, you know, it didn't have that stuff in place and all that.
[262.10 --> 267.86]  And here in the usually warm south, we do not have snow on the ground, but we actually did see flurries.
[268.08 --> 268.42]  Wow.
[268.52 --> 268.94]  There you go.
[268.94 --> 271.70]  And speaking of snow plows, you know, that's such a rare.
[271.94 --> 276.46]  I think I'm more likely to see a living dinosaur rumbling by than a snow plow.
[276.56 --> 280.24]  I think we can count the number of snow plows we have in our state on my two hands.
[280.60 --> 282.20]  So yeah, not many.
[282.80 --> 283.04]  Yeah.
[283.04 --> 290.24]  And, you know, it's I've got a few aches and pains right now from from shoveling myself.
[290.24 --> 292.88]  But that was a good, good workout, I guess.
[293.52 --> 293.80]  Yeah.
[293.90 --> 298.64]  You know, you got the cap on, you know, I know listeners can't see, but got the winter cap on everything.
[298.64 --> 300.72]  You're looking you're looking good and rugged there.
[300.88 --> 308.34]  Well, that's because I have right now I have my recording set up in like the back area of our house, which is the furthest from the furnace.
[308.34 --> 309.74]  It's also really cold here.
[309.90 --> 313.88]  And so the hot air like generally doesn't make it to this side of the house.
[314.12 --> 314.52]  Gotcha.
[314.94 --> 320.04]  So, yeah, it's one of one of those things that's just a practicality.
[320.70 --> 328.70]  Yeah, we're at least up in the 40s, which while is while being fairly cold for us is is downright tropical compared to the rest of the country.
[329.44 --> 329.62]  Sure.
[329.80 --> 330.04]  Sure.
[330.16 --> 330.84]  Yeah, it is.
[331.24 --> 334.56]  Yeah, it's one interesting thing after another.
[334.56 --> 340.64]  But things have been going pretty well work wise, got a lot of interesting things to work on.
[340.80 --> 346.92]  And as a principal emerging technology strategist, which, you know, is always a great title to say.
[347.66 --> 348.94]  It's a long title.
[349.06 --> 350.04]  It is a long title.
[350.40 --> 355.56]  I think we talked once that your title could be acronym PETS.
[356.34 --> 357.06]  P-E-T.
[357.20 --> 357.88]  Yeah, that's right.
[358.10 --> 359.70]  And that, which is very fitting.
[360.24 --> 361.32]  Yeah, yeah, very fitting.
[361.32 --> 365.44]  So what emerging technologies are on your mind as of late?
[366.22 --> 375.74]  Well, you know, there are actually a lot of really cool, you know, with with the fact, you know, noting for people who may listen to this down the road that we are still in the middle of a global pandemic.
[376.04 --> 376.18]  Right.
[376.18 --> 385.46]  Though maybe on the tail end as vaccines are beginning to roll out, you know, there has been quite a lot of interesting research in the in the medical space.
[385.46 --> 388.56]  And there's a lot of AI being used at this point.
[388.66 --> 398.14]  You know, we talked early on about how there were some uses for AI for data sets regarding pandemic, but we haven't really addressed it in many, many months at this point.
[398.14 --> 409.10]  And since then, I've seen I've seen quite a lot of deep learning being applied to various medical and health concerns, some pandemic related and some not.
[409.28 --> 411.62]  So it's really turned the corner in that space.
[412.12 --> 413.58]  Yeah, that's super interesting.
[413.58 --> 436.28]  Obviously, you know, there's going to be a lot of a lot of applications in health care, both, you know, for new processes, new technologies, new applications of AI spurred on by this pandemic, which is sort of shown in a lot of ways how unprepared we are for for certain certain scenarios.
[436.28 --> 440.64]  Those I'm sure that will prompt that pain will prompt a lot of people to innovate.
[440.64 --> 466.14]  And it's always an interesting one for AI in the health care space, because, of course, there's all sorts of privacy concerns with data and, you know, interesting scenarios where you have ideas about how to apply AI, maybe, you know, to detecting certain patterns and medical imagery in lungs to, you know,
[466.14 --> 470.66]  detect COVID related outcomes or something.
[471.20 --> 475.24]  But how are you going to get that imagery to develop those models?
[475.50 --> 476.12]  That's a good point.
[476.24 --> 479.94]  And we had an episode very recently having to do with radiology and imagery.
[480.44 --> 482.26]  So I would refer people back to that.
[482.32 --> 485.46]  I'll get the specific episode number and put it in the show notes.
[485.54 --> 486.68]  So it's only been a couple back.
[486.90 --> 492.84]  And then today, as we address some of the things for those who have not listened to Fully Connected, it's Daniel and I.
[493.16 --> 494.00]  We don't have a guest.
[494.00 --> 498.38]  We're just talking about things that we've noticed in the news, kind of catching up on this.
[498.52 --> 501.00]  So it's a very organic conversation.
[501.36 --> 501.90]  Yeah, yeah.
[501.96 --> 517.76]  And one of the things I was going to mention was I saw an article having to do with CAT scans and the fact that there are, without getting deeply into the medical side of it, there are different grades of CAT scans, if you will, with different utilities associated with that and different costs.
[517.76 --> 531.80]  I noticed that there was an article about using deep learning models to take certain types of images and increase their fidelity so that they're more useful in that thing without, you know, kind of diving right into the topic here.
[532.30 --> 537.78]  So basically, you're saying you take the cheap CAT scan and make it a expensive CAT scan.
[537.80 --> 538.58]  To some degree, yeah.
[538.58 --> 540.48]  Sort of, is the idea.
[540.48 --> 543.78]  Yeah, I think that is more or less along the right ways.
[543.88 --> 544.94]  I'm going to pull it up.
[545.14 --> 552.16]  They actually took ResNet and they're transforming a – and I am not a medical person, so I'm just kind of reading this little blurb off.
[552.28 --> 557.22]  But a clinical single-spectrum CT image to VM counterparts.
[557.22 --> 569.74]  And as I understand it, the VM part, hopefully – I know we have some doctors in the audience and they can offer some comments after the fact, but the VM refers to virtual monoenergetic.
[570.04 --> 571.76]  Yeah, I have no idea what that means.
[571.98 --> 572.68]  I don't either.
[573.32 --> 581.54]  But as I read the article, I was just kind of like, you know, apparently they are able to do some enhancement with this at different energy levels and stuff.
[581.54 --> 586.24]  And I don't know that that's revolutionary in today's because we've talked about imagery a lot.
[586.42 --> 593.72]  But I think it's really notable that when, you know, a while back when we were talking about these things as we first saw them, they were very cutting edge.
[593.88 --> 596.92]  And now it's becoming almost commonplace.
[597.16 --> 606.80]  And I think that's the thing going into this episode that I was thinking about was just how incredibly commonplace deep learning model deployments have become.
[606.80 --> 619.48]  There is sort of a general trend of utilizing lots of low-fidelity or lower-resolution or noise-filled data.
[619.68 --> 628.70]  So using lots of that data to get really good results versus using small amounts of really high-resolution, high-fidelity data.
[628.70 --> 643.08]  I was just hearing on the radio, one of the shows I was listening to, I think the company or the technology they were talking about was persistent surveillance, which this is a more, you know, creepy sort of side of this.
[643.22 --> 656.44]  But essentially, they're just saying, well, you know, we're not going to surveil, like, certain areas in front of a store or somewhere that are maybe, like, where crime is going to happen.
[656.44 --> 664.50]  Because basically, if you put cameras around that have good resolution, you're kind of expecting to, you know, you're going to put them in the best spots, right?
[664.52 --> 666.10]  Because that equipment is expensive.
[666.44 --> 686.22]  So they're on the whole other side of things where they're basically saying, well, let's just fly a drone around constantly in, like, over some city and basically have a whole bunch of low-resolution video of essentially everywhere.
[686.22 --> 689.44]  So they're not capturing things with enough resolution.
[689.44 --> 697.20]  And I think what they're saying is they're not capturing things with enough resolution to, like, identify people in, you know, the video.
[697.32 --> 702.66]  So they can't, like, say this is you or whatever, although they probably can in, like, in certain ways.
[703.06 --> 704.30]  There's always ways.
[704.54 --> 705.38]  I have no comment.
[705.52 --> 707.80]  But, you know, that's what they're saying.
[707.88 --> 708.80]  There's a lot of noise.
[708.94 --> 709.64]  It's low resolution.
[709.64 --> 714.70]  So they're saying, you know, we're not, like, tracking your face or, like, your identity.
[715.08 --> 730.48]  But if something were to happen, like, let's say there was a shooting in a certain area or something, they could basically replay to that specific area and, like, see the little blobs of people moving around and, like, you know, say, oh, no, this guy did come out of this door.
[730.56 --> 732.28]  And then this happened and whatever.
[732.28 --> 740.34]  Of course, that's, like, alarming and interesting in so many different ways that we probably don't have time to talk about it.
[740.44 --> 754.84]  But it's also, like, an example, like, where the mindset was typically, like, I just need to get better and better resolution surveillance cameras or something to be able to really capture everything, every detail in my surrounding.
[754.84 --> 763.24]  They're sort of, like, flipping that and saying, no, just get really low resolution imagery but a whole bunch of it.
[763.68 --> 769.90]  It's the many imperfect considerations that go into the entire field now of AI ethics.
[770.30 --> 770.46]  Yeah.
[770.74 --> 771.44]  And it's funny.
[771.50 --> 772.62]  I've seen so many articles.
[772.92 --> 776.74]  And for a while, as listeners may know, I was working directly in that field.
[776.80 --> 778.46]  And I no longer am in a direct way.
[778.80 --> 779.62]  But I still follow.
[779.62 --> 789.26]  And it's so complicated in terms of there are so many use cases and you're trying to figure out and, you know, people will look at something that's a little bit more clear cut like the Chinese system.
[789.80 --> 791.18]  The social credit system.
[791.26 --> 799.98]  The social credit system where they're actively monitoring citizens or anyone for that matter and actively recognizing who they are and all that.
[799.98 --> 807.12]  And so, you know, it is a level of surveillance that most people in the West are not at all comfortable with.
[807.70 --> 810.82]  Nor would I be, nor would you be from previous conversations.
[810.82 --> 817.50]  And but, you know, there's clearly benefits to doing such surveillance.
[817.50 --> 819.92]  So, you know, how much is enough and too much?
[820.16 --> 820.64]  Yeah.
[820.76 --> 821.76]  I think that's the thing.
[821.92 --> 829.38]  Like, the benefit that could be derived from the technology is not the only motivating factor.
[829.38 --> 837.36]  Just because something can provide beneficial results doesn't mean that it is beneficial as a whole.
[837.60 --> 838.08]  Exactly.
[838.46 --> 840.52]  I think that's the hard thing to wrestle with.
[840.72 --> 840.84]  Right.
[841.02 --> 842.64]  It's a really hard problem.
[842.70 --> 850.20]  And as companies are trying to wrestle with it, not just surveillance, but, you know, use of AI across the board, use of deep learning, I should say, across the board.
[850.60 --> 852.82]  The question is, who's responsible for what?
[852.88 --> 854.12]  What does it do for liability?
[854.12 --> 856.66]  You know, we've had whole episodes talking about some of this.
[857.30 --> 859.84]  And it is not going to be solved anytime soon.
[860.00 --> 860.08]  Yeah.
[860.16 --> 863.62]  There are no right and wrong answers explicitly except on the extremes.
[864.06 --> 865.62]  It's something people will contend with.
[865.76 --> 871.98]  It's and as periodically it makes for a news story that we get to talk about when something goes awry.
[871.98 --> 875.20]  And I think we're going to see more and more of those over the years.
[875.72 --> 879.82]  And it's not only sort of privacy and security, that sort of thing.
[879.94 --> 885.64]  I mean, automation is another big one that obviously has benefits.
[885.64 --> 886.20]  Right.
[886.40 --> 886.58]  Sure.
[886.58 --> 888.90]  But has a lot of costs as well.
[889.50 --> 903.28]  So thinking about and we've talked about this balance before in our show of, you know, automating away jobs versus sort of creating new types of jobs or, you know, other things like that.
[903.38 --> 907.56]  We have a couple episodes on manufacturing things and all that.
[907.92 --> 908.60]  Yeah, we have.
[908.78 --> 910.52]  I think I've said this before on the show.
[910.52 --> 929.82]  I'm sure that I've said it to you between us and that is the fact that I think as you look at all of the various types of industrial revolution that has happened over time, you know, and moving from the horse and buggy into the automobile and, you know, the airplane and all the various things along the way.
[930.16 --> 933.14]  Each one of those has taken away some opportunities.
[933.36 --> 937.24]  It is also created new opportunities that nobody had envisioned to handle the new thing.
[937.24 --> 953.62]  I think the unanswered thing on automation at this point is with it being cognitive in nature and being combined with robotics that can do things that do not require great cognitive overload that, you know, the question is how many new things are created for those that are taken away.
[953.80 --> 960.04]  As we really work into that over time, I think that's one of the great challenges of this century going forward.
[960.26 --> 964.66]  It's one of those fundamental things that we're going to have to do some restructuring to work our way through.
[967.24 --> 980.92]  We deserve a better internet and the Brave team has the recipe for bringing it to us.
[981.06 --> 982.06]  Start with Google Chrome.
[982.30 --> 986.02]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[986.22 --> 987.10]  Rip out the Google bits.
[987.22 --> 987.86]  We don't need them.
[988.22 --> 990.74]  Mix in ad and tracker blocking by default.
[990.74 --> 993.72]  Quick access to the Tor network for true private browsing.
[994.02 --> 998.42]  And an opt-in reward system so you can get paid to view privacy-respecting ads.
[998.62 --> 1002.36]  Then turn around and use those rewards to support your favorite web creators like us.
[1002.68 --> 1007.30]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1007.30 --> 1020.88]  So, Chris, I had an interesting email the other day.
[1021.02 --> 1029.96]  Actually, our friend Rajiv Shah, who was a guest on the episode 109, he came on the show and talked a lot about data leakage,
[1029.96 --> 1047.84]  which was a really great show just discussing scenarios that can go wrong in your experiments where some of your target data leaks back into your training and things behave much better than you think they might.
[1048.32 --> 1053.24]  It's often hard to prevent this in a lot of scenarios is basically what he's saying.
[1053.30 --> 1057.78]  You have to be extremely careful about this and check yourself constantly.
[1057.78 --> 1066.34]  So, he emailed me, he wrote this new article on DataRobot's website blog called Running Code and Failing Models.
[1066.56 --> 1078.36]  And one interesting thing that I think he's drawing out is that just because you release your source code and people are able to rerun it,
[1078.78 --> 1084.70]  doesn't mean that you kind of have a successful or validated model.
[1084.70 --> 1090.98]  Which is interesting because a lot of the code that I try to run that people release, I can't get to run.
[1091.76 --> 1093.74]  So, that's like a first thing.
[1094.06 --> 1095.60]  Because I think there's this temptation.
[1095.88 --> 1097.22]  That happens, I think, to all of us.
[1097.32 --> 1097.50]  Yeah.
[1098.08 --> 1100.44]  I was thinking about this while I was reading the article.
[1100.64 --> 1101.50]  There's this temptation.
[1102.68 --> 1105.90]  There's eight different implementations of this thing I want to do.
[1105.90 --> 1108.44]  And I start trying out one.
[1108.62 --> 1109.72]  The first one doesn't work.
[1109.80 --> 1110.70]  The code doesn't run.
[1110.80 --> 1115.04]  The second one seems weird and it doesn't run.
[1115.24 --> 1116.04]  And the third one.
[1116.20 --> 1119.70]  And eventually I find that one and it's like, this runs all the way to the end.
[1120.22 --> 1121.54]  You know, I can get my model out.
[1121.74 --> 1124.28]  I get that, like, evaluation number.
[1125.02 --> 1127.64]  You know, maybe I have to tweak a few things and whatever.
[1127.64 --> 1133.40]  But I'm so happy that basically I'm like, this ran and it produced a result.
[1134.22 --> 1135.16]  Like, I win.
[1137.34 --> 1138.80]  Sometimes that's how I feel.
[1138.88 --> 1148.32]  Because it's such a process to, like, get any, like, state-of-the-art model implementation to, like, run sometimes.
[1148.38 --> 1148.94]  Which is great.
[1148.94 --> 1160.92]  One of the reasons why it's great that, like, things like transformers from Hugging Face or, like, other, like, packages out there have such a great, like, model zoo or other things that are validated and will run.
[1161.02 --> 1164.18]  Because sometimes it's just so hard to get these implementations to run.
[1164.34 --> 1165.42]  So, as an aside.
[1165.82 --> 1169.28]  So, Steve, I'm going to pull you for a second out of this particular article.
[1169.76 --> 1173.60]  And I just want, what do you think is really causing, I mean, I've run into that too.
[1173.66 --> 1175.74]  I think everybody runs into that problem.
[1175.74 --> 1180.34]  What do you think is, is it just sloppiness on putting, you know, the solution together?
[1180.54 --> 1183.74]  No, no, I don't think it's intentional in a lot of cases.
[1183.90 --> 1185.40]  I think it's a combination of things.
[1185.86 --> 1195.16]  One of the things is people version control the code they use to do something for their own internal purposes or their own research project.
[1195.40 --> 1203.18]  And they actually don't intend to release that thinking that people are going to try to reproduce what they're doing.
[1203.18 --> 1208.14]  And so, they just sort of, as a result of that, they make certain assumptions.
[1209.14 --> 1210.36]  Like, oh, yeah.
[1210.56 --> 1212.88]  Like, I know I have that always installed.
[1213.18 --> 1217.12]  Or, you know, I'm running on this type of environment or whatever.
[1217.30 --> 1219.34]  And that's just sort of assumed knowledge on their part.
[1219.42 --> 1224.94]  And it's not, like, malicious, like, trying to keep people from reproducing what they're doing.
[1225.02 --> 1228.46]  It's just they release that because that's how they're managing their code.
[1228.46 --> 1234.86]  It's open on GitHub because they have a personal account or they want it out there for whatever reason.
[1235.36 --> 1237.10]  So, I think that's thing number one.
[1237.24 --> 1247.38]  Thing number two is it's just, you know, really hard with all of this technology constantly updating and being interconnected in so many weird and different ways.
[1247.38 --> 1256.22]  People will have, like, a requirements file or something like that that has certain packages or something like that with versions.
[1256.54 --> 1262.94]  But they sort of miss a certain dependency or they don't provide that version number or something.
[1263.22 --> 1268.58]  And, you know, that thing makes all the difference and breaks things in weird ways.
[1268.72 --> 1273.40]  And it's just hard when you're trying to make things reproducible.
[1273.52 --> 1274.48]  It's actually very difficult.
[1274.48 --> 1285.78]  Well, so this is something, though, that in the software world we have tackled and done quite a good job in that, you know, it is now typical to pass work around like that through containers.
[1286.10 --> 1295.44]  Is there an argument to be made that data scientists and deep learning engineers and other practitioners in the field maybe should ramp up on containers and pass these around?
[1295.44 --> 1301.62]  Because that way you're passing, you know, a unit of work, if you will, that has all the dependencies built in.
[1301.62 --> 1310.22]  Yeah, I mean, all of our projects internally that I work on, we containerize everything with Docker and that's how we run things.
[1310.42 --> 1324.54]  Even our Jupyter servers or whatever we're running, it's all run within Docker based off of, you know, also based off of supported, oftentimes supported images from NVIDIA or the TensorFlow team.
[1324.54 --> 1330.32]  Or, you know, images that are supported and have documentation.
[1331.02 --> 1338.44]  You can get these from Docker Hub under the official and verified, you know, links of TensorFlow TensorFlow, for example.
[1338.44 --> 1345.32]  Or you could get some from like NGC from NVIDIA has a lot of really great optimized containers.
[1345.66 --> 1346.82]  So, yeah, we use that.
[1346.90 --> 1348.90]  It's probably not the only way, though.
[1349.28 --> 1358.72]  I certainly know that there's a lot of data science people, AI people, researchers that, you know, Docker, they just don't like it for whatever reason.
[1358.86 --> 1361.02]  They can't get the workflow that they like.
[1361.02 --> 1362.72]  So there's other efforts, too.
[1362.86 --> 1370.24]  I know we had a conversation about ML Commons recently, and they've got this project, ML Cube, which we'll link in the show notes.
[1370.44 --> 1375.48]  And that's part of the goal of that project as well as is solving some of these issues.
[1376.40 --> 1376.50]  Gotcha.
[1376.76 --> 1382.10]  And I had pulled you away from Rajiv's thing, and I was just wondering if what the thesis was from his perspective.
[1382.36 --> 1382.46]  Yeah.
[1382.60 --> 1383.86]  Sorry for pulling you away from that.
[1384.02 --> 1385.68]  That was a longer tangent than I expected.
[1385.68 --> 1391.12]  Yeah, no, but I mean, his conclusion, he says, you know, sharing code isn't enough to validate models.
[1391.60 --> 1401.36]  So if you are kind of lucky in one of those cases, and let's say they've provided the Docker image or something, and you can reproduce their exact training run and do the exact thing that they did.
[1402.22 --> 1410.00]  Basically, his comment then is that, well, that doesn't mean that the model is validated, that comes out of that process.
[1410.00 --> 1415.98]  Because there's this whole other thing called data that is at play here.
[1415.98 --> 1429.92]  And what he shows, interestingly enough, in the article is that one thing could happen is that the code that's part of what just ran, you got to run, actually creates some data leakage.
[1429.92 --> 1432.08]  So he found certain examples of this.
[1432.50 --> 1435.40]  And again, I don't think these are honest, you know, mistakes.
[1435.40 --> 1438.22]  And like, I'm sure there's a lot of these around.
[1438.44 --> 1446.46]  He just found some like in some data science or AI textbooks or books and examples.
[1446.80 --> 1456.60]  But he also, I think the one that struck me more was this Sarcos data set, which is a shared task data set based on predicting the movements of a robotic arm.
[1457.04 --> 1464.82]  And he said that he basically found that the holdout data set was straight up built out of the training data set.
[1464.82 --> 1472.46]  So there was overlap of like, you know, 4,500 examples in the test set that are also present in the training set.
[1472.90 --> 1477.68]  And so, yeah, you're going to get some really interesting behavior of your models there.
[1477.68 --> 1485.24]  So like it just, I think, goes to show like you can obviously get your data from a trusted source.
[1485.40 --> 1487.66]  You're not going to be able to reproduce everything.
[1488.50 --> 1491.64]  You know, you're always going to be standing on the shoulders of other people.
[1491.64 --> 1499.42]  But you've also got to assume that those shoulders that you're standing on, they're also fallible people, right?
[1499.50 --> 1509.52]  So there's definitely stuff that could be bubbling up from those things that you're building your project on that have a little bit of issue in them as well.
[1509.52 --> 1518.14]  Whether that be a shared task data set, whether that be a library that you're using or an implementation that you're referencing or whatever it is.
[1518.88 --> 1519.02]  Gotcha.
[1519.30 --> 1520.20]  Oh, that's interesting.
[1520.20 --> 1526.22]  One of the things is you talk about kind of the fallibility of, you know, people not doing that.
[1526.46 --> 1532.82]  There's a lot of manual stuff unless you're going all the way to containers or some other tool that kind of helps catch you up.
[1532.98 --> 1537.34]  There's been a couple of things that I've seen that are almost the other end of the spectrum on that.
[1537.46 --> 1543.06]  And that is trying to do machine learning without code, you know, to where you don't have all that.
[1543.34 --> 1546.92]  Yeah, there's definitely this like jargon of low, no code.
[1546.92 --> 1547.48]  Yes.
[1547.48 --> 1547.80]  Yes.
[1547.94 --> 1548.90]  Sort of deal, right?
[1549.02 --> 1551.04]  And that's really taken off lately, I've noticed.
[1551.22 --> 1560.64]  I've seen a whole bunch of different things, both on the software side and now people are, I've seen multiple articles about Excel for doing machine learning and stuff.
[1560.80 --> 1561.92]  Things come full circle.
[1561.92 --> 1562.70]  It does.
[1562.70 --> 1571.40]  And I will reveal my bias to say, you know, the first time or two I was seeing the Excel articles, I was kind of shrugging it off entirely.
[1571.68 --> 1579.20]  But they seem to be, depending on how you want to define, you know, machine learning and what level and such as that, it's catching on a little bit.
[1579.20 --> 1582.50]  There's a strong interest in, just as there is in the software development field.
[1582.62 --> 1588.22]  I had a conversation just a couple of days ago with a good friend who was talking about all the no code approaches.
[1588.22 --> 1597.26]  Now, and this is a programmer, someone who programs in many languages, talking about all the no code solutions and that some of them are quite good.
[1597.26 --> 1603.96]  So having seen some of these Excel, promoting Excel as machine learning tools, what do you think?
[1604.06 --> 1609.68]  Is that something that would ever, Daniel Whitenack, enter into your mind to get some work done?
[1610.04 --> 1614.92]  Well, first of all, I don't have access to Excel at all.
[1615.18 --> 1620.90]  So I probably wouldn't use Excel just because I don't pay for it.
[1621.16 --> 1621.46]  Got it.
[1621.64 --> 1625.08]  I mean, I don't know if Google Sheets or whatever, maybe there's some of those things.
[1625.08 --> 1627.32]  There was probably some of those things there as well.
[1627.90 --> 1644.20]  But it's interesting that you bring this up because even just last week, I had a Slack message from one of my coworkers who is not a, who's a product manager, not a programmer, developer type person.
[1644.56 --> 1644.78]  Sure.
[1644.78 --> 1648.84]  But tries to keep up with various things.
[1648.84 --> 1657.16]  And she sent me a message just asking, hey, what is this like low code, no code thing?
[1657.28 --> 1659.32]  And how does it relate to what we're doing?
[1659.88 --> 1667.42]  And to be honest, I didn't know how to answer because I don't know if I fully explored the low code, no code things.
[1667.42 --> 1677.86]  The one thing that I had exposure to is alter self-service analytics, data science and something.
[1678.56 --> 1678.68]  Yeah.
[1678.80 --> 1682.40]  So they say, I'm looking at their website right now.
[1682.40 --> 1693.02]  They talk about simply powerful, extraordinarily easy, automated analytics of every kind, data science and AI without coding, data quality in minutes.
[1693.12 --> 1698.96]  So I will say that I work, I did some advising and consulting with a team last year.
[1699.46 --> 1702.62]  And for some of their data pipelining, they use this tool.
[1703.18 --> 1704.98]  And I thought it was really cool, actually.
[1705.22 --> 1706.58]  Is it open source or is it commercial?
[1706.58 --> 1707.62]  No, it's commercial.
[1708.08 --> 1709.92]  And I don't think it's cheap by any means.
[1710.16 --> 1715.74]  But it seemed to be very powerful for the things that I think it fits a certain group, right?
[1716.14 --> 1734.08]  A group that is doing sort of this data pipelining, wanting to use reusable components that other people have developed to do tasks that they can define the tasks, they can define the business logic, but they don't know how to build those components or manage them in a robust way.
[1734.08 --> 1738.52]  And so they were sort of able to drag in like, oh, here, I'm going to like do this.
[1738.60 --> 1745.00]  So like my data comes in and then they drag in a little box that does some type of preprocessing on that data.
[1745.14 --> 1753.06]  And then they drag in a little box that creates a random forest model or something like that and does some classification, predicts some labels.
[1753.38 --> 1759.50]  And then they drag in another box that like egresses that data to some database or something.
[1759.50 --> 1764.02]  So it's all like for at that level, it seemed quite useful.
[1764.32 --> 1767.10]  I can't speak to like the flexibility of it.
[1767.48 --> 1774.20]  Like what if I have a set of data that's like very different from what they normally deal with?
[1774.34 --> 1774.78]  Sure.
[1774.84 --> 1777.82]  Like how many of those reusable components can I use?
[1778.00 --> 1779.34]  How can I customize them?
[1779.38 --> 1783.72]  And I think there are ways to customize them and bring in your own Python code and all of that.
[1783.72 --> 1796.28]  But then the question becomes, well, if I'm doing that customization and not being able to reuse the reusable components, am I getting the full value out of the thing?
[1796.66 --> 1797.72]  So I don't know.
[1797.80 --> 1802.78]  That's a whole ramble of all basically all I know about low code, no code, which isn't much.
[1802.78 --> 1805.36]  So I'm going to make a bold prediction, my friend.
[1805.70 --> 1815.76]  I am predicting that deep learning eventually has many options in the low code, no code arena and that some of them become quite good.
[1815.88 --> 1819.00]  And that there are both commercial and open source.
[1819.22 --> 1826.72]  And there probably are already some that we're not aware of that people are yelling at us as they listen to this as they're running or whatever they're doing today.
[1826.84 --> 1827.68]  Yeah, there's a lot.
[1827.68 --> 1843.46]  And so I think that it will go that way because I think one of the interesting things that helps in this way is that we are also saying if you listen to the show a couple of years ago, we were talking about totally new algorithmic approaches to deep learning all the time.
[1843.46 --> 1853.74]  And right now there is a conversation within the community about, well, we're seeing kind of the same classifications of models that are used or architectures that were used over and over again.
[1854.10 --> 1856.68]  And I'm waiting for the next really big breakthrough.
[1856.68 --> 1857.62]  I'm looking forward to that.
[1857.72 --> 1858.84]  But it's been a little while.
[1858.92 --> 1860.00]  We're seeing a lot of evolution.
[1860.88 --> 1870.14]  And we can talk about it in a negative, but I will say it helps the tooling catch up to some degree so that people, as it gets commoditized, because that's what we are seeing.
[1870.20 --> 1878.10]  It was seeing a lot of productivity on very diverse and massive commoditization of deep learning architectures into many, many use cases.
[1878.36 --> 1880.50]  And so the tooling will catch up.
[1880.50 --> 1888.32]  So the way I'm measuring that, I have my software development workflow, which is, I think, fairly mature, as is for other software developers.
[1888.32 --> 1894.60]  And then we're seeing our deep learning workflows have been maturing steadily as new things have come out the last couple of years.
[1894.60 --> 1903.04]  I'm looking forward to the day when those two are able to merge in the way that I want it to merge, meaning it is a sensible, comprehensive approach.
[1903.04 --> 1904.74]  So I'm excited about that.
[1904.82 --> 1910.24]  And if there is some level of no code, low code built into that workflow, I'm OK with that.
[1910.32 --> 1911.28]  I'm not going to push it away.
[1911.28 --> 1925.18]  Well, Chris, I recently have been working on specking out and getting some quotes for a new server for some of the research that's going on in our organization.
[1926.16 --> 1929.30]  And I was looking through all sorts of different options.
[1929.30 --> 1932.40]  And I talked to all sorts of different people.
[1932.40 --> 1936.42]  Thank you to if there's anyone out there that helped me through that.
[1936.56 --> 1937.20]  You know, thank you.
[1937.80 --> 1948.98]  But after all of our conversations on the podcast, I thought, like, yeah, I kind of like know enough to like pretty instantly figure out what we need.
[1949.16 --> 1954.52]  And then like I started looking at these different options and the thing that got me.
[1954.52 --> 1957.42]  So I knew a lot of the things that we needed.
[1957.42 --> 1965.78]  But then I had this thought of envisioning the multi GPU jobs that we were going to need to run.
[1965.78 --> 1978.14]  And looking at the different systems that were available, I started sort of questioning, like, what sort of like machine do you actually need to run a multi GPU job?
[1978.50 --> 1987.82]  Because there's all of these different like acronyms and things that are promoted, like the NVLink, NVSwitch from NVIDIA.
[1987.82 --> 1988.42]  Sure.
[1988.96 --> 1995.44]  And there's these little NVLink bridges that bridge directly between GPU cards.
[1995.68 --> 1997.26]  So I was unclear.
[1997.68 --> 2010.22]  Like, I just kind of hit a roadblock and I was like, like, what do I actually need for the type of multi GPU jobs that we're going to want to run, which are mainly like training speech related models?
[2010.22 --> 2013.16]  I ran across this.
[2013.16 --> 2026.34]  So in doing that, Lambda Labs, which builds and sells GPU workstations and servers and pods, they have this really interesting set of benchmarks that they've done, which we'll link in the show notes.
[2026.34 --> 2030.34]  And they break out for both PyTorch and TensorFlow.
[2031.34 --> 2035.38]  And you can sort of they have these interactive graphs.
[2035.38 --> 2037.52]  So you can have it a chart or a table.
[2037.76 --> 2053.04]  You can look at different metrics, different precision, different number of GPUs, all sorts of different models, like transformer models, ResNet, WaveGlow, Talkatron, BERT, LargeSquad, all sorts of different models.
[2053.04 --> 2064.06]  And C, for all of these different combinations of GPUs, the throughput numbers essentially is what I came down to.
[2064.06 --> 2070.74]  And one interesting thing, like if you go to four GPUs, you all of a sudden see some some really interesting things.
[2070.74 --> 2087.56]  Like, for example, if I'm looking at, let's say, four GPUs and I look at all models, I can see, OK, well, there's the A1, 4X A100 and one has PCIe, one has SXM4.
[2087.56 --> 2092.56]  The difference there being the way that the GPUs interconnect.
[2093.80 --> 2106.30]  And essentially, if you start looking through these, like if I go down to two then and look at the numbers, some of them like say NVLink, some of them say PCIe explicitly.
[2106.30 --> 2122.62]  And after doing some exploring, I started to realize a lot of these numbers didn't have the NVLink or NVSwitch interconnect, which made me start to question like, well, do you really need NVSwitch to do multi GPU jobs?
[2122.74 --> 2129.70]  Like if I get a bunch of cards and then like they're not linked with NVLink, NVSwitch, can I just do nothing?
[2129.82 --> 2131.44]  Is it going to be absolutely terrible?
[2131.44 --> 2138.78]  And so what I ended up finding was, yeah, like you do get a slight boost with this NVLink NVSwitch.
[2139.20 --> 2144.58]  But in a lot of cases, and even for some of these models, it wasn't significant at all.
[2144.92 --> 2147.42]  And, you know, in some cases it was significant.
[2147.86 --> 2155.78]  And, yeah, I found that I found that sort of interesting that like, yes, you do get a sort of performance hit.
[2155.78 --> 2170.90]  But, or, you know, if you don't have the interconnect, but in some cases it's not that much because, you know, you're only updating those parameters between GPUs when you update your gradients, which isn't happening all the time.
[2171.40 --> 2171.68]  Right.
[2171.68 --> 2181.56]  So I just thought I'd share that while we were discussing things because I hadn't fully like got through that train of thought before I explored these things.
[2182.02 --> 2194.64]  So clearly at the different levels that you can buy in, in terms of hardware, you know, from NVIDIA or other vendors, you know, clearly they're pushing NVLink and those interconnect technologies.
[2194.64 --> 2203.42]  What you're saying, if I'm understanding you is, is it really depends on the architecture that you're deploying and, and the data that you're using the dataset.
[2204.34 --> 2205.38]  Yeah, I think it does.
[2205.48 --> 2207.10]  So here's one way to put it.
[2207.10 --> 2218.52]  You may be able to get more cards that are not linked with NVSwitch, but are like the later gen architectures.
[2218.70 --> 2219.06]  Right.
[2219.08 --> 2228.94]  That will actually perform faster than last generation, like top tier cards that are connected with NVLink or NVSwitch.
[2229.06 --> 2229.84]  That's interesting.
[2229.84 --> 2230.28]  Yeah.
[2230.28 --> 2230.32]  Yeah.
[2230.46 --> 2237.88]  So it's not just a, like, if you're doing multi GPUs, you need this special interlink infrastructure.
[2238.50 --> 2244.18]  You kind of have to also weigh in the generation of cards that you're looking at.
[2244.18 --> 2256.90]  Cause like, if you go down to one, you know, one GPU on the Lambda benchmarks, you can see like that the 3090, which is a consumer card and is very cheap.
[2257.28 --> 2269.40]  Like as far as car, you know, GPU cards go gets you halfway to the training on, on that throughput in as the A100 that's listed there.
[2269.46 --> 2269.68]  Really?
[2269.68 --> 2273.00]  And so like, that's pretty incredible actually.
[2273.46 --> 2273.60]  Right.
[2273.60 --> 2294.12]  So if you then go to like, you know, two GPUs on the benchmark, for example, you could have two 3090s that are going to be more throughput on their, on their benchmarks than two RTX 8000s connected with NVLink.
[2294.12 --> 2297.30]  And those are pretty hefty cards, right?
[2297.30 --> 2299.40]  And they're connected with NVLink.
[2300.22 --> 2313.00]  But two 3090s that are just connected with PCIe, no NVLink, are going to outperform it in terms of this particular benchmark for cheaper, right?
[2313.36 --> 2316.26]  Using this, did you arrive at a spec for your own purposes?
[2316.26 --> 2320.34]  So we have a couple different ones that we've spec'd out.
[2320.66 --> 2323.64]  The 3090s, they're consumer cards, right?
[2323.78 --> 2329.70]  So if you're getting like an enterprise server, they're likely not going to be spec'd out with an enterprise server.
[2329.70 --> 2332.22]  But yeah, we did come up with a solution.
[2332.22 --> 2351.04]  And I think our solution was to get one server that had a bunch of cards that weren't in VLink, didn't have the fancy NV switch because we were going to do a lot of single GPU jobs and get the later gen cards because they're going to be so fast for that stuff.
[2351.04 --> 2360.96]  And then just get, you know, a second server with maybe two of the later gen cards that are linked.
[2361.32 --> 2361.76]  Gotcha.
[2362.02 --> 2363.18]  You split the difference sort of.
[2363.18 --> 2364.42]  So you kind of split the difference.
[2364.70 --> 2364.88]  Yeah.
[2365.18 --> 2366.68]  So by use case, it's going to depend.
[2366.76 --> 2367.72]  It basically depends.
[2368.08 --> 2369.94]  Yeah, I found this all very interesting.
[2370.12 --> 2376.76]  And I don't know, maybe like going into all those details, no one, no one's listening is like, why is he talking about this?
[2377.22 --> 2378.22]  But it was very.
[2378.64 --> 2380.96]  We had a whole episode about this not too far back.
[2381.04 --> 2401.34]  Yeah, it was it was very surprising to me how much I thought I knew going into that versus what it actually sort of took to really understand what was the optimal setup for our team in terms of the generation of the card versus the linking and all that stuff.
[2401.34 --> 2402.86]  And we'll link it in the show notes.
[2402.96 --> 2406.04]  But I know I don't have the episode number off the top of my head.
[2406.04 --> 2411.96]  But we did an episode where you talked about your process of putting together your first server.
[2412.52 --> 2412.64]  Yeah.
[2412.70 --> 2414.68]  And all the decisions that you made.
[2414.92 --> 2422.56]  And so if this conversation is of any interest to someone listening, then they should definitely, if they haven't already listened to it, go back to that episode.
[2422.70 --> 2423.30]  It was excellent.
[2423.56 --> 2425.56]  And we'll put it in the show notes to give you a quick link to it.
[2425.56 --> 2432.48]  As we look forward, I ran into a IEEE Spectrum is a publication of IEEE.
[2432.48 --> 2450.34]  And they had an article here called Deep Learning at the Speed of Light, where they were talking about Light Matter, which is a company who is putting together, you know, photon based computing, you know, using light in its chips to do accelerated deep learning.
[2450.34 --> 2453.26]  And so kind of an interesting thought there.
[2453.46 --> 2455.88]  You know, I don't know where the competition is.
[2455.92 --> 2457.36]  I don't know where NVIDIA is on that.
[2457.66 --> 2460.94]  But definitely it was an interesting idea about the idea of doing that.
[2461.10 --> 2461.84]  Any thoughts?
[2462.02 --> 2471.64]  If you had an affordable chip that you could use for your purposes and there was advantage to it, would you consider doing a light-based solution for your computation?
[2472.42 --> 2473.02]  Yeah, of course.
[2473.14 --> 2476.32]  I mean, I could so nerd out with that.
[2476.32 --> 2483.66]  With my physics background, it's like, you know, oh, you're using a NVIDIA 3090.
[2483.80 --> 2485.88]  I'm using a Max Zender infrarometer.
[2486.94 --> 2489.02]  I mean, who needs electricity when you got light?
[2489.02 --> 2490.70]  It just has a different ring to it.
[2490.70 --> 2491.58]  Yeah, exactly.
[2492.16 --> 2492.64]  Totally.
[2493.42 --> 2499.74]  It'll be interesting to see if the market hits a point where that becomes a commonplace thing and not a novelty.
[2500.38 --> 2505.70]  I just thought it'd ask since I wasn't even going to bring that up, except that we were talking about chips here.
[2505.70 --> 2507.02]  Infrastructure, yeah.
[2507.60 --> 2507.92]  Cool.
[2508.08 --> 2514.80]  Well, as we kind of get to the end here, we always like to share a couple learning resources with people.
[2515.00 --> 2519.94]  And I know that you found one deep learning course that's online now.
[2520.00 --> 2521.42]  Do you want to talk a little bit about that one?
[2521.94 --> 2522.26]  Yeah.
[2522.48 --> 2526.06]  So one of the, I assume you're talking about Jan LeCun's course?
[2526.12 --> 2526.32]  Yeah.
[2527.32 --> 2528.92]  Jan LeCun, who is at Facebook.
[2528.92 --> 2533.02]  I forget his title, Chief AI or something.
[2533.62 --> 2534.82]  I don't have it in front of me.
[2535.04 --> 2537.64]  But he is also one of the legends of the field.
[2537.96 --> 2540.72]  So, you know, he is one of the top minds in the field.
[2541.12 --> 2544.86]  And he released a deep learning course that is free.
[2545.24 --> 2548.10]  And it's really had quite an uptake on it.
[2548.48 --> 2553.52]  It's called Deep Learning DSGA 1008.
[2553.52 --> 2556.82]  It's part of the New York University Center for Data Science.
[2557.44 --> 2559.22]  And it's accessible by all.
[2559.38 --> 2564.00]  And so by signing up for this course, which is released in the spring.
[2564.16 --> 2568.78]  So I think spring 2021, we'll be signing up shortly, if not already.
[2569.18 --> 2572.02]  But you get to learn from one of the great minds of the field.
[2572.02 --> 2577.30]  And so we've seen a few other major figures in the field release their own courses.
[2577.62 --> 2578.48]  And we've taken some.
[2578.62 --> 2583.94]  But it definitely, the depth of somebody who is one of the leading thinkers on where the
[2583.94 --> 2587.74]  field is going, not just as a practitioner, but as a researcher.
[2588.26 --> 2588.62]  I don't know.
[2588.72 --> 2590.48]  It adds a little zest to it.
[2590.62 --> 2594.84]  It's a course that I'm definitely going to look into myself just to see what's on Jan's
[2594.84 --> 2595.20]  mind.
[2595.72 --> 2596.44]  Yeah, that's awesome.
[2596.44 --> 2603.58]  The one learning resource that I wanted to share was this sort of new format that the
[2603.58 --> 2605.44]  TensorFlow team is doing for their...
[2606.30 --> 2610.60]  In the past, they sort of did this TensorFlow Dev Summit, which is a great event.
[2610.78 --> 2613.34]  It was, you know, I also watched it live streamed.
[2613.64 --> 2617.76]  I'm not sure how that'll all play out in what formats they'll eventually do.
[2617.88 --> 2621.08]  But this year, they're doing this thing called TensorFlow Everywhere.
[2621.56 --> 2622.52]  Yep, I noticed that.
[2622.66 --> 2623.92]  Yeah, we'll link it in the show notes.
[2623.92 --> 2626.34]  I think this is really cool, actually.
[2626.68 --> 2632.64]  So they essentially have TensorFlow Everywhere, which is a series of global events that TensorFlow
[2632.64 --> 2635.06]  is hosting with all sorts of different content.
[2635.70 --> 2643.54]  And I think it's really cool because they have events that are, you know, geared towards
[2643.54 --> 2645.20]  certain geographies.
[2645.28 --> 2648.14]  So the time zones match up well for people.
[2648.14 --> 2653.32]  It's not like people have to live stream at, you know, midnight or 1am or something like
[2653.32 --> 2653.68]  that.
[2653.68 --> 2656.20]  But also in a number of languages.
[2656.20 --> 2663.16]  So I see events in Bahasa Indonesian, Chinese, Korean, Vietnamese, Turkish, different languages.
[2663.46 --> 2669.44]  And so people are actually getting that content in a language they value most, at least a little
[2669.44 --> 2671.52]  bit more than they were before.
[2671.64 --> 2674.02]  You know, there's 7,000 languages in the world.
[2674.46 --> 2675.54]  There's only a handful here.
[2675.54 --> 2678.74]  But I think it's a great step in that direction as well.
[2678.86 --> 2682.70]  So I thought it was really cool the way that TensorFlow is doing this.
[2683.02 --> 2689.70]  And you can go to the website, figure out which event is sort of in your geography and
[2689.70 --> 2692.38]  works for your, you know, timing.
[2692.86 --> 2695.28]  They're kind of going on actually right now.
[2695.28 --> 2700.36]  There's some that have already gone on, but then they're stretching out through March as
[2700.36 --> 2700.70]  well.
[2700.80 --> 2707.24]  And the ones in North America, which is where we are, is the 27th of February.
[2707.54 --> 2710.36]  So I'll probably be tuning into that one.
[2710.54 --> 2712.26]  But yeah, definitely check this out.
[2713.02 --> 2714.36]  That sounds really good.
[2714.50 --> 2717.24]  You know, just as a kind of a closing comment on that.
[2717.50 --> 2722.16]  There are so many, obviously, very, very enormous negatives having to do with the pandemic.
[2722.16 --> 2727.30]  But one thing that might be a small positive is the fact that there has been some interesting
[2727.30 --> 2732.10]  innovation with the whole world kept away from one another and us still having the need
[2732.10 --> 2737.44]  to have, you know, to have commerce, to conduct business, to see each other and to talk and
[2737.44 --> 2738.76]  communicate and learn.
[2738.92 --> 2742.04]  There's been quite a bit of innovation in terms of how we've approached it.
[2742.14 --> 2748.30]  So I'm curious as we potentially are at the beginning of the end of the pandemic in terms
[2748.30 --> 2754.44]  of vaccine rollouts and and maybe maybe at some point in the months ahead, having the
[2754.44 --> 2759.14]  ability for for large numbers of people to return to to normal life.
[2759.32 --> 2760.76]  How do you think that'll change?
[2760.90 --> 2761.54]  What do you think?
[2761.86 --> 2764.92]  You know, are we going back to are we all just going to fall back into our old habits
[2764.92 --> 2765.96]  and go to the conferences?
[2766.34 --> 2768.32]  Do you think more things will stay online?
[2768.82 --> 2772.14]  I think there'll be quite a few people that will be eager to do that.
[2772.14 --> 2779.00]  But I'm also hoping that people sort of have found at least some ways to, you know, save
[2779.00 --> 2781.14]  on on travel and those sorts of things.
[2781.14 --> 2788.16]  But also, I'm really hopeful that it, you know, ends up that there are lower cost and
[2788.16 --> 2795.30]  more inclusive ways of involving people, especially from from Africa, from Asia, from Latin America,
[2795.30 --> 2802.32]  from other places in the events that, you know, were primarily sort of North American and Western
[2802.32 --> 2803.40]  European based.
[2803.82 --> 2809.62]  Yeah, that's the part that I really hope survives is like enabling that that access for people
[2809.62 --> 2816.48]  and also enabling those people to contribute, not just sort of be consumers, but actually
[2816.48 --> 2821.30]  realizing that they have valuable things to add into these events and giving them a way
[2821.30 --> 2821.90]  to do that.
[2822.30 --> 2825.04]  Those are the things that that I'm hopeful will survive.
[2825.30 --> 2830.94]  I'm 100% in agreement with you and you cannot possibly have a better note to go out on.
[2831.02 --> 2832.32]  So I think we should stop right there.
[2832.52 --> 2833.74]  Yeah, sounds good.
[2833.80 --> 2834.68]  This has been fun, Chris.
[2834.82 --> 2835.02]  Thanks.
[2835.06 --> 2836.26]  It has been a fun conversation.
[2840.02 --> 2842.30]  Thank you for listening to Practical AI.
[2842.94 --> 2846.64]  If this is your first time, make sure you subscribe so you don't miss a thing.
[2847.16 --> 2854.00]  Head to practicalai.fm to subscribe or find us in Apple Podcasts, Spotify, or wherever you
[2854.00 --> 2854.82]  listen to podcasts.
[2855.30 --> 2859.78]  And if you get value from the show, please do share it with a friend or a colleague.
[2859.94 --> 2861.34]  We appreciate you spreading the word.
[2862.14 --> 2865.06]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2865.58 --> 2869.18]  It's produced by Jared Santo and our music is provided by Breakmaster Cylinder.
[2869.70 --> 2871.86]  We are brought to you by some awesome sponsors.
[2872.42 --> 2874.86]  Shout out to Fastly, Linode, and LaunchDarkly.
[2874.86 --> 2876.92]  That is our show.
[2877.12 --> 2879.62]  We hope you enjoyed it and we'll talk to you again next week.
[2879.62 --> 2899.34]  Outside Animal産 with Daniel Whitenack and Chrisس guys.
[2899.90 --> 2900.46]  Bye-bye.
