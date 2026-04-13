[0.00 --> 4.72]  If you look at technologies for powering AI right now, they're all based on transistors.
[4.92 --> 7.40]  There's never been a computer that's not based on transistors.
[7.66 --> 9.90]  Like this is the way that the world does computation.
[10.54 --> 14.82]  But we've run into this kind of fundamental challenge around shrinking how much energy
[14.82 --> 15.80]  the chips are using.
[16.12 --> 18.02]  And you can't really do that going forward.
[18.38 --> 23.28]  So if you look at the Department of Energy's estimate for energy consumption, 2030, 10%
[23.28 --> 27.36]  of the entire planet's energy consumption will be on compute and interconnect.
[27.36 --> 32.82]  So if we look at 2040, you're talking about most like the overwhelming majority of the
[32.82 --> 33.74]  power being used on this.
[34.06 --> 38.00]  You always have to think in business about the use case that could motivate using that
[38.00 --> 40.66]  much of the planet's power because that would cost a lot of money.
[41.06 --> 44.46]  You will start to see that progress in AI will slow.
[47.26 --> 49.90]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[50.26 --> 50.82]  We love Linode.
[50.90 --> 52.32]  They keep it fast and simple.
[52.44 --> 54.80]  Check them out at linode.com slash changelog.
[54.80 --> 57.10]  Our bandwidth is provided by Fastly.
[57.36 --> 61.02]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[61.26 --> 63.00]  Get a demo at LaunchDarkly.com.
[70.28 --> 76.04]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[76.44 --> 77.38]  and accessible to everyone.
[77.68 --> 81.76]  This is where conversations around AI, machine learning, and data science happen.
[81.76 --> 86.50]  Join the community and Slack with us around various topics of the show at changelog.com slash
[86.50 --> 88.14]  community and follow us on Twitter.
[88.28 --> 89.84]  We're at Practical AI FM.
[95.90 --> 98.92]  Well, welcome to another episode of Practical AI.
[99.26 --> 100.84]  This is Daniel Whitenack.
[100.98 --> 106.98]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[106.98 --> 109.80]  Benson, who is a tech strategist at Lockheed Martin.
[109.80 --> 110.70]  How are you doing, Chris?
[110.82 --> 111.98]  Doing very well, Daniel.
[112.16 --> 113.52]  Excited about today's show.
[113.74 --> 116.16]  I think we have some pretty good stuff coming up here.
[116.28 --> 117.70]  I'm just kind of rearing to go.
[117.84 --> 125.56]  We've talked about a lot of computers on this show and accelerators and cards and GPUs and
[125.56 --> 128.56]  VPUs and all sorts of use.
[129.04 --> 133.40]  But we have yet to talk about photonic computers.
[133.40 --> 137.58]  And that's going to be the topic of today's conversation.
[138.14 --> 142.38]  Today, we've got with us Nick Harris, who is CEO of Light Matter.
[142.92 --> 147.06]  And we're going to hear a lot more about that and photonic computers today.
[147.26 --> 148.04]  So welcome, Nick.
[148.08 --> 148.94]  It's great to have you here.
[149.28 --> 150.62]  Thanks for having me, Daniel and Chris.
[151.04 --> 151.72]  And nice to meet you.
[152.00 --> 156.06]  So a lot of people might have not heard of photonic computers or even know where they
[156.06 --> 162.22]  sit in this sort of landscape or ecosystem of accelerators and types of processors and
[162.22 --> 162.90]  all of this stuff.
[163.02 --> 169.24]  So maybe just give a little bit of a background on how you came to encounter this topic.
[169.48 --> 176.02]  And then also, like, maybe some of the motivations behind this whole topic of photonic computing.
[176.02 --> 176.58]  Yeah.
[176.76 --> 181.62]  So I'll start out with just talking about the AI field as it's growing.
[181.62 --> 185.30]  So in around 2012, we had AlexNet come out.
[185.82 --> 190.10]  AlexNet was a neural net that was able to do image recognition tasks that were really incredible.
[190.10 --> 193.40]  And there was no other technique that could really keep up with it.
[193.62 --> 199.38]  And it made a great business case for companies like Microsoft, Google, Facebook, Amazon, and
[199.38 --> 204.82]  so on, to start building neural networks to do special kinds of problems, things that were
[204.82 --> 208.36]  very hard to write code for, but that neural networks could solve.
[208.36 --> 215.18]  And over the past 10 years now, we've had a really fast rate of progress in the amount
[215.18 --> 218.08]  of compute that's going into these state-of-the-art neural networks.
[218.34 --> 223.78]  It's motivated a lot of companies to start building accelerator chips to try to speed up
[223.78 --> 227.44]  these computations and make it so that we can make bigger and bigger neural nets.
[228.12 --> 232.68]  And some people's objective on this bigger and bigger scale is really to try to build something
[232.68 --> 234.24]  that's on the scale of a human brain.
[235.00 --> 237.58]  So that's kind of the trajectory where things are going.
[237.58 --> 243.90]  There's huge capital expenditures that go into building these kinds of AI supercomputers that
[243.90 --> 245.64]  can do incredible tasks.
[246.26 --> 250.88]  And what we're doing at Light Matter is we're trying to take a crack at that market with
[250.88 --> 251.78]  a unique twist.
[252.04 --> 254.50]  We're using photonics to do computation.
[255.06 --> 257.32]  I can tell you how I got to that place.
[257.58 --> 257.96]  Please do.
[258.28 --> 258.52]  Yeah.
[258.64 --> 262.80]  I was an engineer at Micron working on transistor device physics.
[262.80 --> 269.34]  So basically, I was getting a lot of exposure to the fab processes and some of the challenges
[269.34 --> 274.34]  that companies, not just Micron, are having and shrinking transistors and getting more
[274.34 --> 276.56]  performance out of them year over year.
[276.78 --> 282.50]  So I decided to go to graduate school, ended up at MIT and studying quantum computing.
[283.02 --> 284.00]  That's a bit of a leap.
[284.36 --> 286.64]  What Light Matter is doing isn't quantum computing.
[286.64 --> 290.92]  But I did spend those years building photonic quantum computers.
[291.52 --> 296.50]  And that happened right at the advent of that AlexNet neural network kind of coming out.
[297.02 --> 303.22]  And what we realized in Dirk England's group at MIT was that you could actually use the same
[303.22 --> 309.52]  kind of processor we were doing for quantum computing to do computing on traditional neural
[309.52 --> 311.68]  networks using just lasers.
[312.14 --> 314.72]  And the benefits would be pretty massive.
[314.72 --> 316.70]  Could you tell us like what that implies?
[316.84 --> 317.62]  What does that mean?
[318.00 --> 319.60]  How to use lasers for computing?
[319.98 --> 322.28]  Can you kind of bridge that gap between those two?
[322.52 --> 322.68]  Yeah.
[323.04 --> 324.68]  There's a little bit of history on this.
[324.80 --> 327.88]  So we're not the first people who have looked at photonic computing.
[328.18 --> 333.12]  People have realized first, I think in the 80s, that you might be able to do neural network
[333.12 --> 335.38]  evaluation with photonics.
[335.76 --> 338.26]  And that field kind of like petered out for a while.
[338.54 --> 340.66]  But we came at it from a totally different approach.
[340.72 --> 344.42]  So we were looking at quantum computers and we had a different motivation and a different set
[344.42 --> 347.22]  of like funding pitches for getting money to build these machines.
[347.54 --> 350.02]  We really took integrated photonics.
[350.20 --> 354.96]  That's a field that largely the way that you experience integrated photonics is through
[354.96 --> 356.96]  silicon photonics transceivers.
[357.16 --> 362.68]  So these are devices in data centers that send your communications, your data between different
[362.68 --> 363.40]  server racks.
[363.58 --> 365.66]  Maybe they're hosting a game you're playing.
[365.80 --> 369.34]  Maybe they're mediating your iMessages, something like that.
[369.34 --> 373.48]  But we use that core technology to start doing computing.
[373.80 --> 375.12]  Now, how do you do it with lasers?
[375.50 --> 377.96]  In the quantum computing case, we weren't using lasers.
[378.16 --> 379.50]  We were using single photons.
[379.64 --> 381.16]  But that's a story for another day.
[381.80 --> 384.12]  Lasers are devices that generate light.
[384.36 --> 388.52]  You give them an electrical signal and they're able to start generating light.
[388.64 --> 391.76]  And they're used in all sorts of traditional communications.
[392.26 --> 395.42]  The internet that we're talking over right now is over fiber optics.
[395.42 --> 398.84]  And the communication is sent using lasers to do that.
[399.28 --> 405.84]  So we're able to leverage that same infrastructure, lasers and silicon photonics, to actually do
[405.84 --> 408.62]  the core computations that happen in deep learning.
[409.18 --> 413.92]  And these computations are, I think, tractable really for anybody to understand.
[414.48 --> 420.68]  Deep learning as a field is really just relying on multiplication and addition to do evaluations.
[420.68 --> 424.90]  So the mathematics behind deep learning are relatively straightforward.
[425.10 --> 428.26]  Understanding how to come up with these things isn't straightforward.
[428.72 --> 432.82]  But when you actually run these programs, it's a lot of multiplication and addition.
[433.08 --> 439.28]  And indeed, you can use lasers and silicon photonics to do multiplies and addition.
[439.92 --> 443.08]  And I'm happy to go into how that works a bit later on.
[443.08 --> 444.10]  Yeah, I'm curious.
[444.44 --> 451.68]  Probably the main thing people think about maybe is like GPUs with computation on deep learning.
[451.90 --> 453.06]  And you're exactly right.
[453.12 --> 458.46]  I was just pulling up while you were talking the recent work from Microsoft and NVIDIA,
[458.62 --> 460.70]  I think, on the Megatron model.
[461.24 --> 465.12]  So they just have a figure where it's like, I think most people maybe in our audience have
[465.12 --> 471.64]  heard of BERT, you know, heard that in the context of AI, which had 340 million parameters
[471.64 --> 472.68]  in the model.
[473.38 --> 477.56]  GPT-3, which I think, Chris, you just had a conversation with someone about on the show.
[477.56 --> 477.86]  Last week, yeah.
[478.06 --> 481.72]  Yeah, 175 billion parameters.
[482.08 --> 487.76]  And then this Megatron, which is the new natural language generation model, which is talked about
[487.76 --> 491.60]  just recently, 530 billion parameters.
[492.40 --> 497.84]  So just commenting and following up on your conversation about these large models is pretty
[497.84 --> 498.62]  insane.
[498.62 --> 504.94]  I don't know, like, I think generally people have in their mind racks and racks of GPUs
[504.94 --> 506.06]  when they're thinking of this.
[506.22 --> 512.78]  So like with a photonic computer, and this is maybe just like a very simple question,
[512.78 --> 518.16]  but to have something in people's mind where like, so I've been near some like quantum computing
[518.16 --> 523.04]  labs where like they've got dilution fridges and it looks like this like whole like vacuum
[523.04 --> 524.06]  system and all that.
[524.06 --> 529.82]  And then I think about like laser labs with all these like, you know, lasers and you've
[529.82 --> 531.02]  got these lenses and stuff.
[531.12 --> 536.08]  And then that seems very different to me than like, oh, I'm going into the data center.
[536.20 --> 537.66]  I see these racks of computers.
[537.90 --> 543.96]  Just as a very simple question, like if you were to go to like look at a set of, you know,
[544.06 --> 550.50]  photonic computers, what does that look like form factor wise and like connection wise maybe
[550.50 --> 552.56]  as comparison to some of these other things?
[552.56 --> 557.56]  Well, I would say the biggest deployments of AI are in hyperscaler environments and in
[557.56 --> 558.52]  cloud environments.
[559.10 --> 563.26]  And to play in those spaces, you need to avoid doing anything weird.
[563.46 --> 567.06]  So a big dilution refrigerator or a vacuum, that's going to be a problem.
[567.44 --> 571.70]  And so if you look at photonic computers, like the things that we're developing, they just
[571.70 --> 573.20]  look like a normal silicon chip.
[573.48 --> 575.62]  They do have optical fibers that come out.
[575.90 --> 579.28]  You do need to get light into the processor so that it can do the calculations.
[579.28 --> 582.60]  But, you know, it's really just a standard computer chip.
[582.74 --> 584.80]  It looks like a card sitting in a server.
[585.34 --> 588.26]  But there's a little addition of having a laser in there.
[588.60 --> 592.70]  You know, just maybe on the larger picture here, there are so many different ways that
[592.70 --> 597.56]  people are looking at powering AI computation because the market opportunity is so big.
[597.66 --> 601.44]  And we're all trying to power these 500 billion weight neural networks.
[601.44 --> 604.00]  And it's going to take a lot of computing power.
[604.50 --> 606.86]  And that power is the principal problem.
[607.06 --> 609.44]  Like computer chips are getting way too hot.
[609.96 --> 614.14]  That's really one of the fundamental things that we're interested in trying to help with.
[614.52 --> 618.84]  When you said it was kind of one of the principal things, is that kind of the primary value
[618.84 --> 623.28]  proposition when you're saying, you know, go with photonics, you know, laser driven,
[623.46 --> 627.98]  it doesn't heat up, you don't have the massive problem that you have to deal with in a data
[627.98 --> 629.06]  center where you have a bunch of that?
[629.06 --> 630.26]  Is that the primary thing?
[630.34 --> 634.82]  Are there other performance characteristics or non-performance characteristics that play
[634.82 --> 639.12]  into the field in general in terms of the field itself having value proposition?
[639.52 --> 639.68]  Yeah.
[639.80 --> 642.54]  So I can say some really general things about computers.
[642.54 --> 648.32]  If you have one processor and you run a program on that processor, you will get one processor
[648.32 --> 649.54]  worth of performance.
[649.94 --> 654.72]  If you take two processors and try to scale it up, it'll be just less than two processors
[654.72 --> 655.58]  worth of performance.
[655.58 --> 660.74]  When you get to a thousand nodes, you're going to be looking at something that is kind of doing
[660.74 --> 663.54]  the amount of computation that half the number of units will be doing.
[663.78 --> 663.86]  Yeah.
[663.98 --> 668.94]  So what I'm getting at with that is, as you try to power bigger and bigger neural networks,
[669.52 --> 670.58]  you need to scale up.
[670.78 --> 675.22]  And the reason that you need to scale up is that the individual computer chips that we
[675.22 --> 681.74]  build today, Intel's chips, AMD's chips, NVIDIA's chips, they all consume a lot of power.
[681.74 --> 685.62]  And you kind of have to spread them out and they're getting to be really big.
[685.84 --> 690.88]  And so this heat problem, in addition to what's known as Omdahl's law, scaling, where every
[690.88 --> 694.46]  time you add a unit of compute, you do not get a unit of performance out.
[694.80 --> 696.20]  Those two things kind of work together.
[696.34 --> 700.18]  So really power efficiency is tied to compute scaling.
[700.42 --> 702.20]  It's tied to compute per chip.
[702.52 --> 705.72]  There's really a maximum amount of heat that you can pull out of a processor.
[705.72 --> 711.96]  So it's just this whole story that's built around, you can't be trying to dissipate kilowatts
[711.96 --> 713.66]  of power in a single chip.
[713.94 --> 715.16]  You're not going to be able to cool it.
[715.36 --> 718.90]  And you're certainly not going to be able to continue a roadmap where you're pumping
[718.90 --> 720.60]  more power through chips.
[721.12 --> 725.20]  So it's performance, energy efficiency, and all that stuff is fundamentally linked.
[725.32 --> 727.82]  And they sort of hamper your ability to scale out.
[728.32 --> 733.70]  And I know that we've talked on the show a couple of times about the environmental impacts
[733.70 --> 737.44]  of what we're doing with these sort of large models.
[737.84 --> 742.16]  And I think, you know, there was that one study, I forget how old it is now, it's actually
[742.16 --> 746.66]  probably a couple of years old now, where it was talking about like one of these large
[746.66 --> 752.02]  language models is like running five cars into the ground for like their whole life
[752.02 --> 753.60]  period to train like once.
[753.76 --> 755.44]  And, you know, we're training them multiple times.
[755.44 --> 760.12]  So as you're talking about power, a lot of what I'm thinking is related to that sort of
[760.68 --> 763.62]  sustainability side of things.
[763.70 --> 769.78]  So like in terms of that power requirement side of things, I mean, lasers still require
[769.78 --> 770.78]  power, I'm assuming.
[771.04 --> 776.40]  So I don't really have a sense of like, what sort of scales are we looking at on like a
[776.40 --> 780.58]  sort of GPU accelerated AI versus like photonic based?
[781.08 --> 785.74]  Yeah, maybe we can start with like a bit of the bigger picture around the energy scaling
[785.74 --> 786.10]  problem.
[786.36 --> 790.76]  So when you double the number of transistors on a computer chip, that's Moore's law.
[790.92 --> 792.40]  It should happen every 18 months.
[792.40 --> 794.54]  Maybe we're a little bit behind schedule on that.
[794.74 --> 796.52]  But Moore's law is mostly OK.
[796.90 --> 800.48]  Every time you double the number of transistors on the chip, they're going to need to use
[800.48 --> 803.54]  less energy in order for that chip to not get really hot.
[804.04 --> 809.90]  And since around 2005, when we've shrunk the transistor, the amount of energy that they
[809.90 --> 811.82]  use isn't shrinking commensurately.
[811.82 --> 814.66]  And so the chips are getting hotter and hotter and hotter.
[815.04 --> 819.58]  It sort of pushed us to a spot where you've heard a lot about system on chip and Apple's
[819.58 --> 822.24]  recent announcement of the M1 chips.
[822.78 --> 823.46]  You can see it.
[823.84 --> 825.42]  These are system on chip platforms.
[825.64 --> 827.28]  They have lots of different functionality.
[827.78 --> 831.94]  But it turns out that if they turned all of those functionalities on at the same time,
[831.98 --> 835.02]  you would really hit the thermal limits for the system.
[835.02 --> 840.72]  So this is a result of the fact that the energy scaling in transistors hasn't continued with
[840.72 --> 841.26]  their shrinking.
[841.86 --> 843.16]  That's called Denard scaling.
[843.56 --> 845.84]  So that's kind of what's toast right now.
[846.30 --> 851.40]  So when you look at solutions from NVIDIA, for example, they're really pushing the limits
[851.40 --> 852.84]  of what's possible to cool.
[853.20 --> 855.32]  I can tell you we have a packaging team at Light Matter.
[855.82 --> 859.22]  Their job is to make sure that you can pull the heat out of your computer chips.
[859.22 --> 863.90]  And we're all very impressed with how much heat they're able to get out of the A100 processor.
[864.42 --> 866.42]  It's something like 450 watts.
[867.06 --> 872.42]  There's a new chip from Intel, Ponte Vecchio, and that chip is 600 watts.
[872.60 --> 873.84]  Really cool technology.
[874.00 --> 874.52]  It's awesome.
[874.68 --> 876.92]  But this power thing, it's a real challenge.
[877.30 --> 882.22]  It turns out that once you get to those kind of numbers, Ponte Vecchio is water-cooled.
[882.28 --> 885.66]  So you really have to go from a heat sink and a fan, which is what you'll find in your
[885.66 --> 888.96]  computer at home unless you're an enthusiast and you love water-cooling.
[888.96 --> 890.66]  You have to move towards water-cooling.
[890.76 --> 895.42]  And after that, you're seeing advertisements from Azure, Microsoft Azure, where they're
[895.42 --> 896.36]  doing immersion cooling.
[896.94 --> 900.94]  So they take computer chips and put them underneath apparently edible oil.
[901.18 --> 902.48]  Don't ask me how I know it's edible.
[902.88 --> 903.94]  From the diner?
[904.92 --> 908.24]  Yeah, I don't know if it's fry grease, but it's apparently edible.
[908.50 --> 910.08]  I don't know why you would ever eat it.
[910.60 --> 913.80]  Maybe it's like a reusable type material.
[914.08 --> 915.86]  I don't know why they would advertise it as edible.
[916.10 --> 917.84]  It's an odd characteristic to note.
[917.84 --> 919.54]  It shows safety, I guess.
[919.64 --> 922.98]  If you're like, if you can eat it, it's probably pretty safe.
[923.48 --> 925.80]  It sounds like a long chemical word.
[926.00 --> 928.60]  So edibility is probably a good sign.
[929.16 --> 933.98]  So the basic point here is that if you look at technologies for powering AI right now,
[934.10 --> 935.56]  they're all based on transistors.
[935.76 --> 938.24]  There's never been a computer that's not based on transistors.
[938.52 --> 940.74]  This is the way that the world does computation.
[940.74 --> 945.68]  But we've run into this kind of fundamental challenge around shrinking how much energy
[945.68 --> 946.94]  the chips are using.
[947.48 --> 949.70]  And you can't really do that going forward.
[950.06 --> 955.06]  So if you look at the Department of Energy's estimate for energy consumption, 2030, so in
[955.06 --> 961.20]  about eight years, 10% of the entire planet's energy consumption will be on compute and interconnect.
[961.20 --> 967.70]  So if you know about compound annual growth rates, if we look at 2040, you're talking about most,
[967.90 --> 970.36]  like the overwhelming majority of the power being used on this.
[970.64 --> 976.00]  You always have to think in business about the use case that could motivate using that much of the planet's power,
[976.12 --> 977.52]  because that would cost a lot of money.
[977.52 --> 985.34]  And I think what happens is that you will start to see that progress in AI will slow because of the heat problem,
[985.44 --> 990.16]  because it puts a lot of financial pressure on data centers and the people who scale these things.
[990.38 --> 995.74]  To be clear, those neural networks that Daniel was talking about, those are trained by the biggest companies in the world.
[996.06 --> 998.50]  And there are hundreds of millions of dollars for the supercomputer.
[998.84 --> 1001.12]  And running those models costs like $10 million.
[1001.68 --> 1003.24]  These are massive scale problems.
[1003.24 --> 1011.58]  And I would go out on a limb and say it's already probably an uncomfortable amount of money for those companies that they're spending on these things.
[1011.90 --> 1013.14]  So that's the state of things today.
[1013.24 --> 1014.50]  Everything's based on transistors.
[1014.86 --> 1020.68]  And you've really got Denard scaling, which, by the way, it's underpinned by quantum mechanics.
[1021.00 --> 1022.44]  It's not something that we can fix.
[1022.76 --> 1028.28]  TSMC doesn't have a solution for how they're going to get rid of this little pesky energy scaling problem.
[1028.64 --> 1029.60]  I wish they did.
[1029.80 --> 1031.94]  But that's kind of where photonic computing comes in.
[1031.94 --> 1037.68]  And so we don't really have to worry about the quantum tunneling effects because we're not using transistors.
[1038.16 --> 1039.84]  It's a totally different type of device.
[1040.30 --> 1043.70]  And so that part of the scaling doesn't matter so much.
[1044.04 --> 1050.54]  So hopefully that starts to give you a picture of like, we just sort of said transistors, that's how people do computation.
[1050.98 --> 1053.06]  For deep learning, we think we can do it with optics.
[1053.28 --> 1057.56]  We think we'll use a lot less energy and we'll get rid of that whole energy scaling problem.
[1057.72 --> 1059.86]  Just walk around it because we're using different physics.
[1061.94 --> 1076.14]  Changelog++ is the best way for you to directly support practical AI.
[1076.66 --> 1080.90]  Join today and unlock access to a private feed that makes the ads disappear,
[1081.34 --> 1087.04]  gets you closer to the metal, and help sustain our production of practical AI into the future.
[1087.04 --> 1096.12]  Simply follow the Changelog++ link in your show notes or point your favorite web browser to changelog.com slash plus plus.
[1096.42 --> 1100.32]  Once again, that's changelog.com slash plus plus.
[1101.76 --> 1102.76]  Changelog++.
[1103.30 --> 1104.06]  It's better.
[1104.06 --> 1122.66]  So Nick, you just started getting to where I really was interested in discussing next,
[1122.66 --> 1130.96]  which is around like, okay, we think we can do sort of these computations related to deep learning and AI with photonics.
[1130.96 --> 1136.82]  I'm curious, like, I guess the first question is where we add in that process.
[1136.94 --> 1140.48]  Is it like this is being done and has been being done?
[1140.60 --> 1144.42]  And, you know, I suspect you've done certain things.
[1144.56 --> 1154.02]  Like, how far are we to like doing training and our inference in a like reasonable way with photonics?
[1154.02 --> 1156.28]  All right. So there's been a history here.
[1156.42 --> 1162.84]  I've been building these systems as part of my graduate work and now the company at Light Matter for about a decade.
[1163.40 --> 1169.98]  And over that time, we've demonstrated a number of applications running language processing on these chips.
[1169.98 --> 1175.88]  That was done at MIT, along with a bunch of other cool applications of the processor technology.
[1175.88 --> 1180.98]  At Light Matter, we announced the Mars chip, and that was at Hot Chips 2020.
[1181.24 --> 1187.16]  Hot Chips is a conference on computer architecture, and that chip is capable of running state-of-the-art neural networks.
[1187.76 --> 1195.46]  And what we're up to right now at Light Matter is we are gearing up to start delivering our processors to customers.
[1195.92 --> 1202.10]  Very big companies that are interested in energy-intensive AI and trying to power their roadmap.
[1202.10 --> 1207.10]  They really care a lot about how do you get to the trillion parameter neural network and beyond.
[1207.62 --> 1212.62]  So we're very far along in this journey, like quite confident that you're going to get to see it.
[1212.98 --> 1217.74]  And, you know, we've built lots of prototypes along the way, peer-reviewed stuff in academia.
[1217.94 --> 1222.74]  It's been published in Nature, Nature Photonics, Nature Physics, all the natures.
[1224.06 --> 1227.52]  And so it's real stuff, and we're going to be selling it.
[1227.52 --> 1238.12]  Yeah, and before we go into like the actual like what you'll be selling and some of like how it's related to AI and such, I'm curious, like that's been a long road.
[1238.38 --> 1241.48]  I'm sure like it hasn't been all smooth sailing.
[1241.86 --> 1246.82]  Have there been points along that path where you're like, oh, this is like, I don't think we're going to make it.
[1246.96 --> 1253.60]  Or like, you know, what have been major like bumps in the road or like major achievements along the way that have happened?
[1254.36 --> 1255.88]  Entrepreneurial war stories here.
[1255.88 --> 1258.56]  Yeah, building companies is a lot of work.
[1258.80 --> 1262.20]  Hiring people, hiring really good people, it takes a lot of time.
[1262.52 --> 1265.14]  I have a lot of entrepreneurial war stories.
[1265.54 --> 1276.52]  In terms of challenges along the way, I'd say that the first couple years of the company, we were spending a lot of time trying to figure out exactly what the photonic compute architecture would look like.
[1276.88 --> 1278.46]  We knew it was silicon photonics.
[1278.90 --> 1285.08]  We had Global Foundries as our partner, Fab, but we had to figure out exactly what we were going to build.
[1285.08 --> 1287.82]  And there are a lot of ways to build these processors.
[1288.14 --> 1292.08]  Like, make no mistake, we've patented about 70 ways to do that.
[1292.20 --> 1295.36]  But there's only one that really works well from what we've seen.
[1295.66 --> 1297.76]  So narrowing that down was a lot of work.
[1298.06 --> 1299.54]  Building teams is super hard.
[1299.54 --> 1303.82]  And especially building teams where you've invented a new field.
[1304.32 --> 1308.18]  Silicon photonics is a technology that's been deployed for about 10 years now.
[1308.32 --> 1310.96]  So data centers have been using it long-haul communications.
[1311.34 --> 1315.32]  Like, across the country type communications have been using silicon photonics.
[1315.54 --> 1321.22]  But people were not trained in using silicon photonics for building computers because it didn't really exist.
[1321.74 --> 1323.44]  So that's some of the big stuff.
[1323.44 --> 1326.96]  The other pieces are, you know, you have to build a supply chain for these things.
[1327.52 --> 1329.02]  And it's, you know, it's not straightforward.
[1329.24 --> 1333.20]  There are a lot of people who touch the hardware from start to finish.
[1333.50 --> 1336.88]  And some of the steps are with companies that are, you know, smaller.
[1337.06 --> 1342.16]  And you have to kind of work with them to try to get things productized and stable and all that sort of thing.
[1342.24 --> 1343.84]  You can think about lasers, for example.
[1343.84 --> 1352.10]  So can you describe a little bit, for those of us who are trying to kind of wrap our minds around what this kind of chip is like?
[1352.38 --> 1356.22]  Obviously, you can't describe in detail the internals, nor would you want to.
[1356.30 --> 1360.64]  But kind of give me a sense of what a photonic chip is like.
[1360.74 --> 1362.92]  What are some of the considerations that go into it?
[1363.04 --> 1366.32]  For those of us who are brand new to this field and just trying to...
[1366.32 --> 1370.90]  I know at the end of the day, you're producing a board that's going to go into my computer.
[1370.90 --> 1375.72]  But what's this little photonic magical thing that's inside that?
[1375.88 --> 1376.80]  You know, how does that work?
[1376.90 --> 1382.28]  What's different about it from the way I might already be thinking about these other architecture chips that we've talked about?
[1382.58 --> 1387.12]  So I can say something sort of boring, which is, have you heard of the Google TPU?
[1387.72 --> 1391.04]  So GV, formerly Google Ventures, is an investor.
[1391.44 --> 1394.68]  And our technology looks a lot like a TPU.
[1394.96 --> 1395.26]  Okay.
[1395.50 --> 1395.78]  Yeah.
[1395.78 --> 1401.84]  So it is a matrix processor with a lot of other things wrapped around it.
[1402.04 --> 1404.10]  It's not just doing matrix processing.
[1404.28 --> 1406.06]  There's a lot of things wrapped around it.
[1406.22 --> 1407.30]  Emphasize on that.
[1407.58 --> 1409.48]  But it's basically doing linear algebra.
[1409.70 --> 1412.60]  So we have multiple processor cores.
[1412.80 --> 1417.90]  Our product's actually a quad core computer, just like an Intel, like quad core chip.
[1418.02 --> 1420.24]  And each one of those cores is doing linear algebra.
[1420.24 --> 1427.04]  If you were to look at the chip and just follow the light, what you would see is values from an image.
[1427.22 --> 1428.36]  Like, let's say we have a pixel.
[1428.54 --> 1429.56]  It's red, green, or blue.
[1429.98 --> 1433.06]  And there's an intensity for each pixel from zero to one.
[1433.42 --> 1438.62]  What you'd see is a brightness of light corresponding to that intensity number, if we're doing image processing.
[1438.62 --> 1441.48]  Kind of like being distributed around the chip.
[1441.74 --> 1449.60]  And then you'd see these photonic units in a two-dimensional array receiving the signals and then doing multiplication and addition.
[1449.90 --> 1450.98]  That's basically it.
[1451.06 --> 1458.06]  So it would look to you a lot like a TPU, this like box, like a 2D array of multiply accumulate units.
[1458.32 --> 1463.04]  Except you would see light being distributed to all of the individual components.
[1463.74 --> 1468.02]  You talked a lot about heat and its sort of motivation in this.
[1468.02 --> 1479.32]  I imagine that there's a number of, you're thinking about the heat problem, but also with this sort of chip, I imagine there's like a lot of sort of like interference type things.
[1479.36 --> 1480.40]  And we're thinking about light.
[1480.40 --> 1481.88]  Is there different considerations?
[1481.88 --> 1502.32]  Like maybe you have some benefits in the heat side of things, but are there other sort of like shielding or interference or other sort of challenges related to that in terms of building the physical unit that you have to take into consideration that you wouldn't have to take into consideration with another type of computer?
[1502.32 --> 1504.38]  So yes and no.
[1504.68 --> 1505.54]  We're using light.
[1505.80 --> 1508.90]  And so light signals can't interfere with each other.
[1509.44 --> 1511.60]  So that's kind of an interesting property.
[1511.80 --> 1516.30]  However, whenever you build a metal wire, it ends up being kind of an antenna.
[1516.70 --> 1523.22]  And so in chip design, there are these things called antenna rules and digital chips have to worry about these two.
[1523.22 --> 1534.38]  And so, you know, we have to observe these things so that we don't get unwanted signals from radio hosts or something getting into the chip and messing up the optical computation through the wires.
[1534.56 --> 1540.10]  But otherwise, I think that it really just looks like a mixed signal chip.
[1540.26 --> 1549.20]  So there's analog circuits, there's digital circuits, and then the photonic circuits, which for all practical purposes are just analog type circuits.
[1549.20 --> 1555.66]  So you have to be careful about coupling unwanted signals through antennas that you didn't intend to be there.
[1556.14 --> 1558.32]  But otherwise, no, not really.
[1558.60 --> 1565.66]  So I could still have all my RGB lighting in my computer case and like have flashing cool stuff.
[1566.12 --> 1567.84]  Yeah, if that's the question, absolutely.
[1568.12 --> 1569.88]  It turns out that it's very hard.
[1570.20 --> 1572.36]  We have these things, and I should have mentioned this.
[1572.44 --> 1573.94]  We have these things called waveguides.
[1574.20 --> 1578.52]  They're about 300 nanometers wide and about 200 nanometers tall.
[1578.52 --> 1581.10]  And there are optical wires that are on our chip.
[1581.18 --> 1582.28]  So they're really tiny.
[1582.56 --> 1584.86]  And we have hundreds of thousands of them on the chip.
[1585.06 --> 1587.12]  It's very hard to get light into those.
[1587.26 --> 1592.58]  And so if you shine the flashlight on our waveguides, you get like nothing into the waveguide.
[1592.92 --> 1597.88]  You have to really want to get the light in there for that to work out, which is fortunate and unfortunate.
[1597.88 --> 1599.42]  I'm kind of curious.
[1599.42 --> 1611.94]  Is there, if you're looking at the wire, you know, world that we've been in for so long and the physics, you know, as it gets smaller and smaller and they're running into all sorts of challenges, heat and otherwise, how does that translate?
[1612.08 --> 1620.16]  Do you, you know, you just talked about how small that optical wire is, if you will, and the fact that because of that, you don't get the light into it.
[1620.16 --> 1629.58]  So what are some of the kind of in the science of this, what are some of the limitations as you are constantly trying to get to smaller and smaller architectures to scale out?
[1629.90 --> 1631.30]  What are the things you have to think about?
[1631.64 --> 1633.18]  Yeah, it's an interesting question.
[1633.52 --> 1637.20]  So at first glance, you would be like, all right, you've got a new kind of computer.
[1637.46 --> 1643.12]  We're going to want to shrink it every 18 months and have a photonic Moore's law or something, some kind of scaling law.
[1643.12 --> 1644.74]  You could go down that path.
[1644.88 --> 1649.34]  And the way you would do it is you'd start out, we work at 1550 nanometers wavelength.
[1649.76 --> 1654.40]  You could go down to 1310 nanometers and then you could go down to 900 nanometers.
[1654.58 --> 1659.18]  By the way, your eye will just start to pick this up and it will look like red and so on down.
[1659.52 --> 1662.88]  And then maybe you get to ultraviolet, which is what gives you skin cancer.
[1663.14 --> 1664.80]  OK, and then we keep going.
[1664.88 --> 1665.76]  We get to x-rays.
[1665.96 --> 1668.58]  And the whole time these optical components are shrinking.
[1668.58 --> 1676.24]  They're going from 300 by 200 nanometers, eventually at the x-ray kind of scale to, you know, a few nanometers kind of dimensions.
[1676.58 --> 1677.38]  You could do that.
[1677.52 --> 1678.24]  It's possible.
[1678.48 --> 1683.42]  But it turns out that the light sources that you need to follow that path would be pretty tricky.
[1683.78 --> 1689.48]  And when you build optical wires, they care a lot about the quality that you build those wires with.
[1689.66 --> 1692.22]  The light wants those wires to be very smooth.
[1692.52 --> 1698.46]  So if you're not, you know, really, really careful about the quality of those wires as you shrink it, you're going to have a hard time.
[1698.92 --> 1701.76]  And luckily, it turns out we don't need to shrink them at all.
[1702.34 --> 1704.78]  Well, you just took the next question right out of my mouth on that one.
[1704.88 --> 1706.40]  So keep going, please.
[1706.40 --> 1706.76]  Yeah.
[1706.96 --> 1715.02]  So it turns out that in a traditional computer, if I said that your CPU is clocked at 3 gigahertz, you'd be like, yeah, that totally makes sense.
[1715.14 --> 1719.30]  If I say 20 gigahertz, you're like, I've never heard of that.
[1719.30 --> 1727.88]  And it probably will never be a thing because I remember, like when I was in undergrad in like 2005, I had a 3 gigahertz processor then, if I recall correctly.
[1728.38 --> 1730.36]  So like that frequency hasn't been scaling.
[1730.72 --> 1734.40]  With optics, the frequency you can operate at is very high.
[1734.40 --> 1737.24]  So we work at about 1550 nanometers.
[1737.58 --> 1740.96]  That corresponds to a frequency of 193 terahertz.
[1741.44 --> 1742.60]  That's a lot of bandwidth.
[1743.02 --> 1743.12]  Yeah.
[1743.40 --> 1749.38]  Turns out that you will never practically get anywhere near that kind of bandwidth because you have to talk to the thing.
[1749.74 --> 1755.22]  You know, like ultimately, these things have to talk to electronic computers because that's sort of how the world works.
[1755.22 --> 1756.62]  And so you get limited.
[1756.88 --> 1760.72]  Maybe you can do 20 gigahertz, 50 gigahertz, something like this.
[1761.02 --> 1770.54]  But the point is that we're able to turn up the clock frequency to obviate the need for shrinking these things because we're going to give you more performance per unit area through the clock frequency.
[1771.00 --> 1772.06]  And there's one other thing.
[1772.38 --> 1774.14]  So, yeah, we can go fast and clock.
[1774.40 --> 1779.40]  We can do something else special, which is we can use multiple colors at exactly the same time.
[1779.56 --> 1784.84]  So if you remember, we have this 2D array that's doing matrix computation.
[1785.22 --> 1790.58]  Each one of the elements in the array can process different colors of light at the same time.
[1790.96 --> 1796.64]  So each element could do three colors at the same time, 16 colors at the same time, something like this.
[1797.14 --> 1807.64]  And what that means is that in the same area, that same array size, two colors of light, you've just doubled the compute in the unit area, three colors of light, three times the compute per unit area.
[1807.64 --> 1814.50]  And you see, like, there's really no need in principle for this sort of shrinkage of the photonic devices.
[1814.50 --> 1821.46]  Well, as Chris knows, I'm always interested in the very practicalities of things.
[1821.82 --> 1828.48]  And I'm imagining, OK, we have this processor and it works and can do some computations.
[1828.70 --> 1831.36]  You have it integrated into some system.
[1831.36 --> 1849.72]  But ultimately, like, I have TensorFlow and I know how to run TensorFlow on a regular computer or on a GPU because there's underlying libraries, which eventually get mapped into some type of machine code that, you know, is mapped onto like this processor.
[1849.72 --> 1854.38]  So maybe just describe like, OK, you have this photonic computer.
[1854.64 --> 1867.26]  How do you even start to think about that process of integrating software into the system and like making sure you support like tooling that people want to use and that sort of thing?
[1867.78 --> 1869.34]  Yeah, that's a huge amount of work.
[1869.34 --> 1873.28]  So building the photonic computer is really hard in terms of the physics and engineering.
[1873.84 --> 1879.88]  But building a software stack that integrates with PyTorch and TensorFlow is a ton of work.
[1879.98 --> 1882.86]  But it's something that we've bid off and we call it Idiom.
[1883.18 --> 1885.72]  So Idiom is Light Matters software development kit.
[1886.10 --> 1892.46]  What we allow you to do is take neural networks that you've built in PyTorch or TensorFlow, import our libraries.
[1892.46 --> 1899.82]  And we have a compiler that can take the emissions from PyTorch and TensorFlow and build machine code that runs on Envise.
[1900.20 --> 1901.70]  Envise is our photonic computer.
[1902.16 --> 1909.54]  So we have our own instruction set architecture and our compiler emits that ISA is what people call it, instruction set architecture.
[1909.86 --> 1910.70]  It's a ton of work.
[1910.78 --> 1912.28]  We have a pretty big software team here.
[1912.52 --> 1920.30]  I expect by the end of next year that we'll have significantly more software engineers than hardware engineers, even though we're building these crazy chips.
[1920.30 --> 1930.40]  And generally, that's the trend, certainly in the machine learning space, but in computer chips in general, because people, they don't really care about computer hardware.
[1930.66 --> 1936.84]  They just care that it's fast and it keeps getting better and that it doesn't have errors and it's not annoying to use.
[1936.84 --> 1942.80]  So we're very focused on just delivering the same experience that you're used to with PyTorch and TensorFlow.
[1943.28 --> 1947.76]  And you can just use our alien technology and not worry about what's under the lid.
[1947.88 --> 1949.44]  But it's a very big effort.
[1949.44 --> 1949.48]  Right.
[1949.92 --> 1966.76]  So if you're thinking about that, just to clarify for a moment, if we're going to PyTorch or TensorFlow and we have your chip in the system and we have idiom there, it's basically taking that, converting it into something that works on your hardware in that context.
[1966.76 --> 1975.02]  But from our standpoint, as data scientists or software developers or deep learning engineers, our workflow is more or less the same, if I'm understanding you correctly.
[1975.16 --> 1976.04]  Is that accurate?
[1976.54 --> 1977.04]  That's right.
[1977.38 --> 1978.90]  So right now we're targeting inference.
[1978.90 --> 1985.12]  So the way you'd imagine this working is you've got a neural network that you've trained in PyTorch or TensorFlow.
[1985.52 --> 1992.00]  And then we have a bridge to Onyx and then Onyx to our compiler and you're good to go.
[1992.20 --> 1992.64]  That makes sense.
[1993.10 --> 1993.26]  Yeah.
[1993.40 --> 1996.88]  And so the chip can do training, but we're not focused on it right now.
[1996.94 --> 2002.04]  They're very, very different markets with very different things that you optimize for.
[2002.38 --> 2004.04]  Happy to talk about that.
[2004.04 --> 2007.62]  But inference and training are really drastically different beasts.
[2007.76 --> 2008.24]  Yeah.
[2008.32 --> 2019.72]  Maybe you could touch on that a little bit because I think maybe the, at least for people getting into deep learning, a lot of the tutorials and whatever they see is all about training.
[2019.86 --> 2019.98]  Right.
[2019.98 --> 2028.68]  So it becomes this perception that like training is the major problem to solve as a data scientist or an AI researcher at your day job.
[2028.68 --> 2045.94]  Could you maybe like on some of your work with Light Matter, but also just working with clients and understanding their needs, like maybe speak into that in terms of why inferencing is like such a big market, but also really important for, you know, practical use cases of AI.
[2045.94 --> 2053.22]  Yeah. So training is R&D mode. You're building a tool that takes inputs and then tells you something about those inputs.
[2053.46 --> 2064.30]  If that's all we ever did in machine learning, no companies would fund this stuff because the ultimate goal of building those models is that you want to use them for something.
[2065.00 --> 2075.40]  And if you're Google or Facebook, these neural networks get deployed at massive scale and their job is to take a user query, run a neural network on the query, give you results.
[2075.40 --> 2085.04]  And sometimes there are lots of neural networks in that chain. And that is where the overwhelming majority of the energy footprint of AI will be over time.
[2085.38 --> 2096.70]  Training is a really big deal. You gave the example, I think MIT Tech Review did that analysis that you were quoting where it was like five cars over their whole lifetime is how much energy that the training was using.
[2096.70 --> 2110.00]  And I think the equivalence was in like carbon emissions. So yeah, inference is deployment, which is where most of the scale is. And training is just doing the R&D that lets you do that thing that makes you money because the training stuff doesn't make you money.
[2110.00 --> 2115.18]  As you go, I actually want to go back for one second and touch on something to combine two things that you've said.
[2115.62 --> 2125.94]  So as we're doing this and we get to, you know, as practitioners keep the same workflow more or less that we're doing, and we are still able to use the tools that we're already using to be productive.
[2125.94 --> 2134.80]  We've now been kind of supercharged by having these photonic processors in there. I may not be using the right terminology on that.
[2134.94 --> 2141.38]  But, and we've talked about scaling without having that limitation from the thermal limitation that we've talked about.
[2141.38 --> 2163.62]  Does, to go back for just a second of a curiosity, is your limiting factor then the receptor of the light inside there being able to detect the number of different lightweight frequencies, the number of different colors that are available so that in theory, if it's along as, as you can build better and better receivers for different, for more and more colors in there, they can distinguish.
[2163.88 --> 2164.10]  Yes.
[2164.14 --> 2169.70]  Then you're essentially unbounded by that constraint until you hit whatever that practical limit may eventually be.
[2169.70 --> 2174.34]  Yeah, that's a great question. So what are the ultimate bounds on using color and frequency?
[2174.82 --> 2174.94]  Yeah.
[2175.10 --> 2190.84]  Detectors are pretty broadband, so they can detect a large number of different colors at the same time. No problem there. But there's a device called a multiplexer or a demultiplexer. If you can think of the Pink Floyd album cover, you have a prism.
[2191.04 --> 2191.18]  Yeah.
[2191.18 --> 2196.50]  And there's a white light that comes in and a rainbow that comes out the other side. That's identically what I'm talking about.
[2196.50 --> 2222.88]  So that specific kind of device that takes in a stream of multiple colors and spreads it out into the individual constituent colors. That device is what will limit you from getting to like 64 colors or 128 colors. Eventually, it gets really hard to accurately separate those colors. And then when you're at this point, scale out becomes really important. By the way, that's a long ways away.
[2222.88 --> 2223.20]  Okay.
[2223.20 --> 2241.90]  In terms of the roadmap for photonic computing. When we're at 64 colors, the amount of compute on the chip is something like hundreds of peta ops. It's crazy. So like decadal timescales. But then when you get there, what's really important is that you can efficiently take lots of cores, lots of processor cores, and connect them to each other.
[2241.90 --> 2268.84]  Earlier, I was talking about Omdel's law and the fact that you add another unit of compute. And unfortunately, because of communications, you don't get another unit of throughput. We've invented an interconnect technology that surprise, surprise, uses light. It's a wafer scale computer chip, eight inch by eight inch. So it's the size of your laptop screen practically. And it allows you to let your processors talk optically. And they can dynamically configure how they're connected.
[2268.84 --> 2294.24]  You remember those old switch rooms where people are making phone calls and they need to connect to some other. So imagine you have someone doing that, but at the microsecond timescale, they're able to unplug the optical waveguides built into this computer chip and plug them into different locations at crazy high speeds. And that allows you to scale it. So whenever you run out of colors, scale out is going to be really important. And we've invented a technology for that. And it's called Passage.
[2294.24 --> 2308.20]  That's really cool. I love that analogy. And I love the fact that you're also thinking about scale out, not in terms of always making things smaller and pushing those boundaries, but doing it in other creative ways as well.
[2308.20 --> 2323.40]  So if I'm understanding right, you kind of have the chip. So in terms of like what you're bringing to market and what you're doing, you have the sort of chip or processor, you have this Passage technology, and then the Idiom software integration.
[2323.40 --> 2342.12]  I'm wondering if you could just give a few or highlight a few sort of use cases or tests that you've done with these technologies in terms of maybe models that we might be aware of about like inference time or like what sort of differences are you seeing and how is that impacting actual inferencing?
[2342.12 --> 2372.10]  Yeah, so comparing our technology to competitors, right? So on the Idiom side, it's a software stack. And the goal is really just to make sure that it doesn't slow down the hardware compared to what it's theoretically capable of. So we'll leave that on the table. On the advise side, on our website, you can see a comparison between advise server and NVIDIA's DGX A100 server, we use a very small fraction of the power. So that chips quoted at about 80 watts, compared to NVIDIA's 400
[2372.12 --> 2401.50]  150 watts, and pretty significant boost on ResNet 50, BERT. And then I believe we also looked at DLRM. I don't have the numbers off the top of my head, but in many cases, it's multiple times faster. But what's extremely important from a scale-out perspective is if you look at the power. And just like if you think about it this way, we can up the performance, we're not anywhere near that power envelope. So we can keep going up there. There's a point though, and this is why we invented Passage, where
[2401.50 --> 2418.22]  making advise faster is great, but it's just sitting there waiting for work. It's sort of like this ultra capable person and you like hand them a paper once a day and they're just poured out of their mind. So we really had to invent Passage as a way to keep advise busy. So that should give you an idea.
[2418.78 --> 2430.48]  It does. I know this is day-to-day stuff for you, but this is quite remarkable for those of us not in the field. Where do you see this going? I mean, you know, is this what everything inevitably has to go to?
[2430.48 --> 2444.64]  Do you think that the field will stay with lots of different technologies that are competing? What does the future look like to you? How should the rest of us be kind of thinking about the years forward in our career versus where we're at now? How much change is coming?
[2444.64 --> 2457.34]  So what we're doing is targeted at AI. For general purpose computing, where you're running Windows and you're playing a video game, probably photonic computing will not be able to contribute meaningfully.
[2457.34 --> 2476.90]  There are some really hard challenges in running general programs. So to be Turing complete, you need to have these sort of nonlinear operations. If you're a programmer, you can think about branching, like this ability to have conditionality if and then. Doing these nonlinear conditional type behaviors with optics is super hard.
[2476.90 --> 2483.70]  And so you mentioned a future where potentially there are lots of competing technologies. I think that's exactly what will happen.
[2484.14 --> 2491.82]  We've had this incredible platform with transistors and Moore's law scaling that's been so general purpose. We use it for everything.
[2491.82 --> 2503.58]  What you're going to see going forward is you'll have photonic computers for AI. And our plan is to help them dominate that field because we think that they're very well suited to the mathematics that underlies deep learning.
[2503.92 --> 2512.24]  And I think you're going to see quantum computers. I love quantum computing. I did my PhD in quantum computing, but I'm not as bullish on the right now timeline.
[2512.24 --> 2523.32]  I think they've got quite a while left, but I'm rooting for everybody working on it. And in general, I just think it's the case that we've reached the limit of transistors being able to kind of do everything good enough.
[2523.50 --> 2534.60]  And you're going to see a bunch of different types of technology platforms all competing. You'll see analog electronics at the edge. You'll see digital electronics for running your games.
[2535.02 --> 2541.82]  You'll see photonic compute units for doing your deep learning. Like my goal is to have all of Google run on light matters processors.
[2541.82 --> 2552.38]  So when you say, hey, Google, that goes through advise. That's where I want to get to. So you can kind of see this is this is how I see it. These technologies are all just suited to different kinds of problems.
[2553.12 --> 2567.90]  We're really looking forward to seeing how you bring this technology to market. It's incredibly impressive, sort of blown away by the amount of work that's gone into this and just the amazing thought process that goes along with it.
[2567.90 --> 2579.16]  We'll include links that we've talked about in our show notes for everyone listening out there. Definitely check out light matter, see what they're doing. There's links that we'll post there with some of these benchmarks and other things.
[2579.58 --> 2594.18]  But Nick, it's been a real pleasure to talk to you. It's just amazing stuff that you're doing. And I'm really looking forward to maybe talking next year and seeing how far you got and how many how many advise processors are running in Google.
[2594.18 --> 2595.82]  Awesome. Well, thanks for having me, guys.
[2624.18 --> 2631.28]  And to our longtime sponsors, Fastly, LaunchDarkly and Linode. That's all for this week. We'll talk to you again next time.
[2654.18 --> 2660.18]  We'll see you again next time.
