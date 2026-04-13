[0.00 --> 7.28]  Welcome to Practical AI.
[7.70 --> 15.00]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[15.00 --> 17.72]  changing the world, this is the show for you.
[18.06 --> 20.64]  Thank you to our partners at Fly.io.
[21.16 --> 26.86]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on
[26.86 --> 30.72]  six continents, so you can launch your app near your users.
[31.28 --> 33.24]  Learn more at Fly.io.
[35.02 --> 36.14]  What's up, friends?
[36.40 --> 39.72]  Intel Innovation 2024 is right around the corner.
[39.88 --> 40.72]  Accelerate the future.
[41.10 --> 47.18]  Registration is now open, and it takes place September 24th and 25th in San Jose, California.
[47.62 --> 52.66]  This event is all about you, the developer, the community, and the critical role you play
[52.66 --> 55.48]  in tackling the toughest challenges across the industry.
[55.48 --> 58.28]  Ignite your passion for AI and beyond.
[58.58 --> 64.56]  Grow your skills to maximize your impact and network with your peers as they unleash the
[64.56 --> 67.16]  next wave of advancements in technology.
[67.52 --> 68.46]  Here's what you can expect.
[68.82 --> 74.86]  Understand the emerging innovation and trends in dev tools, languages, frameworks, and technologies
[74.86 --> 78.72]  in AI and beyond to empower you and the solutions you're building.
[79.20 --> 80.92]  Get in-depth technical experience.
[80.92 --> 87.02]  Join hands-on workshops, labs, meetups, and hackathons to collaborate and solve problems
[87.02 --> 87.84]  in real time.
[88.18 --> 91.38]  You can explore featured partner and Intel solutions.
[91.84 --> 94.12]  They have partners there, startups there, customers there.
[94.40 --> 99.82]  And Intel is showcasing the latest in products, services, and solutions across keynotes, tech
[99.82 --> 102.44]  sessions, and the show floor to help you meet your development needs.
[102.88 --> 103.76]  Collaborate with experts.
[103.76 --> 104.88]  Learn and have fun.
[104.88 --> 111.58]  Engage in interactive sessions to connect, get certified, gain unique ideas and perspectives,
[112.28 --> 116.20]  build long-lasting networks, and of course, have fun.
[116.56 --> 117.32]  And get inspired.
[117.48 --> 122.50]  Hear from leading industry experts, technologists, startup entrepreneurs, and fellow developers,
[122.84 --> 128.54]  along with Intel leadership, CEO Pat Gelsinger, and CTO Greg Lavender, as they take you through
[128.54 --> 130.80]  the latest advancements in technology.
[131.26 --> 133.80]  Don't miss this chance to be at the forefront of innovation.
[134.16 --> 137.52]  Take advantage of early bird pricing right now until August 2nd.
[137.80 --> 139.48]  Register using the link in our show notes.
[139.70 --> 143.08]  Or to learn more, go to intel.com slash innovation.
[143.52 --> 146.02]  Once more, that's intel.com slash innovation.
[146.48 --> 148.22]  Or go to the show notes and click that link.
[158.54 --> 167.06]  Well, welcome to another episode of Practical AI.
[167.32 --> 168.90]  This is Daniel Whitenack.
[169.02 --> 171.48]  I am founder and CEO at Prediction Guard.
[171.70 --> 177.18]  I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer
[177.18 --> 178.48]  at Lockheed Martin.
[178.72 --> 179.40]  How are you doing, Chris?
[179.54 --> 180.52]  I'm doing fine.
[180.76 --> 182.52]  We got a fun one today, Daniel.
[182.66 --> 183.54]  This is going to be a good one.
[183.84 --> 185.04]  Yes, of course.
[185.04 --> 192.98]  It was wonderful not that long ago to be in the great city of San Francisco and run
[192.98 --> 196.80]  into our friend Demetrios from the ML Ops community.
[197.46 --> 201.14]  And I figured I'd just bring him along for another conversation.
[201.46 --> 202.80]  So Demetrios, how are you doing?
[203.14 --> 203.98]  I'm great, man.
[204.26 --> 204.92]  We're back.
[205.28 --> 208.74]  And I've got some bad news to break to you right now.
[208.80 --> 209.96]  I wanted to do it on air.
[210.38 --> 211.22]  Go for it.
[211.22 --> 212.68]  Just to get your reaction.
[213.12 --> 213.64]  Oh, boy.
[213.64 --> 214.72]  You can be vulnerable.
[215.04 --> 216.52]  This is how we build community.
[216.80 --> 217.70]  Yeah, I'm nervous.
[218.12 --> 218.36]  Yeah.
[218.54 --> 220.06]  So Prediction Guard, awesome.
[220.26 --> 222.68]  Congratulations on all the success that you've had.
[223.00 --> 227.28]  We're doing a data engineering for ML and AI virtual conference.
[227.46 --> 230.92]  And one of your colleagues, Daniel, filled out the CFP.
[231.48 --> 234.66]  I haven't gotten back to him yet, but I can't accept him.
[235.00 --> 238.82]  I just am way too full, way over my head.
[238.82 --> 246.50]  And as much as I want to, I'm going to have to divert him to doing his own special event.
[246.64 --> 250.82]  Basically, we're going to actually take what may have been a bad thing and turn it into
[250.82 --> 251.28]  a good thing.
[251.50 --> 252.48]  That sounds great.
[252.60 --> 254.24]  I'm looking forward to learning more.
[255.10 --> 256.00]  There we go.
[256.00 --> 262.50]  So I got to make sure that you get all the love and shine you deserve because I'm super
[262.50 --> 263.38]  stoked at what you're doing.
[263.90 --> 264.12]  Yeah.
[264.22 --> 264.44]  Yeah.
[264.48 --> 265.36]  Well, appreciate that.
[265.42 --> 266.70]  It was great to see you.
[266.86 --> 269.72]  And you had your own event in SF.
[269.92 --> 270.52]  How was that?
[270.52 --> 275.06]  I do not recommend doing live events to even my greatest enemies.
[275.48 --> 283.52]  If anyone out there is contemplating organizing an AI conference, you can do it, but I don't
[283.52 --> 284.06]  recommend it.
[284.14 --> 284.56]  It's going to hurt.
[285.18 --> 285.34]  Yeah.
[286.12 --> 287.58]  It's painful, man.
[287.94 --> 289.38]  But it was a big success.
[289.60 --> 292.98]  It was just a lot of work leading up to it, as you can imagine.
[293.36 --> 296.24]  And we had fun on the day of.
[296.24 --> 304.98]  I think over 750 people showed up, a lot of great conversations, a lot of fun, spontaneous,
[305.56 --> 307.14]  sporadic meetings with people.
[307.26 --> 311.22]  And that's the stuff you get at in-person conferences that it's really hard to replicate
[311.22 --> 311.96]  virtually.
[312.40 --> 312.50]  Yeah.
[312.60 --> 313.66]  You know what the secret is?
[313.90 --> 317.30]  The secret is it's AI and it needs a lot of hype.
[317.62 --> 319.14]  It really needs a lot of hype.
[319.68 --> 322.12]  There's one thing that we don't have enough of in AI.
[322.34 --> 323.36]  It's we don't have enough hype.
[323.84 --> 326.00]  If you had hyped it more, it would have worked.
[326.24 --> 330.98]  You know, I do a fair amount of hyping.
[331.26 --> 338.72]  And so for those out there that are sick of the hype, like myself, I've only got myself
[338.72 --> 339.72]  to blame on this.
[340.86 --> 349.54]  Well, Chris, you sent me a very interesting looking hype filled chart the other day.
[349.68 --> 352.00]  You want to go into what that was?
[352.00 --> 353.08]  I will.
[353.34 --> 356.00]  And I'm actually blaming it all on Demetrius.
[356.62 --> 360.42]  He was making fun of the Gartner hype cycle.
[360.56 --> 364.00]  And gosh, I hope they're not a sponsor because we're making fun of them today.
[364.00 --> 367.70]  And he was going through that and it was funny.
[367.92 --> 373.64]  And I said, dude, we need to do an episode where we all analyze the Gartner hype cycle
[373.64 --> 376.36]  in 2024 for artificial intelligence.
[376.36 --> 381.46]  And we break it down and we're going to assess it and decide what we think of those things.
[381.62 --> 386.26]  And we're not doing this in our normal, extremely serious manner.
[386.58 --> 388.64]  We are doing this in the fun way.
[389.00 --> 393.48]  And lest you don't know Demetrius out there, which I can't imagine because he's a regular
[393.48 --> 395.16]  guest on the show here.
[395.16 --> 400.98]  He is, in addition to being a brilliant guy in this field, he is also the funniest man
[400.98 --> 402.70]  in all of artificial intelligence.
[403.00 --> 404.24]  So this is going to be good.
[404.72 --> 408.98]  And we're going to dive into the Gartner hype cycle today and break it down for you.
[409.04 --> 413.46]  We're going to start with the real one and then we're going to maybe make some adjustments
[413.46 --> 414.08]  to it.
[414.54 --> 420.78]  You know, Chris, you say making fun, but I mean, Gartner seems to have fulfilled their
[420.78 --> 421.04]  mission.
[421.04 --> 425.04]  I mean, we're talking about the hype cycle where we're going into it.
[425.12 --> 429.62]  So maybe their mission was fulfilled and, you know, we are their fulfillment.
[430.10 --> 430.32]  Yeah.
[430.82 --> 431.56]  Oh, my God.
[431.58 --> 432.92]  Yeah, we're hyping it up right now.
[432.92 --> 433.46]  We're hyping it up.
[433.70 --> 434.10]  Okay.
[435.02 --> 436.44]  And we're going to have fun doing it.
[437.00 --> 442.62]  Oh, I just have to say, yeah, please, if anyone knows how I can get a job doing this
[442.62 --> 449.62]  kind of stuff, just making up words and then putting them onto a wave graph, let me know
[449.62 --> 451.68]  because I would love this as a job.
[451.76 --> 453.26]  It just seems like it's too much fun.
[453.98 --> 454.70]  Well, let's see.
[454.76 --> 455.68]  I think surf's up.
[455.84 --> 459.36]  Let's hop on the wave and let's start talking our way through.
[459.60 --> 463.70]  You know, Demetrius, do you want to lead off on some of your ideas there?
[463.70 --> 471.00]  So I think the most surprising to me out of this whole graph and for anybody that's not
[471.00 --> 478.00]  familiar with the hype cycle, you've got the big like upward side and then it goes down
[478.00 --> 485.40]  and it kind of crashes and then it starts to climb back up and it's the traditional like.
[485.40 --> 489.48]  And the two second version of that, and I did it in our, in a previous episode, I did
[489.48 --> 493.02]  a longer version when we were looking at some specific things on it.
[493.02 --> 496.20]  But the two second version is new technology comes out.
[496.52 --> 498.14]  Everyone's super excited about it.
[498.18 --> 501.24]  They think it's going to be the greatest thing since sliced bread.
[501.78 --> 503.46]  It doesn't live up to the hype.
[503.62 --> 504.56]  They get frustrated.
[504.98 --> 505.84]  They go, good.
[505.88 --> 507.20]  This thing sucks.
[507.54 --> 513.14]  And, and it falls down on the hype popularity side and then cooler heads prevail and they kind
[513.14 --> 515.16]  of go, okay, well maybe it can do something okay.
[515.48 --> 518.66]  And, and then it's into a reasonable sense of productivity.
[518.66 --> 520.48]  So that's Gartner in a nutshell.
[520.48 --> 526.76]  So the biggest surprise for me is at the bottom of the slope.
[526.90 --> 533.00]  So after it's gone all the way up the hype cycle, it's come down and crashed down and is
[533.00 --> 539.70]  at the absolute bottom that the trush of disillusionment exactly there is cloud AI services.
[540.06 --> 540.20]  Yes.
[540.20 --> 546.92]  And for me, that is the biggest misnomer because if anybody is making any money out of any of
[546.92 --> 553.42]  this, and I guess maybe hype and actual money, they're detached and they're very decoupled
[553.42 --> 553.68]  here.
[553.82 --> 555.90]  But for me, that was like, wait, what?
[556.12 --> 558.68]  There's no hype in cloud AI services.
[559.24 --> 561.28]  So bedrock out of there.
[561.48 --> 562.34]  Hype is killed.
[562.50 --> 564.14]  It's at the trough of disillusionment.
[564.54 --> 569.96]  Any type of SageMaker, if you're using that or Vertex, no out of there.
[569.96 --> 571.64]  It's the lowest of the low.
[571.64 --> 576.58]  And so when I saw that, that was instantly like, dude, why are you even doing it?
[576.90 --> 577.08]  Yeah.
[578.08 --> 582.66]  I did not believe a thing that I read afterwards, but that was my thing.
[582.70 --> 584.70]  Any, any big surprises from you guys?
[585.04 --> 591.06]  I think your point on, if there's anyone making a killer amount of money on this, it's Microsoft,
[591.54 --> 593.72]  it's Amazon, it's Google.
[594.52 --> 599.98]  Part of my struggle here is some of these terms, like I could interpret them one way
[599.98 --> 602.28]  or another way, right?
[602.28 --> 607.58]  Like SageMaker, for example, which for those that don't know is, it's kind of like a model
[607.58 --> 612.84]  deployment service within AWS and there's various convenience around it and that sort
[612.84 --> 613.18]  of thing.
[613.36 --> 619.42]  Like that's been around for quite a while now, like a very long time, even before sort
[619.42 --> 622.56]  of the kind of hyped gen AI stuff.
[622.78 --> 623.54]  Oh, long before.
[623.68 --> 624.40]  But yeah.
[624.50 --> 627.42]  So like, is that a cloud AI service?
[627.58 --> 629.86]  Like that's been around for a huge amount of time.
[629.90 --> 633.58]  Or are we just talking about like hosted model APIs, right?
[633.68 --> 634.78]  They don't say.
[634.78 --> 637.56]  Which also, to be fair, have been around a long time.
[637.56 --> 641.88]  Like you look at something like OCR or translation or something like that.
[642.02 --> 647.80]  And in cloud services have been around for a really long time and are sort of ubiquitously
[647.80 --> 648.34]  used.
[648.64 --> 649.74]  It's funny that it's down there.
[649.84 --> 650.82]  I get your point.
[651.20 --> 655.24]  Maybe it's just like everyone knows that's where the cloud, that's where all the services
[655.24 --> 655.70]  are.
[655.84 --> 657.14]  We're all paying for them.
[657.38 --> 657.56]  Yeah.
[657.66 --> 661.14]  So does hype correspond to usage, I guess?
[661.14 --> 666.44]  Like in this chart, is it that people aren't hyping cloud AI services, even if they're
[666.44 --> 666.98]  used?
[667.24 --> 669.34]  Or I think it's an emotional thing.
[669.46 --> 671.88]  You know, the hype side is, you know, how much people are talking.
[672.20 --> 674.30]  So maybe it's accurate in this context.
[674.80 --> 678.86]  There is nothing sexy about AI services in cloud providers.
[679.02 --> 683.28]  And maybe that's what they're getting at is like, yes, we're paying an arm and a leg.
[683.38 --> 684.70]  We're giving them all of our money.
[684.90 --> 686.46]  But there is nothing sexy.
[686.72 --> 689.96]  But productivity wise, it's definitely productive.
[689.96 --> 691.44]  I would think so.
[691.78 --> 695.50]  Yeah, it's very pragmatic, too, especially for those people just starting.
[696.22 --> 704.46]  I don't know any easier way than to just grab an API from like Amazon Bedrock is just hosted
[704.46 --> 708.00]  model, hit that API like you would hit an open AI API.
[708.18 --> 709.98]  But now you have a suite of models, right?
[710.28 --> 713.70]  So that seems to me like a near miss.
[713.80 --> 718.44]  But then at the top of the peak is the other one that was a huge surprise to me.
[718.44 --> 720.80]  Because I've noticed this trend.
[720.90 --> 727.42]  I don't know if you guys have noticed it, but people who were formerly ML engineers, we've
[727.42 --> 730.10]  all converted into being AI engineers.
[730.74 --> 736.72]  And an AI engineer is so misleading because you don't know, is that somebody that is coming
[736.72 --> 739.68]  from like a front end development world?
[739.68 --> 741.82]  And now they do a little prompt engineering.
[741.82 --> 749.12]  They use a few frameworks and they can chain together some prompts to make a bit of a demo
[749.12 --> 749.74]  on Twitter.
[750.06 --> 751.76]  And now they're an AI engineer.
[751.76 --> 756.28]  Or is it somebody that was deep, deep in the ML platform weeds?
[756.28 --> 761.48]  And because AI is now the new rage, they call themselves an AI engineer.
[761.68 --> 764.34]  So I don't know about that, but it's at the top.
[764.54 --> 765.28]  I think it's the same.
[765.82 --> 765.96]  Yeah.
[766.10 --> 773.60]  I think people use AI, ML, and before it really fell out of vogue, deep learning interchangeably.
[774.40 --> 775.76]  Yeah, exactly.
[776.12 --> 780.88]  I don't know if it's also maybe connected to the fact like Chris and I talked about this,
[780.88 --> 786.36]  I believe it was maybe last week, the fact that some of the disillusionment around AI
[786.36 --> 793.50]  is sort of the realization that turns out AI is integrated in software and you still have
[793.50 --> 796.34]  to do engineering to like build software.
[797.02 --> 802.78]  And it doesn't just sort of like having a model is a solution doesn't really like play
[802.78 --> 803.66]  out in reality.
[804.24 --> 808.40]  You mean I can't just buy an AI model and stick it out there and magic things happen?
[808.88 --> 809.16]  Yeah.
[809.16 --> 810.62]  I mean, one would think.
[810.86 --> 811.72]  I'm so disillusioned.
[812.04 --> 812.26]  Yeah.
[813.00 --> 818.10]  It's funny you guys mentioned that too, because I've seen a few people talking about how LLMs
[818.10 --> 819.12]  are not a product.
[819.12 --> 827.12]  You have to build on top of LLMs your product or whatever it is, your service that needs
[827.12 --> 827.68]  to be there.
[827.78 --> 831.30]  So you can't look at an LLM as a product per se.
[831.90 --> 838.24]  And then I've also seen, or I've been thinking deeply about something that is like the companies
[838.24 --> 842.94]  that are really getting a ton of value out of this AI movement.
[842.94 --> 850.40]  I'm thinking about one of my friends' companies who does like a support software.
[851.00 --> 858.38]  And now he's leveraging AI and LLMs for creating like multi-agents and helping answer feedback
[858.38 --> 861.82]  or answer questions and queries for support.
[861.82 --> 864.52]  And he's using AI.
[864.52 --> 865.46]  That's awesome.
[865.56 --> 870.54]  He's able to sell that support product to companies really well.
[870.78 --> 879.70]  What I haven't seen is companies that say, hey, I am fraud detection as a service.
[879.70 --> 886.12]  And I'm going to sell you this, whatever traditional ML product as a service.
[886.22 --> 894.32]  Whereas you can create regular business unit products as a service that leverage AI, but
[894.32 --> 898.90]  you can't quite, or at least I haven't seen anybody crack the nut, create some kind of
[898.90 --> 902.98]  a traditional ML service type of product.
[903.22 --> 904.54]  I don't know if you guys have seen that.
[904.62 --> 907.52]  And I also don't know if I'm making much sense right now because it's something that's
[907.52 --> 909.80]  relatively fresh in my mind.
[910.42 --> 911.68]  I'm going to turn that one over to Daniel.
[913.64 --> 918.68]  So no, I wasn't making much sense, I guess is what the nice way of saying it is.
[919.68 --> 927.12]  I mean, so you've got like, what I would say is the things that I have seen most are either
[927.12 --> 928.46]  what you were talking about.
[928.46 --> 937.50]  So utilizing generative AI embedded in the functionality of sort of domain specific applications.
[937.52 --> 943.68]  like the customer service you're talking about or financial services or whatever, or access
[943.68 --> 947.92]  to models over some API infrastructure, right?
[948.44 --> 955.18]  There's maybe less like general, I guess maybe the biggest one I've seen is sort of just general
[955.18 --> 957.18]  like fine tuning as a service.
[957.18 --> 962.04]  If you look at something like, you know, open pipe or something like that, but that's still
[962.04 --> 963.24]  fairly general purpose.
[963.24 --> 967.68]  It's not specific to any sort of use case that you might use.
[967.68 --> 972.62]  Maybe to some degree, you know, certain rag services would fit into that.
[972.84 --> 978.18]  Like we were talking to Pinecone about their recent, like they have more kind of prebuilt
[978.18 --> 984.66]  things to have you do kind of like load in all your documents and have rag set up and
[984.66 --> 985.56]  all that stuff.
[985.68 --> 986.86]  So I don't know.
[986.90 --> 990.62]  That's maybe the closest that I've seen to that sort of scenario.
[990.62 --> 991.06]  Yeah.
[992.26 --> 998.26]  Well, also the big question is everybody wants to, and this kind of ties back into the hype
[998.26 --> 998.64]  cycle.
[999.32 --> 1004.38]  Everybody wants to be doing rag and wants to have all these great use cases with their
[1004.38 --> 1004.72]  rag.
[1004.84 --> 1009.16]  And so like you were talking about with Pinecone, they make it really easy for you to do your
[1009.16 --> 1009.76]  rag.
[1009.76 --> 1019.04]  But then at the end of the day, is that a viable business or is that actually super useful as
[1019.04 --> 1026.70]  opposed to somebody's got this support software that they can come in and really cut down the
[1026.70 --> 1032.12]  burden for your customer success engineers or your customer success people.
[1032.12 --> 1037.64]  And that is fascinating to me because it's a booming business right now.
[1038.28 --> 1039.94]  The rag business, maybe.
[1040.18 --> 1041.08]  Yeah, that's great.
[1041.22 --> 1042.78]  Maybe there's some interest there.
[1042.94 --> 1043.82]  Is it a booming business?
[1043.90 --> 1044.28]  I don't know.
[1044.32 --> 1045.12]  I haven't seen numbers.
[1045.64 --> 1053.16]  But I think the really fascinating part to me is if you try to juxtapose that with like
[1053.16 --> 1060.52]  a fraud detection as a service type of product, I just haven't seen that anywhere because I
[1060.52 --> 1070.98]  think, A, you're not able to really like give away everything as freely and B, what works for
[1070.98 --> 1076.66]  one fraud detection use case doesn't necessarily, it's not like you can productize that and then
[1076.66 --> 1079.36]  go out and sell it as a service in my opinion.
[1079.36 --> 1087.40]  So this is a little bit of a tangent, I know, but all that to say is we're at peak hype for
[1087.40 --> 1088.32]  AI engineers.
[1089.16 --> 1090.60]  Peak hype, yes.
[1090.90 --> 1094.96]  So I'm going to draw us back over to the hype cycle just for a moment and I want to read,
[1095.20 --> 1096.86]  I'm going to do something boring for a moment.
[1096.98 --> 1101.44]  I'm going to read off the things where they are for our listeners because the three of us
[1101.44 --> 1105.08]  have the benefit, obviously, of seeing the graph in front of us and for listeners who aren't.
[1105.50 --> 1109.34]  So I'm going to take a moment and then we can go back and start hitting them there.
[1109.36 --> 1116.22]  Very quickly, heading up the curve initially, the innovation trigger, we have autonomic systems,
[1116.60 --> 1123.52]  we have quantum AI, we have first principles AI, we have embodied AI, multi-agent systems,
[1123.92 --> 1133.02]  AI simulation, causal AI, AI-ready data, decision intelligence, neurosymbolic AI, composite AI,
[1133.70 --> 1136.42]  artificial general intelligence, otherwise known as AGI.
[1136.42 --> 1139.52]  And then we're hitting the peak of inflated expectations.
[1139.52 --> 1146.28]  At the top of that hype cycle, we have sovereign AI, AI trism, prompt engineering, responsible AI,
[1146.58 --> 1148.74]  and at the very peak, AI engineering.
[1148.92 --> 1155.12]  And then starting to slide down, we have edge AI, foundation models, synthetic data, model ops,
[1155.42 --> 1156.38]  and generative AI.
[1156.66 --> 1163.00]  And just going into the trough of disillusionment is neuromorphic computing, smart robots followed
[1163.00 --> 1165.24]  at the bottom by cloud AI services.
[1165.74 --> 1172.06]  And then we slide up the slope of enlightenment to autonomous vehicles, knowledge graphs, intelligent
[1172.06 --> 1172.70]  applications.
[1173.16 --> 1178.06]  And finally, the singular one on the plateau of productivity, which is where you want to end
[1178.06 --> 1182.22]  up, is computer vision, which is basically, yeah, we can do that.
[1182.48 --> 1184.28]  It's boring and no one talks about it anymore.
[1184.28 --> 1185.50]  But hey, we're making money.
[1185.50 --> 1191.56]  So if the listeners out there are not confused.
[1192.02 --> 1192.84]  Oh, there's a whole bunch.
[1192.92 --> 1194.42]  I don't have any idea what they are.
[1195.30 --> 1199.38]  I was going to say, which ones do you actually know what they are?
[1199.48 --> 1201.28]  Because what the hell is embodied AI?
[1201.46 --> 1204.48]  Oh, I learned what that is after I put out the post.
[1204.66 --> 1209.14]  So someone said, oh, yeah, embodied AI is when you use AI in robots.
[1209.40 --> 1209.86]  It is.
[1210.14 --> 1210.60]  So yeah.
[1210.60 --> 1214.42]  But there's also smart robots on the cycle.
[1214.82 --> 1217.16]  And I used it at a former employer.
[1217.64 --> 1220.92]  I was specifically doing AI systems in robots.
[1220.92 --> 1222.10]  And I've never heard of it.
[1222.16 --> 1223.64]  You never called it embodied AI?
[1223.78 --> 1225.00]  Well, it's been a few years.
[1225.08 --> 1225.92]  I'll give you that.
[1226.12 --> 1227.02]  It was so.
[1227.44 --> 1228.82]  But no, we weren't calling it embodied.
[1229.16 --> 1233.32]  I mean, so I think I'm at like a 30% hit rate on these.
[1233.48 --> 1239.22]  And I really would love to know what first principles AI is, because that feels like buzzword bingo
[1239.22 --> 1240.30]  to the fullest.
[1240.30 --> 1241.20]  I don't know.
[1241.86 --> 1242.62]  Let's see.
[1242.86 --> 1243.18]  First.
[1243.50 --> 1243.74]  Yeah.
[1244.02 --> 1244.76]  Daniel's going.
[1245.02 --> 1245.64]  He's cheating.
[1246.26 --> 1248.28]  He's going to models to find out.
[1248.48 --> 1248.58]  He's.
[1249.08 --> 1255.34]  The car AI generated card in my Google search says when applied to AI, first principles
[1255.34 --> 1261.16]  AI suggests developing AI systems and algorithms by understanding the foundational principles
[1261.16 --> 1264.50]  of machine learning, neural networks and data science from the ground up.
[1265.12 --> 1266.92]  Don't we do that anyway when we're.
[1266.92 --> 1271.10]  Isn't that kind of inherent in training new models and stuff?
[1272.24 --> 1274.40]  Oh, but no, no, we're really going back.
[1274.48 --> 1276.16]  We're going back to the very first ones.
[1276.24 --> 1277.62]  You're at the second or third principle.
[1277.96 --> 1278.52]  We're beating you.
[1278.70 --> 1278.82]  Yeah.
[1278.92 --> 1279.22]  No.
[1279.22 --> 1284.68]  Because all you guys that are out there that aren't using first principles, you know, that's
[1284.68 --> 1286.74]  lower down on the hype cycle.
[1286.88 --> 1287.16]  Okay.
[1287.38 --> 1288.18]  Oh, this is.
[1289.04 --> 1289.18]  Yeah.
[1289.18 --> 1293.68]  So the other pieces, I mean, were there any other surprises for you guys?
[1293.68 --> 1296.70]  Because I have so many other pieces on here that I'm like, what?
[1297.12 --> 1302.72]  I think for me, like some of these things are themselves correlated and yet in different
[1302.72 --> 1305.10]  places on the chart.
[1305.30 --> 1305.60]  Right.
[1305.86 --> 1314.72]  So it's like if you look at generative AI foundation models, edge AI, AI engineering, prompt
[1314.72 --> 1321.88]  engineering, probably some others on there, all of those like sort of fit into the same
[1321.88 --> 1325.04]  ish bucket and yet are on different sides of the hump.
[1325.60 --> 1326.76]  So, yeah, I don't know.
[1326.86 --> 1330.90]  Like some of these, it's also a matter of where do you draw the boundaries?
[1330.90 --> 1336.72]  Where's the boundary between generative AI and foundation models or generative AI and prompt
[1336.72 --> 1337.22]  engineering?
[1337.22 --> 1342.32]  I'll give you one, you know, as we're at the very bottom on the innovation trigger is
[1342.32 --> 1348.40]  quantum AI and I've, okay, so that's not going to happen anytime soon.
[1348.40 --> 1354.50]  And I will note that they have it on the greater than 10 years, but I would suggest it's probably
[1354.50 --> 1356.62]  greater than greater than 10 years.
[1357.02 --> 1362.30]  But isn't that, I mean, one of the things that's interesting about this whole cycle is
[1362.30 --> 1366.52]  there's that one, maybe you all can tell me or I can look it up.
[1366.52 --> 1367.50]  There's a one law.
[1368.22 --> 1374.74]  It's like a general law that people talk about where you underestimate short term innovation
[1374.74 --> 1378.82]  and overestimate long term innovation or something like that.
[1379.14 --> 1379.46]  Underestimate vice versa.
[1379.82 --> 1380.32]  Yeah, yeah.
[1380.32 --> 1380.54]  Sorry.
[1380.60 --> 1381.34]  I said that backwards.
[1381.52 --> 1381.64]  Yeah.
[1381.74 --> 1389.32]  So it seems like some, like it's hard to, especially the time angle of this, it's hard to, because
[1389.32 --> 1395.48]  things just pop up and you like really didn't see certain things coming and others that you
[1395.48 --> 1397.00]  thought would come don't.
[1397.20 --> 1399.58]  So yeah, it's extremely difficult.
[1400.20 --> 1400.72]  100%.
[1400.72 --> 1408.36]  One thing that I am, just to tag on what you're talking about, Daniel, with the bucketing these,
[1409.24 --> 1413.66]  please tell me what the difference is between an AI engineer and a prompt engineer.
[1413.66 --> 1414.30]  What?
[1414.30 --> 1419.10]  Well, like a prompt engineer is someone that only does prompts, I guess.
[1419.28 --> 1420.70]  And that's all that matters.
[1420.70 --> 1425.04]  So they're just, so I can see how, how it's like, where's the line here?
[1425.04 --> 1429.78]  When prompt engineering came out, Daniel, you might remember, I kind of made fun of that.
[1429.92 --> 1433.68]  I was like the whole, that you talk about like, because people were saying their new
[1433.68 --> 1435.94]  jobs are for prompt engineers and stuff.
[1436.04 --> 1438.76]  And I'm like, that is a passing fad.
[1438.76 --> 1442.58]  Like that will be just so ingrained in what everybody does all the time.
[1442.84 --> 1448.18]  That the notion of there being someone who that's their entire job all the time for years
[1448.18 --> 1449.48]  is not going to happen.
[1449.48 --> 1452.00]  Yeah, I also didn't know.
[1452.46 --> 1458.24]  So like, I've never heard anyone use the word, or if it's a word, it's an acronym, AI
[1458.24 --> 1458.70]  trism.
[1459.46 --> 1461.54]  Do people go around saying that?
[1461.82 --> 1461.96]  Yeah.
[1462.00 --> 1462.60]  What is that?
[1462.72 --> 1463.24]  What is it?
[1463.62 --> 1469.78]  So it's, I looked it up and you know what's, what's funny because this is exactly the area
[1469.78 --> 1471.78]  that I'm working in every day.
[1472.52 --> 1477.98]  It's AI trism is tackling trust, risk, and security in AI models.
[1478.56 --> 1479.08]  Okay.
[1479.72 --> 1481.58]  You've never heard that used, have you?
[1481.60 --> 1486.66]  And I've never heard that, but now I feel like I should put it on our website because
[1486.66 --> 1487.36]  it's hyped.
[1487.82 --> 1488.26]  Yeah.
[1488.34 --> 1489.48]  You definitely need there.
[1489.60 --> 1490.16]  That's right.
[1490.16 --> 1496.54]  The funny part is it's almost as hyped as prompt engineering, which you is basically all
[1496.54 --> 1498.68]  you hear about is prompt engineering, right?
[1499.22 --> 1499.40]  Yeah.
[1499.40 --> 1499.54]  Yeah.
[1499.54 --> 1500.34]  They're right there together.
[1500.50 --> 1502.58]  AI trism you never hear about.
[1503.10 --> 1503.26]  Yeah.
[1503.48 --> 1504.26]  There you go.
[1504.74 --> 1507.62]  Uh, but the trism it's, it's out there.
[1507.72 --> 1508.34]  It is.
[1508.34 --> 1513.64]  We hear about, you know, the, the components that make that up all the time.
[1513.68 --> 1513.94]  Sure.
[1514.22 --> 1517.60]  But just never the, and I've never heard them put together that way.
[1517.60 --> 1521.92]  And I'm sure there are people that are out there that, that, you know, their focus is
[1521.92 --> 1522.72]  in the, that area.
[1522.72 --> 1524.46]  And they're like, of course it's trism, honey.
[1524.46 --> 1525.48]  But yeah, guess what?
[1525.64 --> 1526.62]  Most of us don't know that.
[1526.96 --> 1528.14]  No, not at all.
[1528.46 --> 1533.70]  I don't even know if I go and I just look at this, I don't know what causal AI is.
[1533.86 --> 1538.10]  I don't know what the AI simulation is.
[1538.48 --> 1541.56]  The multi-agent I do understand.
[1541.56 --> 1546.16]  But then like, even when you say quantum AI, I don't know what that is.
[1546.16 --> 1554.70]  The one that I would say is probably in the wrong spot is synthetic data.
[1554.84 --> 1560.92]  It feels like that should be still going up on the hype train because we're just discovering
[1560.92 --> 1562.60]  what we can do with synthetic data.
[1563.10 --> 1573.66]  And every week I feel like we unlock new use cases and synthetic data is just a, it's the
[1573.66 --> 1575.42]  gift that keeps on giving in my eyes.
[1576.26 --> 1583.00]  I think that's the difference in you who actually does it and somebody at Gardner, you know,
[1583.12 --> 1588.20]  who was tasked to go put the chart together and doesn't actually do the thing in real life.
[1588.28 --> 1590.26]  I've, I've terribly offended somebody out there.
[1590.92 --> 1593.44]  Well, we're glad that it's out there.
[1593.52 --> 1598.44]  Let's just say that we are very happy that this exists so we can have a whole episode
[1598.44 --> 1599.96]  dedicated to breaking it down.
[1600.14 --> 1600.46]  Yes.
[1600.60 --> 1602.10]  It's a conversation starter.
[1602.56 --> 1603.48]  That's what I mean.
[1603.56 --> 1606.06]  Like achievement made.
[1607.14 --> 1607.50]  Unlocked.
[1607.50 --> 1613.08]  So one thing that I noticed isn't there at all, which really surprises me given how much
[1613.08 --> 1615.84]  it's bantered about is ethical AI.
[1616.30 --> 1617.48]  It's not on the chart.
[1617.76 --> 1619.20]  And that doesn't go in the trism?
[1619.72 --> 1620.30]  That's not one of the trisms?
[1620.30 --> 1620.92]  Maybe it does.
[1621.08 --> 1625.92]  Maybe this is where I, you know, is ethical AI now transformed from a labeling standpoint
[1625.92 --> 1626.76]  into trism?
[1626.94 --> 1628.26]  Is that, is that where we're going?
[1628.34 --> 1628.84]  I don't know.
[1628.94 --> 1633.74]  Or what is the overlap between responsible AI trism and ethical AI?
[1634.30 --> 1634.60]  Okay.
[1635.08 --> 1635.30]  Well.
[1635.62 --> 1635.84]  Yeah.
[1635.94 --> 1636.08]  I don't.
[1636.08 --> 1641.50]  And there isn't really anything on here about GPUs or hardware.
[1641.50 --> 1649.62]  So I think that's because they made their own hype cycle for GPUs.
[1649.62 --> 1650.24]  That's right.
[1650.34 --> 1655.52]  If I'm not mistaken, I feel like I've seen that somewhere on the internet.
[1655.52 --> 1657.58]  You'd be cannibalizing your other chart.
[1657.90 --> 1658.34]  Exactly.
[1658.34 --> 1662.80]  So you can't put any GPU hardware, anything on the AI one.
[1662.88 --> 1666.44]  You got to refer people to the GPU hype cycle.
[1667.02 --> 1669.04]  And maybe it's like that with ethical AI.
[1669.22 --> 1671.68]  Like they made a whole other ethical AI chart.
[1671.80 --> 1674.36]  That is the hype cycle for ethical AI.
[1674.36 --> 1675.08]  Maybe so.
[1675.46 --> 1676.62]  I'm not familiar with it.
[1676.70 --> 1677.96]  How many charts can you make?
[1678.50 --> 1680.12]  That's if you're Gardner, I guess.
[1680.90 --> 1685.52]  I mean, we have just the artificial intelligence hype cycle here, but they probably have.
[1685.76 --> 1690.24]  I think I've seen multiple, you know, subdivisions and stuff out there.
[1690.62 --> 1692.90]  That's why it's a great business to be in.
[1693.08 --> 1695.70]  Gardner's selling all these different hype cycles.
[1696.52 --> 1703.62]  Well, speaking of what to hype, what's not on the hype cycle, but should be.
[1703.62 --> 1704.44]  All right.
[1704.58 --> 1711.98]  If I could have talked to somebody at Gardner before they were making this, I would have advised.
[1712.52 --> 1715.96]  And so this is my, basically, this is my video job interview right now.
[1716.12 --> 1718.12]  I'm busy typing an invoice up for you to send to them.
[1718.22 --> 1718.36]  Okay.
[1718.56 --> 1719.00]  Just for you.
[1719.08 --> 1719.40]  All right.
[1719.74 --> 1720.18]  Exactly.
[1720.52 --> 1722.42]  I would have advised AI Gateway.
[1723.00 --> 1726.32]  That is very popular.
[1726.44 --> 1733.58]  That's climbing the hype cycle right now because people really like to have the option to
[1733.58 --> 1734.50]  hit an AI Gateway.
[1735.16 --> 1743.08]  And if it is not that complex of a query, you don't need to hit GPT-4.
[1743.40 --> 1745.32]  You don't need the most expensive model.
[1745.54 --> 1751.50]  If you have some kind of open source model that is cheap, then let the simple query go
[1751.50 --> 1752.68]  to that 7B model.
[1752.68 --> 1756.34]  And so I've been hearing people call it an AI Gateway.
[1756.76 --> 1760.52]  Others, I think, have called it like a LLM proxy.
[1760.72 --> 1760.86]  Router.
[1760.96 --> 1761.16]  Maybe.
[1761.54 --> 1762.14]  Or router.
[1762.34 --> 1762.50]  Yeah.
[1762.54 --> 1763.24]  That's another one.
[1763.38 --> 1769.84]  So we would have to agree on the actual name, but that's gaining hype for sure.
[1770.90 --> 1771.10]  Yeah.
[1771.32 --> 1771.80]  Agreed.
[1772.02 --> 1772.28]  Yeah.
[1772.66 --> 1775.02]  I've definitely seen the router language.
[1775.02 --> 1782.90]  Whatever it is, the languages overlap with networking, which is basically like you're just
[1782.90 --> 1784.48]  routing API calls.
[1784.80 --> 1785.76]  So I guess that makes sense.
[1786.66 --> 1786.78]  Yeah.
[1787.16 --> 1790.76]  Any that you guys would have liked to have seen on here and where?
[1791.40 --> 1792.32]  I had the ethical.
[1792.58 --> 1794.50]  I'm still wondering what composite AI is.
[1794.56 --> 1795.56]  Did we ever get that answered?
[1795.78 --> 1798.26]  Or am I having a senior moment or something?
[1798.26 --> 1798.82]  What is it?
[1798.90 --> 1799.10]  Yeah.
[1799.10 --> 1799.86]  What is it?
[1800.56 --> 1806.64]  The one that really stands out to me, unless I'm just like, there's a lot of words on this
[1806.64 --> 1808.64]  page, so maybe I'm totally missing it somewhere.
[1809.32 --> 1811.50]  But where is multimodal AI?
[1811.50 --> 1811.82]  Oh, yeah.
[1811.94 --> 1813.72]  Oh, good catch there.
[1814.70 --> 1815.96]  It's not on here, is it?
[1816.88 --> 1817.18]  No.
[1817.28 --> 1818.28]  Who cares about multimodal?
[1818.28 --> 1818.82]  That's so weird.
[1819.28 --> 1822.10]  That should be in the peak of inflated expectations.
[1822.10 --> 1826.74]  This is like the thing of 2024, like multimodal AI.
[1827.30 --> 1828.14]  That's so funny.
[1828.14 --> 1833.84]  Even multimodal rag should be on here, like climbing the innovation trigger.
[1834.26 --> 1838.12]  Multimodal models should be on the peak of inflated expectations.
[1838.80 --> 1840.38]  That is such a good catch.
[1840.74 --> 1845.08]  I know tons of people who say multimodal and have no idea what it means.
[1845.74 --> 1847.34]  Well, what does it mean, Chris?
[1849.50 --> 1850.64]  Quiz time.
[1850.64 --> 1857.64]  Well, it's having different mobilities of input there so that you can combine different inputs
[1857.64 --> 1860.98]  to get a rich output, you know, in a very general sense.
[1861.34 --> 1861.90]  I have no idea.
[1862.44 --> 1862.60]  Yeah.
[1862.72 --> 1863.66]  So voice.
[1864.16 --> 1865.08]  I know when I see it.
[1865.08 --> 1865.32]  Photos.
[1865.50 --> 1865.86]  Yeah.
[1866.08 --> 1866.36]  Video.
[1866.76 --> 1867.18]  Photos.
[1867.28 --> 1867.76]  Video.
[1867.90 --> 1868.20]  Yeah.
[1868.20 --> 1869.02]  All the things.
[1869.48 --> 1870.38]  All the things.
[1870.42 --> 1870.92]  Yeah, exactly.
[1870.92 --> 1872.00]  Which is what we want.
[1872.10 --> 1877.68]  I want to throw a bunch of stuff that I have and have a fantastic, just have it sorted
[1877.68 --> 1879.50]  out and give me the best answer.
[1879.88 --> 1884.94]  And even with today's multimodal models, that doesn't happen very well.
[1885.10 --> 1890.62]  There's, I'm often frustrated and disappointed with those outputs.
[1890.62 --> 1893.64]  So yeah, it's, I'm expecting better.
[1894.36 --> 1894.50]  Yeah.
[1894.62 --> 1898.96]  And along those lines, I have two that I would like to have seen.
[1899.38 --> 1903.40]  One is just Transformers in general.
[1903.54 --> 1904.36]  Where's that?
[1904.66 --> 1907.48]  Where are they on this hype cycle?
[1908.08 --> 1912.74]  Because that also feels like, are they climbing or are they going down?
[1912.90 --> 1913.42]  I don't know.
[1913.56 --> 1918.22]  It would be trough of disillusionment heading downward because that it's kind of, we're,
[1918.22 --> 1922.52]  we're, we're past that and people are now talking about post-transformer models, you
[1922.52 --> 1923.28]  know, quite often.
[1923.62 --> 1926.06]  So it's kind of like, yeah, yesterday.
[1926.64 --> 1930.02]  So there needs to be another dot for post-transformer models.
[1930.26 --> 1931.46]  That's definitely going up.
[1931.74 --> 1932.24]  And that's right.
[1933.04 --> 1939.66]  Speaking of which, it feels like, okay, we've got small language models.
[1939.80 --> 1940.30]  Where are they?
[1940.76 --> 1943.58]  Because that is all the rage.
[1943.78 --> 1944.02]  It is.
[1944.02 --> 1951.06]  That was like, and maybe it's all the rage for every vendor who is not open AI because
[1951.06 --> 1954.24]  they can't compete on GPT-4.
[1954.76 --> 1955.72]  And so what do they do?
[1955.80 --> 1960.70]  They say, well, you can just host your own small language model and fine tune it and get
[1960.70 --> 1962.48]  better performance than GPT-4.
[1963.30 --> 1970.12]  And so I think small language models are probably, they should be in that innovation trigger.
[1970.12 --> 1979.16]  Maybe the peak of inflated expectations because anyone who's ever used the 7B model might
[1979.16 --> 1981.98]  not want to use it if they have the choice.
[1983.10 --> 1988.12]  Well, maybe, maybe it's, is it, are you sure that's going up or could it possibly be sliding
[1988.12 --> 1990.26]  into that disillusionment that you just reverted to?
[1990.26 --> 1990.30]  Yeah.
[1990.54 --> 1990.98]  Potentially.
[1991.24 --> 1991.54]  That's true.
[1991.54 --> 1996.90]  Because maybe it is going into the trough of disillusionment, you know, just hypothetically,
[1997.12 --> 2002.10]  because I do think that when it gets to the plateau of productivity, small models will
[2002.10 --> 2005.94]  be those, the, just the workhorse, you know, you'll have them out on the edge everywhere.
[2006.12 --> 2010.90]  Every fricking device you've ever imagined or seen is going to have small models in it
[2010.90 --> 2012.44]  that are inferencing.
[2012.72 --> 2014.90]  We won't ever have anything that doesn't have them.
[2014.98 --> 2016.98]  It'll be just the, oh, yawn.
[2016.98 --> 2019.82]  And of course we have our small models in our watch.
[2020.66 --> 2024.06]  Which leads me to the next one that I'm like, where is this?
[2024.16 --> 2026.08]  Why do they not have wearable AI?
[2026.24 --> 2029.50]  That is a perfect buzzword that should be on here.
[2030.00 --> 2035.62]  And if you look at like what Meta's doing with the glasses, or if you see any of those
[2035.62 --> 2038.32]  necklaces that you can wear and it records everything.
[2038.64 --> 2038.92]  Yeah.
[2039.16 --> 2040.74]  That's wearable AI right there.
[2040.86 --> 2045.28]  I just, I may have just made that up or I may have seen that before, but that one should
[2045.28 --> 2045.76]  be on here.
[2045.76 --> 2046.72]  It should be there.
[2046.84 --> 2047.18]  I agree.
[2047.18 --> 2062.74]  Hey friends.
[2063.06 --> 2069.00]  Outshift, Cisco's incubation engine, merges innovation with the art of possible, a launch
[2069.00 --> 2071.30]  pad for transformative emerging tech.
[2071.30 --> 2076.38]  Outshift blends startup agility with corporate strength to develop next-gen technologies from
[2076.38 --> 2080.44]  the ground up in AI, quantum technologies, cloud native, and more.
[2080.96 --> 2087.34]  Their newest AI innovation, Motific, addresses a critical challenge in the rapidly advancing
[2087.34 --> 2089.02]  world of gen AI.
[2089.36 --> 2095.44]  Bridging the gap between concept and deployment, this model and vendor agnostic solution supports
[2095.44 --> 2097.58]  the entire gen AI.
[2097.58 --> 2104.38]  From assessment and experimentation, Motific accelerates deployment from months to days while safeguarding
[2104.38 --> 2109.00]  against gen AI security, trust, compliance, and cost risks.
[2109.00 --> 2115.92]  All while empowering business function and IT teams to rapidly configure end-user assistance powered
[2115.92 --> 2117.54]  by organizational data.
[2117.96 --> 2123.50]  Motific provides advanced, customizable policy controls to prevent unauthorized access to
[2123.50 --> 2127.86]  sensitive data and helps ensure compliance throughout the entire process.
[2127.86 --> 2137.66]  With deep visibility into operational and business metrics, Motific enables you to track ROI, optimize costs, and make informed decisions.
[2138.16 --> 2145.60]  By offering a centralized view, Motific deters shadow AI usage and empowers teams to innovate responsibly.
[2146.08 --> 2150.42]  So move beyond the traditional constraints of AI implementation.
[2150.42 --> 2155.78]  Utilizing AI deployment that is both responsible and is revolutionary.
[2156.48 --> 2162.20]  Ensuring your projects are not just quickly launched, but built on a foundation of trust and efficiency.
[2162.20 --> 2164.56]  Visit Motific.ai.
[2164.72 --> 2169.34]  That is M-O-T-I-F-I-C dot A-I.
[2180.42 --> 2189.32]  Maybe this fits into kind of the agentic stuff that is represented in certain ways on there.
[2189.32 --> 2197.38]  But this whole idea of whatever, you know, like tool function calling slash like text to SQL,
[2197.94 --> 2203.30]  like interacting with structured databases, APIs, whatever that is.
[2203.30 --> 2210.30]  I don't know like the maybe the general name for that other than tool and function calling or text to SQL.
[2210.62 --> 2220.38]  But certainly that's like sliding into a zone where people are definitely doing some of those things in production and there's products released around it.
[2220.78 --> 2224.86]  So like the hex magic stuff and all that other.
[2225.28 --> 2227.48]  Where is it on the chart, though, before we go on?
[2227.66 --> 2228.76]  Oh, where is it on the chart?
[2228.76 --> 2234.32]  I mean, it's got to be somewhere somewhere around AI engineering.
[2234.96 --> 2235.92]  So it's at the peak of it.
[2237.18 --> 2238.08]  Maybe maybe.
[2238.38 --> 2239.54]  Yeah, I don't know.
[2239.64 --> 2239.94]  I don't know.
[2240.00 --> 2240.50]  It might be.
[2240.76 --> 2245.04]  Maybe it's going down because people are like agents aren't reliable.
[2245.42 --> 2246.14]  I think that's right.
[2246.18 --> 2248.30]  I think it's heading down into the drop of disillusionment.
[2248.38 --> 2249.10]  That's where I would guess.
[2249.32 --> 2249.54]  Yeah.
[2250.44 --> 2250.70]  Yeah.
[2251.04 --> 2256.76]  And if you compare that to where they have it, multi-agent systems, it's got a long way to go up.
[2256.76 --> 2259.48]  It is at the very bottom of this hype cycle.
[2260.38 --> 2265.56]  So, yeah, I think we instinctively are like, no, please, no more agents.
[2267.32 --> 2269.58]  Gardner's like, oh, we're just getting started, baby.
[2270.60 --> 2274.44]  Well, and they're like, no, please, more agents together.
[2274.90 --> 2275.76]  Multi-agents.
[2276.88 --> 2280.12]  Gardner's going to create their own agent hype cycle next.
[2280.32 --> 2282.52]  That's going to be the next one that they can create.
[2282.52 --> 2282.88]  Maybe.
[2283.08 --> 2288.82]  And so we'll, you know, take a commission for giving you that idea, Gardner.
[2288.98 --> 2290.24]  No problem there.
[2291.18 --> 2294.64]  One thing, can we call out the elephant in the room?
[2294.70 --> 2299.10]  Because where is retrieval augmented generation on?
[2299.10 --> 2299.26]  Yeah.
[2300.22 --> 2300.52]  Yeah.
[2300.86 --> 2302.24]  How is that not on here?
[2302.26 --> 2302.54]  Really?
[2302.68 --> 2302.84]  Yeah.
[2303.32 --> 2303.66]  Rag?
[2303.78 --> 2304.28]  What's that?
[2304.40 --> 2305.44]  Because I was thinking about it.
[2305.44 --> 2311.24]  I was thinking about it and I was like, oh, you know what they missed is graph rag.
[2311.52 --> 2314.14]  That is all the hype these days.
[2314.14 --> 2314.32]  Yeah.
[2314.32 --> 2320.90]  And that's probably right around where sovereign AI is, where it's maybe like at the border.
[2321.30 --> 2321.58]  It's nearing the peak.
[2321.94 --> 2322.26]  Yeah.
[2322.40 --> 2322.60]  Yeah.
[2322.60 --> 2325.92]  It's going up nearing the peak of inflated expectations.
[2326.18 --> 2326.52]  You're right.
[2326.66 --> 2327.88]  More hype than the trism.
[2328.52 --> 2328.76]  Yeah.
[2328.86 --> 2330.06]  More hype than the trism.
[2330.58 --> 2333.90]  But I would argue rag is heading to the trough of disillusionment.
[2333.90 --> 2335.26]  Anyone want to disagree with that?
[2335.34 --> 2335.68]  No, no.
[2335.74 --> 2336.44]  I think so too.
[2336.56 --> 2337.72]  I think it's over the hump.
[2338.26 --> 2338.38]  Yeah.
[2338.40 --> 2338.90]  I do too.
[2339.26 --> 2343.80]  I mean, it's, and people are kind of hitting the challenges and, and, and, you know, and
[2343.80 --> 2349.72]  actually, uh, Daniel advanced rag, you know, which we've talked about several times, you
[2349.72 --> 2351.16]  know, kind of, kind of trailer.
[2351.28 --> 2352.70]  Well, we don't just have rag now.
[2352.80 --> 2354.16]  We have advanced rag.
[2354.24 --> 2354.42]  Yeah.
[2354.42 --> 2359.68]  And, and, you know, as things are starting to head over that peak of inflated expectations
[2359.68 --> 2361.40]  with rag and you, well, guess what?
[2361.42 --> 2362.34]  We can juice some more.
[2362.34 --> 2362.74]  Yeah.
[2362.74 --> 2363.80]  We have advanced rag.
[2364.42 --> 2368.46]  But I think, I think the whole thing is starting to go over the side and, you know, people
[2368.46 --> 2372.84]  are like, okay, well, we've kind of done at least the easy stuff, uh, to the advanced
[2372.84 --> 2373.48]  rag point.
[2373.76 --> 2378.88]  There are people that are, that are doing it better than others, but nonetheless, you know,
[2378.96 --> 2381.18]  it's, you know, what's next.
[2381.26 --> 2384.22]  So what, what, I'm just curious, two second deviation.
[2384.68 --> 2387.04]  We've talked about, you know, fine tuning.
[2387.16 --> 2388.72]  We've talked about rag.
[2389.18 --> 2391.82]  What's coming next in that, in that sphere?
[2391.82 --> 2393.10]  What, what are they missing there?
[2393.28 --> 2393.48]  Yeah.
[2394.40 --> 2395.36]  A new model.
[2396.06 --> 2396.44]  Yeah.
[2396.44 --> 2404.00]  I think you mentioned that you might've had some of these Demetrius, uh, what are AI hyped
[2404.00 --> 2411.68]  items that are your own, that you've come up with a name for that other people will have
[2411.68 --> 2416.22]  to interpret to figure out their definition?
[2416.22 --> 2418.16]  You want to, you want to guess?
[2418.38 --> 2418.68]  Yes.
[2418.82 --> 2419.50]  On this one.
[2419.60 --> 2420.34]  All right, here we go.
[2420.54 --> 2425.10]  I am going to start you off with, uh, with a pretty simple one.
[2425.20 --> 2427.66]  This one is free range AI.
[2428.96 --> 2429.92]  Free range.
[2430.20 --> 2433.00]  Is that, is that open access LLMs?
[2433.86 --> 2434.30]  Close.
[2434.78 --> 2435.14]  Close.
[2435.24 --> 2435.96]  What do you got, Chris?
[2436.04 --> 2436.74]  Grain fed.
[2437.36 --> 2439.50]  I can't get off the free range thing.
[2439.56 --> 2440.36]  I'm an animal guy.
[2440.36 --> 2443.52]  I can't even, I can't even get into the AI headspace on this one.
[2444.48 --> 2447.50]  That's AI that was trained without guardrails.
[2447.74 --> 2448.22]  Okay.
[2448.64 --> 2449.04]  Gotcha.
[2449.04 --> 2449.40]  Okay.
[2449.50 --> 2450.14]  I like that.
[2450.70 --> 2457.14]  Well, we, we already talked about, about one here, um, that, that you alluded to Demetrius,
[2457.20 --> 2459.60]  but my name for it was trinket AI.
[2461.20 --> 2461.68]  Wearables.
[2462.30 --> 2462.78]  Yes.
[2463.04 --> 2463.52]  Yeah.
[2463.92 --> 2464.38]  Yes.
[2464.70 --> 2465.78]  Trinket AI.
[2466.36 --> 2466.70]  Trinket AI.
[2466.70 --> 2466.82]  Yeah.
[2466.82 --> 2468.80]  Imagine it's, it's in your fidget spinner.
[2468.80 --> 2470.24]  That sounds a lot.
[2470.34 --> 2470.52]  Right.
[2470.66 --> 2472.86]  That's a much better name than wearable AI.
[2473.00 --> 2473.14]  Yeah.
[2473.68 --> 2473.86]  Yeah.
[2473.98 --> 2474.80]  Trinket AI.
[2475.80 --> 2476.54]  It is.
[2476.64 --> 2480.60]  Every little thing you have on your body has a fricking model in front single on it,
[2480.62 --> 2485.14]  you know, or you're, and it doesn't bring you any extra value.
[2485.64 --> 2488.16]  We're going to follow the AI trend.
[2488.66 --> 2490.28]  You just don't have to think anymore.
[2490.44 --> 2493.12]  You can click that button and take a picture, Demetrius.
[2493.32 --> 2498.38]  No, it just gives you some verbose answer to a question that you didn't really ask.
[2498.80 --> 2503.40]  And so your shirt is, you're like, Hey, have I been sweating?
[2503.40 --> 2510.02]  And then it tells you the origin of sweat in a three page PDF that you have to go download.
[2511.10 --> 2512.98]  Well, do I get senior moment AI?
[2513.36 --> 2514.50]  That would be good for me.
[2514.58 --> 2516.60]  You know, I, I, there's a huge market for that.
[2517.04 --> 2522.38]  Everybody over the age of, you know, 50 is going to buy senior moment AI to, to, you know,
[2522.38 --> 2523.28]  like what, what, what?
[2523.28 --> 2524.84]  Oh, and it, oh, there we go.
[2524.84 --> 2528.68]  And you know, I can, I can continue instead of pausing for the next three minutes to try
[2528.68 --> 2530.50]  to figure out what it was I was about to do.
[2530.98 --> 2538.22]  Or I was thinking that that's a, how seniors interface with AI so they don't get left behind.
[2538.56 --> 2543.86]  It's like, this is the product that will make sure you stay up to date.
[2543.92 --> 2545.30]  You're ahead of the curve.
[2545.30 --> 2546.58]  Okay.
[2547.58 --> 2548.20]  Sounds good.
[2548.70 --> 2548.98]  All right.
[2548.98 --> 2550.20]  I got another one for you all.
[2550.20 --> 2554.62]  This one is EQ AI.
[2555.08 --> 2556.76]  Oh, empathetic AI.
[2557.40 --> 2557.76]  Yeah.
[2557.82 --> 2560.54]  So it's also been known as empathetic AI.
[2560.82 --> 2560.94]  Yeah.
[2561.02 --> 2565.10]  You may hear other people out there and on the streets calling it empathetic AI.
[2565.10 --> 2572.46]  Uh, this one is a type of AI that has high emotional intelligence and it feels empathy
[2572.46 --> 2578.40]  for you when you get frustrated that it's not giving you the right answer and your prompts
[2578.40 --> 2581.58]  aren't working, but it doesn't actually make your prompts work.
[2581.66 --> 2583.58]  It just feels bad for you.
[2584.04 --> 2584.14]  Okay.
[2584.48 --> 2591.48]  I, that minus the AI bit that happened to me yesterday, I was on Comcast on their stupid
[2591.48 --> 2594.72]  text support for four hours texting.
[2595.30 --> 2600.18]  They passed me off and every, everyone was so empathetic, but they accomplished nothing.
[2600.34 --> 2602.86]  If you put that in AI, I'm quitting AI.
[2603.24 --> 2606.84]  If you put that into any AI that does that, I'm just done.
[2607.04 --> 2608.70]  I'm, I'm walking away from the whole field.
[2608.70 --> 2612.68]  Are you sure it wasn't already AI that you were talking to?
[2612.68 --> 2613.14]  It could have been.
[2613.32 --> 2614.74]  I mean, it was just text.
[2614.96 --> 2617.24]  It was only text, but it was horrible.
[2617.66 --> 2619.54]  We've already passed the Turing test.
[2619.94 --> 2621.26]  So it's like they're there.
[2621.26 --> 2623.30]  I'm getting a response of, I'm so sorry.
[2623.38 --> 2624.28]  I'm just very sorry.
[2624.34 --> 2625.26]  We're going to hear to help you.
[2625.30 --> 2627.32]  And I'm like, I'm going to freaking kill you.
[2627.48 --> 2628.02]  You know?
[2628.14 --> 2628.36]  Yeah.
[2628.80 --> 2629.20]  Yes.
[2629.30 --> 2633.22]  That's what four hours texting support will do, but don't do.
[2633.48 --> 2633.70]  Yeah.
[2633.94 --> 2637.14]  I just, if you bring that to AI, it'll ruin the whole thing for me.
[2637.14 --> 2640.80]  Well, this one, funny enough, is actually on the uptick.
[2641.08 --> 2646.22]  When you look at the slope, the EQ AI has got a lot of runway left.
[2647.12 --> 2647.28]  Yep.
[2647.28 --> 2658.02]  Um, so my, my next one is AI, either AI nepotism or AI anti nepotism.
[2658.24 --> 2662.60]  Oh, I don't, I'm trying to make that.
[2662.94 --> 2664.48]  Fighting AI nepotism.
[2664.98 --> 2666.86]  Fighting AI nepotism.
[2667.34 --> 2667.60]  Oh.
[2667.70 --> 2667.84]  Okay.
[2667.84 --> 2670.04]  You're going to have to, you're going to have to go into that one for me.
[2670.12 --> 2670.42]  That's.
[2670.88 --> 2671.70]  I've stopped you.
[2671.84 --> 2671.86]  Yeah.
[2671.86 --> 2672.02]  Yeah.
[2672.36 --> 2672.58]  Yeah.
[2672.66 --> 2673.42]  This is exciting.
[2674.52 --> 2682.60]  It's basically using AI against like the government using AI or what?
[2682.60 --> 2683.64]  No, no.
[2683.88 --> 2685.34]  So, uh, uh.
[2685.34 --> 2687.06]  Foundation model related maybe?
[2687.44 --> 2687.92]  Yeah.
[2688.18 --> 2698.58]  So this would be like multi model AI in that you are not preferential to one language model
[2698.58 --> 2706.84]  family and only using that family, but you are now multi model and, you know, as such
[2706.84 --> 2708.72]  not practicing nepotism.
[2709.12 --> 2710.78]  But are you multi model, multi model?
[2713.28 --> 2714.76]  This is also, maybe not.
[2714.92 --> 2718.60]  You know, I knew it by its other name, uh, which is polygamy AI.
[2720.00 --> 2720.56]  Yes.
[2720.64 --> 2721.24]  Oh gosh.
[2721.24 --> 2722.64]  Where am I going?
[2725.10 --> 2731.62]  No, or, or some in San Francisco call it polyamorous AI as it tends to be.
[2732.14 --> 2736.48]  So the, the next one that I've got for you.
[2736.58 --> 2739.72]  Oh, where is this nepotism AI on the hype cycle, by the way?
[2740.42 --> 2742.84]  Uh, I think it's still a bit on the rise.
[2742.96 --> 2745.82]  I saw a 16 Z and they're in their post.
[2745.90 --> 2748.26]  One of the things they called out was multi model future.
[2748.26 --> 2749.00]  Oh yeah.
[2749.00 --> 2750.96]  Uh, there's a future for this one.
[2751.10 --> 2751.88]  That is for sure.
[2753.48 --> 2759.38]  So I've got one that is called broccoli AI.
[2759.96 --> 2760.42]  Okay.
[2760.78 --> 2762.42]  This one's, this one's going down.
[2762.42 --> 2764.68]  Is it related to some sort of graph thing?
[2765.48 --> 2767.50]  No, but that could be nice.
[2767.64 --> 2767.78]  Yeah.
[2768.20 --> 2770.04]  Is it synonymous with healthy AI?
[2770.42 --> 2770.74]  Yeah.
[2770.96 --> 2771.70]  Yeah, exactly.
[2771.84 --> 2774.30]  Maybe you've heard it termed healthy AI.
[2775.12 --> 2775.52]  Efficient.
[2776.82 --> 2777.26]  Yeah.
[2777.26 --> 2778.22]  It's sustainable.
[2779.00 --> 2779.30]  No.
[2779.46 --> 2784.76]  So, Oh, that's another one that I've got though, but we'll get to that in a minute, which,
[2784.96 --> 2789.80]  which reminds me like, it does feel like sustainable AI should have been on the real hype cycle.
[2789.80 --> 2791.42]  Like that's an actual term, isn't it?
[2791.42 --> 2792.14]  Yes, it is.
[2792.20 --> 2792.78]  And it's not.
[2792.98 --> 2793.86]  And it's not on there.
[2793.98 --> 2797.54]  The other one that should have been on there that I was like, why isn't it on there?
[2797.54 --> 2802.08]  Is ensemble AI that feels like, or ensemble models.
[2802.24 --> 2803.70]  That feels like it should have been on there.
[2803.70 --> 2808.90]  See, one of the ones that I looked up was composite AI.
[2809.24 --> 2809.32]  Yeah.
[2809.32 --> 2810.26]  That's the one I didn't know.
[2810.34 --> 2811.76]  I think, well, I don't know.
[2811.84 --> 2817.50]  It's slightly different than ensemble, but I think that they like composite was combining
[2817.50 --> 2822.76]  multiple, multiple AIs together in some way or another.
[2822.76 --> 2827.74]  For one inference, like you have multiple, you know, models inferencing, but you have
[2827.74 --> 2829.92]  one inference back out to the user.
[2830.44 --> 2830.62]  Yeah.
[2830.70 --> 2831.68]  Something like that.
[2831.80 --> 2832.30]  I don't know.
[2832.72 --> 2839.46]  Although ensemble could very, yeah, very much mean for a single inference getting a majority
[2839.46 --> 2841.02]  vote or something like that.
[2841.14 --> 2841.32]  Okay.
[2841.32 --> 2845.18]  So it would be where composite AI is on the chart if they're assuming they're correct.
[2845.64 --> 2845.84]  Yeah.
[2845.84 --> 2849.30]  And before we leave it, sustainable AI, where is it on the chart?
[2849.72 --> 2852.86]  That's very much like, it's got a lot of hype to go.
[2853.36 --> 2853.62]  Yeah.
[2853.62 --> 2857.54]  I think it's low to mid-level, mid-level on the curve up.
[2857.86 --> 2858.12]  Yeah.
[2858.92 --> 2859.18]  Okay.
[2859.46 --> 2863.98]  Just think about how many people are talking about the energy that is wasted training the
[2863.98 --> 2864.84]  foundational models.
[2865.52 --> 2865.70]  True.
[2865.70 --> 2870.26]  And how we need to build out all these data centers and they need to be sustainable, et cetera,
[2870.34 --> 2870.60]  et cetera.
[2870.60 --> 2875.66]  So yeah, sustainable AI for sure has some room to grow.
[2875.88 --> 2880.34]  Back to broccoli AI, aka healthy AI.
[2880.72 --> 2884.36]  This is AI, and this is very much on the downslope again.
[2884.82 --> 2886.92]  It has passed its peak.
[2887.46 --> 2893.36]  People are a little disillusioned with it because it's AI that doesn't taste good for the organization,
[2893.66 --> 2894.76]  but it's needed.
[2895.66 --> 2900.58]  And so you can imagine the cybersecurity folks, they love this kind of AI.
[2900.60 --> 2907.20]  Is this like a linear regression model or what would you consider good for an organization?
[2907.34 --> 2908.54]  I think you use the word good.
[2909.08 --> 2909.24]  Yeah.
[2909.54 --> 2910.02]  Healthy.
[2910.44 --> 2914.08]  It's healthy for the, we could go to healthy for the organization.
[2914.66 --> 2915.62]  What could that be?
[2915.72 --> 2924.20]  I mean, I actually didn't get to do enough market research in this section to figure that
[2924.20 --> 2924.72]  part out.
[2924.84 --> 2926.88]  You know, I was just throwing spaghetti at the wall.
[2926.88 --> 2931.04]  But if I were to think about what's healthy, yeah, it would probably be the traditional
[2931.04 --> 2931.44]  ML.
[2931.84 --> 2936.32]  Going back to the, what I was talking about before, like fraud detection is one of those
[2936.32 --> 2939.26]  where it's not really AI.
[2939.44 --> 2942.94]  Some people might know it as its former term, ML.
[2944.02 --> 2944.18]  So.
[2945.56 --> 2949.04]  I'm telling you, they're all the same from a marketing standpoint.
[2949.04 --> 2949.20]  Exactly.
[2949.66 --> 2950.10]  Exactly.
[2950.82 --> 2951.24]  Well, yeah.
[2951.36 --> 2955.36]  The waters are too muddied for them to make any actual difference.
[2955.68 --> 2956.18]  That's right.
[2956.64 --> 2957.40]  So what else you got?
[2957.46 --> 2958.04]  What else you got?
[2958.36 --> 2958.62]  Okay.
[2958.68 --> 2965.16]  So I've got unsustainable AI, which is way different than sustainable AI, just so we're
[2965.16 --> 2965.60]  clear.
[2966.00 --> 2966.62]  An inverse.
[2966.62 --> 2973.56]  But it's not even, it's a whole different sector of the universe that we're talking about.
[2973.68 --> 2977.58]  It's not like, oh, it's just the opposite of sustainable AI.
[2978.02 --> 2983.36]  Unsustainable AI is, it's got, it's at peak hype right now.
[2983.56 --> 2984.32]  Let's be honest.
[2984.36 --> 2989.94]  If I could swap it out with the AI engineer, it is at peak hype because this is AI that was
[2989.94 --> 2992.82]  built for a product demo, but not for scale.
[2993.42 --> 2995.50]  That is unsustainable AI.
[2995.50 --> 2997.46]  It happens all the time.
[2997.96 --> 2998.06]  Yeah.
[2998.26 --> 3003.38]  So anything that you see, basically we can, hopefully none of these guys are your sponsors,
[3003.56 --> 3011.06]  but let's just cue Devin or Rabbit or Humane, all those unsustainable AI.
[3011.76 --> 3012.38]  The trinkets?
[3012.96 --> 3013.90]  The trinkets.
[3014.24 --> 3014.40]  Yeah.
[3014.90 --> 3015.56]  That's true.
[3015.68 --> 3021.30]  So it's sort of analogous to doing like prototyping software where you're never intending to grow
[3021.30 --> 3022.08]  it into production.
[3022.42 --> 3022.92]  Exactly.
[3022.92 --> 3027.16]  So, so that's all of mine that I could think of.
[3027.50 --> 3029.04]  Well, I think that was a pretty good list.
[3029.56 --> 3035.42]  I did realize, I don't know, maybe, maybe related to some of the discussion we had earlier,
[3035.42 --> 3039.26]  but I don't see neighborly AI on here.
[3039.26 --> 3041.30]  That's kind of creepy when you think about it.
[3042.02 --> 3045.78]  I wasn't creeped out until you said that, but.
[3048.24 --> 3053.44]  I had this image of Mr. Rogers' neighborhood, you know, instead of Mr. Rogers, it's the AI.
[3054.10 --> 3055.16]  Hi, girls and boys.
[3055.16 --> 3060.38]  Maybe they can help you clean up a few things with their rags?
[3060.92 --> 3061.16]  It clean.
[3061.28 --> 3061.62]  No.
[3064.52 --> 3065.32]  Oh boy.
[3066.70 --> 3071.40]  Well, I was thinking it was like next door where it was almost like the voting system,
[3071.54 --> 3074.28]  the ensemble, but it was for local LLMs.
[3074.48 --> 3074.60]  Gotcha.
[3075.18 --> 3075.38]  Yeah.
[3075.38 --> 3079.78]  I realized there's nothing about vectors or embeddings on the chart.
[3079.94 --> 3081.24]  I was just thinking about that.
[3081.40 --> 3083.92]  Actually, there's, yeah, there's no vector stores on here.
[3084.04 --> 3087.62]  Or even just general embeddings of any type.
[3087.62 --> 3087.64]  Embedding models.
[3088.04 --> 3088.26]  Yeah.
[3089.38 --> 3091.36]  Wouldn't that be plateau productivity now?
[3091.46 --> 3093.80]  We've had those for so long that they're just.
[3093.80 --> 3094.20]  I don't know.
[3094.88 --> 3096.92]  Lexicon, no emotion left in them.
[3097.44 --> 3097.70]  Yeah.
[3097.84 --> 3104.22]  What I was thinking is they probably aren't on there because Gardner also has one of their
[3104.22 --> 3107.56]  best products ever, the Magic Quadrant.
[3107.56 --> 3111.06]  And that'll be the next episode that I come and drop in on.
[3111.26 --> 3115.50]  We can remake the Magic Quadrant for the different sectors.
[3115.80 --> 3120.24]  And I imagine that they have a Magic Quadrant for vector databases.
[3120.70 --> 3120.96]  Yes.
[3121.32 --> 3122.42]  That sounds delightful.
[3123.26 --> 3123.44]  Yeah.
[3123.44 --> 3128.66]  Well, it has been delightful to have you on, Demetrius.
[3129.24 --> 3135.48]  I'm glad you brought your various new AI terms to the hype cycle.
[3136.20 --> 3141.30]  And now I have some work to do on my broccoli AI.
[3142.04 --> 3144.22]  Incorporate that into your product for sure.
[3144.64 --> 3145.76]  It's right around there.
[3146.32 --> 3146.84]  Trism.
[3147.30 --> 3151.24]  It would be a good AI logo, just like a broccoli floret.
[3151.66 --> 3152.12]  Yeah.
[3152.12 --> 3156.20]  The broccoli or the, I saw a great paper that was all about leaks.
[3156.30 --> 3160.66]  It was all about data leakage when you send API calls to open AI.
[3161.16 --> 3167.20]  And the paper started with a emoji of a leak.
[3167.28 --> 3167.96]  That's awesome.
[3168.04 --> 3168.96]  Like the leaks you eat.
[3169.04 --> 3169.26]  Right.
[3169.26 --> 3180.14]  And it was saying here's, and it was basically showing how you send your data to open AI, but a lot of other people are going to get it too if you're not careful.
[3180.48 --> 3180.78]  Yeah.
[3180.98 --> 3186.64]  Which is one thing that we haven't really touched on, but that seems like it's got some hype around it.
[3186.98 --> 3187.50]  It's what?
[3188.20 --> 3189.54]  Data leakage AI.
[3189.54 --> 3190.44]  Data leakage.
[3190.78 --> 3191.46]  Data poisoning.
[3192.04 --> 3192.56]  Data poisoning.
[3192.56 --> 3195.90]  I know in my day job, that's a common conversation.
[3196.42 --> 3196.58]  Yeah.
[3196.76 --> 3197.54]  Prompt injection.
[3198.08 --> 3198.78]  Should be there.
[3198.78 --> 3199.20]  Prompt injection.
[3200.08 --> 3200.44]  Yes.
[3201.86 --> 3203.84]  I guess this all fits under trism.
[3204.60 --> 3204.92]  Yeah.
[3205.14 --> 3205.64]  This is it.
[3205.76 --> 3207.98]  We're going over trisms right now.
[3209.08 --> 3210.06]  Trisms and trinkets.
[3210.06 --> 3221.02]  On that note, that very profound note, it has been great to discuss all the trisms with you, Demetrius.
[3221.24 --> 3222.30]  I've had a blast as always.
[3222.50 --> 3225.36]  Please, please come back as usual.
[3225.60 --> 3232.16]  Give your own hype about the upcoming event before we close out and where people can find out more about it.
[3232.60 --> 3232.90]  Yeah.
[3232.96 --> 3233.94]  I always feel bad.
[3234.02 --> 3236.12]  I come on here and just show my stuff.
[3236.26 --> 3237.28]  So this time, no shilling.
[3237.28 --> 3239.38]  I've just had a blast doing this with you guys.
[3239.56 --> 3239.68]  Okay.
[3240.06 --> 3245.28]  So if anybody wants to find out about the next virtual conference or the in-person conference,
[3245.44 --> 3248.98]  they can just Google MLOps community and I'm sure it'll pop up.
[3249.54 --> 3249.94]  Cool.
[3250.28 --> 3250.60]  All right.
[3250.70 --> 3252.18]  Hey, much appreciated.
[3252.36 --> 3253.52]  We'll talk to you soon, Demetrius.
[3253.62 --> 3254.00]  Thanks, man.
[3254.08 --> 3254.24]  Yeah.
[3254.34 --> 3254.84]  Thanks, guys.
[3262.42 --> 3263.34]  All right.
[3263.66 --> 3266.02]  That is Practical AI for this week.
[3266.74 --> 3267.86]  Subscribe now.
[3267.86 --> 3273.02]  If you haven't already, head to PracticalAI.fm for all the ways.
[3273.02 --> 3278.34]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire
[3278.34 --> 3279.44]  ChangeLog community.
[3280.02 --> 3284.66]  Sign up today at PracticalAI.fm slash community.
[3284.66 --> 3291.06]  Thanks again to our partners at Fly.io, to our Beat Freakin' Residence, Breakmaster Cylinder,
[3291.30 --> 3292.18]  and to you for listening.
[3292.54 --> 3294.30]  We appreciate you spending time with us.
[3294.72 --> 3295.84]  That's all for now.
[3296.08 --> 3297.76]  We'll talk to you again next time.
[3297.76 --> 3307.82]  We'll talk to you again next time.
[3307.82 --> 3308.74]  Game on!
