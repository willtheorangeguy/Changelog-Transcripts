[0.00 → 1.68] And ultimately, we don't need Docker, actually.
[1.80 → 3.66] Turns out if you build things in the right way,
[3.80 → 9.14] you can have incredibly portable, side-by-side installable native executables that work just fine.
[9.26 → 11.34] And that's essentially what the Conda system is about.
[13.50 → 16.16] Bandwidth for Changelog is provided by Vastly.
[16.52 → 18.42] Learn more at Fastly.com.
[18.66 → 21.74] We move fast and fix things here at Changelog because of Rollbar.
[21.74 → 23.56] Check them out at Rollbar.com.
[23.82 → 25.98] And we're hosted on Linde cloud servers.
[26.32 → 28.32] Head to linode.com slash Changelog.
[30.00 → 33.72] This episode is brought to you by DigitalOcean.
[34.08 → 40.74] Droplets, managed Kubernetes, managed databases, spaces, object storage, volume block storage,
[41.02 → 44.46] advanced networking like virtual private clouds and cloud firewalls,
[44.68 → 47.90] developer tooling like the robust API and CLI
[47.90 → 50.92] to make sure you can interact with your infrastructure the way you want to.
[50.92 → 54.86] DigitalOcean is designed for developers and built for businesses.
[54.86 → 61.96] Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[62.26 → 65.70] Head to do.co slash Changelog to get started with a $100 credit.
[66.10 → 68.18] Again, do.co slash Changelog.
[68.18 → 83.00] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[83.32 → 85.06] productive, and accessible to everyone.
[85.36 → 89.46] This is where conversations around AI, machine learning, and data science happen.
[89.58 → 93.94] Join the community and Slack with us around various topics of the show at Changelog.com
[93.94 → 95.84] slash community and follow us on Twitter.
[95.96 → 97.60] We're at Practical AI FM.
[98.18 → 107.90] Well, welcome to another episode of Practical AI.
[108.30 → 110.26] This is Daniel Whiten ack.
[110.36 → 113.72] I am a data scientist with SIL International,
[114.04 → 116.82] and I'm joined as always by my co-host, Chris Benson,
[117.06 → 120.30] who is a principal AI strategist at Lockheed Martin.
[120.48 → 121.14] How are you doing, Chris?
[121.54 → 122.54] I am doing very well.
[122.58 → 123.46] How's it going today, Daniel?
[123.80 → 125.32] It's going pretty good.
[125.32 → 135.16] Yeah, it's got a chance to get outside a bit over the weekend, even if it was just in my yard doing mowing and yard work and that sort of thing.
[135.32 → 138.04] So good to get away from the screen a little bit.
[138.44 → 139.12] And what about yourself?
[139.50 → 141.30] I tried to do some yard work myself.
[141.30 → 148.46] And for anyone who listened to us a couple of weeks ago, I had the broken rib, and I discovered it is not as healed as I was hoping it was.
[148.66 → 150.08] And so I stopped doing yard work.
[150.14 → 150.98] That's no good.
[151.22 → 152.42] And took lots of medication.
[152.78 → 154.42] And thus, I'm here and everything is fine.
[154.72 → 155.42] Okay, good.
[155.50 → 155.68] Yeah.
[155.68 → 162.44] The other thing I did was actually some people asked me about my AI workstation build in our Slack channel.
[162.80 → 163.66] So that's up and going.
[163.76 → 167.64] I have that pretty much running 24-7 with some type of model training.
[168.16 → 173.10] But I have a colleague who, there are two GPUs on it, so he's running some stuff on the other one.
[173.48 → 183.62] And I tried to set up, like, I got a new router for my, I intended to, like, put in this new router at my house and set my, like, other router in bridge mode.
[183.62 → 185.80] And, like, I had this really nice plan.
[186.02 → 188.50] And, you know, it was VPN access and all of this stuff.
[188.62 → 190.26] And all of that completely failed.
[190.68 → 195.96] So, you know, more network things in the future.
[196.30 → 197.02] But, yeah.
[197.38 → 198.60] Never works the first time.
[199.06 → 199.50] Exactly.
[199.82 → 200.20] Exactly.
[200.78 → 209.94] Well, speaking of very practical things and also, you know, setting up environments and all of those things, we're really excited today.
[209.94 → 218.12] Because, you know, Chris, we've mentioned so many times on the podcast, we've mentioned Anaconda or Conda in all sorts of contexts.
[218.12 → 227.22] Because, you know, it's just a pillar of the sort of data science and AI world ever since, you know, I've known about data science.
[227.28 → 228.84] I've known about Anaconda.
[229.30 → 236.04] So I'm really excited that today we have Peter Wang, who is the CEO at Anaconda, joining us today.
[236.46 → 237.18] Welcome, Peter.
[237.70 → 238.14] Thank you.
[238.22 → 239.14] Thank you for having me on the podcast.
[239.14 → 240.86] Yeah, great to have you.
[241.24 → 254.64] Before we jump into all things Anaconda, it'd be great if you could just tell us a little bit about your background and how you eventually crossed paths with this data science world and ended up helping found Anaconda and all of those things.
[255.28 → 258.64] Yeah, I'll try to give a somewhat of an abbreviated version of the story.
[258.88 → 259.74] Sure, that'd be great.
[259.86 → 260.90] It's a lot to cover all at once.
[260.90 → 261.54] It's a lot to cover.
[261.70 → 262.96] It's about 20-something years here.
[263.08 → 266.62] But I started actually, my academic background is in physics.
[266.82 → 267.56] And so I was doing...
[267.56 → 268.16] Same here.
[268.16 → 268.86] Oh, great.
[268.96 → 269.08] Yeah.
[269.18 → 271.72] Quantum information and quantum computing and physics.
[272.34 → 277.10] And when I graduated, I decided to go into the software industry, join a startup.
[277.66 → 278.70] I've always been coding.
[278.78 → 281.86] I've been coding since I was a very young child, and I've always loved it.
[281.86 → 288.14] But just given that it was the dot-com era, I thought that would be a good time to try my luck at that whole thing.
[288.52 → 296.54] But anyway, long story short, I ended up in Austin, Texas working at a Python-based scientific software consultancy.
[297.16 → 299.80] And that was kind of the early to mid-2000s.
[299.80 → 301.78] And it was there that I really...
[301.78 → 305.46] I'd always been, I guess, since 99, it was when I first started getting into Python.
[306.42 → 315.80] But then over the course of the 2000s, when I started doing a lot of work in the scientific Python, scientific numerical computing with Python, that was, you know, basically I was using Python before NumPy existed.
[316.02 → 318.12] It was still numeric or sum array and those kinds of things.
[318.12 → 327.94] But basically over that time, I started seeing through more and more of my work and my consulting jobs that Python was being adopted in places that were outside of like what you would consider scientific computing.
[328.52 → 332.90] And so we were initially thinking, oh, this is like a cooler alternative to MATLAB.
[333.04 → 340.68] And then we started seeing it in business environments, started seeing it, you know, go into like investment banks and just see it being used everywhere to do financial modelling.
[340.82 → 342.98] And I'm like, okay, well, this is very interesting, right?
[342.98 → 350.36] And so around just the turn of the decade, I guess, the last decade, the 2010s, you know, I think many of us in the community were having this realization.
[350.48 → 364.20] But I personally, as an entrepreneur, you know, I started realizing, you know, hey, with the joint evolution or transformational things of cloud computing, as well as big data, the big data creates a demand to do bigger analysis, if you will.
[364.42 → 369.84] And traditional SQL is not going to cut it when you have that much messy, you know, the four Vs of messy big data.
[370.30 → 371.14] SQL doesn't cut it.
[371.14 → 379.92] And then if you look at what hedge funds do, and hedge funds are usually kind of the leading edge of numerical modelling technology, they're all doing very sophisticated kinds of predictive analytics.
[380.26 → 382.00] And Python, they were choosing Python all the time.
[382.56 → 383.86] So there was that.
[383.94 → 397.14] And then I realized with cloud computing, it meant that every company on the planet would be able to rent computers to do, their data would end up in the cloud, and they would rent computers to do massive scale, super computing scale jobs that would have been inconceivable before.
[397.14 → 400.80] Because you'd have to ask IT, wait five years, and they might build you a data centre, right?
[401.14 → 409.28] And so with these two combined transformational forces happening, I realized, aha, Python is actually a thing we should be pushing for data analysis.
[409.48 → 413.64] And so in 2012, when I founded Anaconda, of course, at the time, it was called Continuum Analytics.
[413.64 → 420.26] I also started the Data kind of community movement and kind of that branding, if you will.
[420.30 → 423.78] It's kind of a branding exercise because all the tools are basically SciPy, right?
[423.86 → 427.74] And I mean, of course, you have Pandas in there and a few others, you know, stats models, things like that.
[427.92 → 430.54] But ultimately, it was basically SciPy rebranded for a business audience.
[430.54 → 437.04] But that pushing of Python for data analysis was something that me and a few other people, I'd say we were the pioneers, we're on the vanguard.
[437.18 → 439.00] And everyone else was looking at us like we were weird.
[439.10 → 444.56] It was either Hadoop or maybe it was going to be R as the scion for, you know, the successor to SAS.
[444.82 → 449.94] But we came on the field, and I was very vocal at that time, like, hey, Python's the thing.
[450.04 → 450.60] Python's awesome.
[451.02 → 452.34] And then people will be looking at me weird.
[452.34 → 456.28] But now I think we've proven that Python is a thing, and it's a good and useful thing.
[456.72 → 457.78] Of course, it has its warts.
[458.32 → 460.28] But anyway, that's kind of how I came to founding the company.
[460.70 → 464.34] And we created actually the Anaconda distribution as sort of like a thing we had to do.
[464.44 → 469.86] We were interested in creating distributed computing and interactive visualization and compilers and optimizing all this and that and the other.
[470.26 → 474.98] But we couldn't get any of that into people's hands because they were still struggling to install SciPy or Matplotlib.
[475.24 → 482.32] So we built a distribution called Anaconda to make that problem, particularly nasty problem even to this day, easier.
[482.86 → 484.58] And so that's just kind of continued to be a thing.
[484.94 → 485.52] So, yeah.
[485.88 → 497.24] So to take you back just a moment, I'm kind of curious, just for perspective, kind of historical perspective, as a big advocate for Python at the time, as you're looking at this, and you're kind of saying, hey, it's going this way.
[497.62 → 500.50] I'm just curious if you can take yourself back.
[500.64 → 504.54] What was it about Python then that was really driving that passion?
[505.04 → 509.42] Why was that passion not with Matlab or with R or with some of the others?
[509.52 → 511.04] What was it that really grabbed you?
[511.04 → 513.04] I'm just curious how you got motivated on that.
[513.36 → 516.28] So I am kind of a like I said, I've been programming for a long time.
[516.34 → 517.20] I know a number of languages.
[517.34 → 520.98] I started with BASIC and LOGO, as so many people do, you know, children of the 80s.
[521.26 → 522.56] But I learned a lot of languages.
[522.68 → 525.04] In fact, my professional work had been a C++.
[525.32 → 527.86] And I was a huge performance nerd and all that stuff.
[528.18 → 531.30] When I first included Python, it was, I think, version 152.
[531.70 → 532.64] And it was a Slash.post.
[532.72 → 535.10] And I was like, you know, I'm tired of all these Slash. Posts on Python.
[535.36 → 536.72] Let me finally take a look at what it is.
[536.72 → 539.34] Because Perl 6 looks like it's going to take a little while to get here.
[539.68 → 540.86] And I might as well play with Python, right?
[540.94 → 544.82] But when I started using it, I realized, oh my gosh, this is very nice.
[544.90 → 546.22] This is executable pseudocode.
[546.62 → 550.82] And furthermore, I can use Python to script my low-level C++ graphics engine
[550.82 → 555.28] and be way faster than sitting there beating my head into like C++ templates,
[555.46 → 559.86] which back at that time, they were not very well-supported by any of the compilers.
[559.86 → 561.78] So I could get more abstraction.
[562.42 → 563.90] I could prototype very fast.
[564.42 → 565.86] And it was just pleasant to work in.
[565.94 → 569.70] I felt like I could do stuff without like slogging through a pile of like syntax.
[570.40 → 572.82] So that kind of ease of use and that friendliness,
[573.06 → 576.50] even for a seasoned programmer, professional programmer like myself, was very nice.
[576.74 → 579.82] And what ended up happening over the course of the 2000s
[579.82 → 583.88] was that you could see people who are not traditional programmers.
[584.16 → 585.58] And this is going to be a very important thing
[585.58 → 589.10] as we talk about practical AI and kind of talk about the demographics
[589.10 → 590.72] of the next generation of practitioners.
[591.30 → 595.60] The people who made Python good for science and data science and all this,
[596.24 → 597.80] they're not professional software developers, right?
[597.92 → 603.48] So Jupyter was born as IPython, created by, well, I mean, Fernando, for instance,
[603.62 → 605.08] is an applied physicist.
[605.66 → 608.30] There are a lot of physicists actually banging around on an ecosystem.
[608.56 → 609.08] It's a trend.
[609.36 → 609.76] It's a trend.
[609.82 → 610.22] It's a thing.
[610.22 → 612.78] And then you've got like, you know, Jake Underplots,
[612.78 → 615.94] another contributor to like Psychic Learns and creator of Altair and whatnot.
[616.10 → 616.88] He was an astronomer.
[617.38 → 620.34] You've got like Travis Oliphant, creator of NumPy, my co-founder at Anaconda.
[620.76 → 621.94] He was a double E.
[622.18 → 624.64] You know, he was a system professor when he made NumPy.
[624.94 → 628.92] So the tools that were built in Python for doing data science and analysis
[628.92 → 633.32] and things like that were built by people who could take what was there
[633.32 → 636.74] in the Python ecosystem, modify it so it's fit for purpose,
[636.82 → 640.82] so it was pleasant to use for what they wanted to use a computing system to do.
[641.56 → 642.90] That's very different.
[643.04 → 645.68] That's sort of the product development is coming inside.
[645.80 → 646.98] It's inside the head, right?
[647.00 → 648.72] It's coming from within the person making the thing.
[648.98 → 651.60] So like, for instance, Was McKinney, the creator of Pandas,
[651.94 → 654.30] developed when he was at a hedge fund, right?
[654.40 → 657.74] And he's like, this is the thing I need to like bang around my data frames.
[657.74 → 664.54] So that's a motif in the Python ecosystem that took it from just kind of this cool,
[664.68 → 669.32] fun, easy to learn language that was, you know, embodying Guido's vision of computer programming
[669.32 → 672.04] for everyone and a nicer scripting system than Bash.
[672.44 → 676.84] We really, I think the scientific Python ecosystem took it to this next level of like,
[676.92 → 682.62] okay, this is the numerical quantitative computing system that we all wish we had, right?
[682.62 → 685.84] And it's unencumbered by like 30 years of legacy crap.
[686.20 → 689.48] It's on a language that's very nice to use, easy and approachable.
[689.64 → 694.28] But under the hood, you open it up, you know, this like nice little like approachable little
[694.28 → 695.78] Honda Accord, you open up under the hood.
[695.98 → 699.40] It's this incredibly modular like warp drive unit, right?
[699.44 → 703.82] You can bolt on things like Swig, really weird pieces of software that do incredible things,
[703.90 → 706.68] automatically generates wrappers for any of these other languages, right?
[706.70 → 708.34] So you can bolt on to Fortran, C++.
[708.34 → 710.96] We have a Justice compiler we built for it.
[711.46 → 714.78] It's a fascinating upgradable piece of kit, right?
[714.82 → 717.64] To use a British sort of term.
[718.20 → 722.40] So that's, I think, what's given its kind of the sticking power that has now kind of,
[722.74 → 724.54] you know, now we've seen that evolve more and more.
[724.72 → 729.04] And so now it's this really cool community, almost like a standard language that's very modular.
[729.30 → 731.20] And those are some of the key aspects of it.
[731.34 → 731.84] Well said.
[731.98 → 735.88] Sorry, that was a very long-winded answer, but you get me talking about true Python evangelism
[735.88 → 737.12] and I could just, you know, I can't stop.
[737.12 → 739.02] No, I totally relate.
[739.18 → 745.40] I remember, yeah, it was late in my PhD when I was working on a piece of scientific computing
[745.40 → 746.44] code in Fortran.
[746.70 → 751.64] And I remember that was the first time that I was introduced to Python because I went to
[751.64 → 753.06] go see some of our collaborators.
[753.72 → 756.48] I spent like three weeks with them working on some experiments.
[756.90 → 761.60] And I was like pair programming with this guy, and he's like, oh, you know, I'm just going
[761.60 → 762.60] to run a few things.
[762.60 → 767.76] And he had this, you know, Python script around, you know, running all of this Fortran stuff.
[767.76 → 769.68] And I remember just being like stunned.
[769.74 → 772.00] I'm like, oh, why haven't I been doing this?
[772.20 → 774.60] This guy has like a superpower of some kind.
[775.06 → 775.20] Right.
[775.20 → 781.08] But yeah, I'm wondering, you know, maybe moving from there, like you talked about how like
[781.08 → 787.18] the numerical and scientific and data science tooling that was developed in Python that was
[787.18 → 792.42] kind of developed by this sort of these groups of whether it be scientists or people in industry
[792.42 → 797.84] doing data analysis or not really maybe the traditional kind of programmer types.
[797.84 → 805.18] Do you feel like that contributed to some of the maybe struggle or inconsistency around
[805.18 → 811.84] like managing environments and installs and like how people like managed all of their stuff?
[811.92 → 816.94] Was it just because people like had a bunch of different views on those things, or what's
[816.94 → 818.16] your perspective on like?
[818.44 → 820.22] Why is packaging so terrible in Python?
[820.42 → 820.60] Right.
[820.74 → 821.82] Yeah, yeah, exactly.
[822.20 → 824.02] Well, so I can answer that question.
[824.02 → 828.54] But first, I would just have sort of a meta critique of the question, which is any system
[828.54 → 833.42] which does the number of things that Python does, I would assert, has similar kinds of
[833.42 → 834.52] software dependency issues.
[835.28 → 835.40] Okay.
[835.56 → 837.20] And even systems that don't.
[837.64 → 842.32] So JavaScript, which is all interpretable, right, has created an absolutely nightmarish scenario
[842.32 → 842.96] of packaging.
[843.40 → 846.84] And even though they have a vendor the world, everything sits in the subdirectory, vendor
[846.84 → 851.36] the world kind of approach, even though, you know, it's all pure, just pure text, there's
[851.36 → 852.02] no compilation.
[852.02 → 855.48] You can't go and gripe about Fortran ABI specifications.
[855.92 → 857.42] I mean, it's just text, right?
[857.76 → 860.80] But even JavaScript, everyone knows packaging is a nightmare.
[861.02 → 866.32] So even under the most non-compiled sort of scenario, you end up with the packaging
[866.32 → 870.86] morass because you have an ecosystem that is able to build on each other sort of things.
[871.06 → 872.94] Yeah, can do so many things.
[873.08 → 873.26] Right.
[873.42 → 876.48] But in the case of Python, think about what we're talking about.
[876.84 → 877.96] Gluing to Fortran code.
[878.18 → 878.50] All right.
[878.58 → 880.22] Well, you know, maybe Perl has nicer packaging.
[880.22 → 882.18] Where's the Perl glue to Fortran code?
[882.22 → 884.24] And where is that being used on a million nodes?
[884.36 → 884.48] Right.
[884.74 → 885.12] It's not.
[885.60 → 887.36] So I think there's a thing to recognize.
[887.52 → 890.28] Like the reason why your duct tape has all this crap stuck to the back of it is because
[890.28 → 890.76] it's sticky.
[890.84 → 891.32] It's duct tape.
[891.74 → 892.84] So Python is a glue language.
[892.96 → 895.14] Of course, it gets a bunch of cruft glued into it.
[895.18 → 898.58] And now we have a much harder problem to solve because we do speak to so many different
[898.58 → 898.96] things.
[899.12 → 899.26] Yeah.
[899.26 → 899.50] Okay.
[899.56 → 903.06] Now, that being said, I think fundamentally one of the reasons why Python packaging is
[903.06 → 909.80] difficult has been that packaging was treated as a second class concern by the BDFL.
[909.96 → 910.04] Right.
[910.08 → 914.50] So Guido clearly admitted very early on he just didn't think about it that much and didn't
[914.50 → 916.28] really, you know, it wasn't a big problem for him.
[916.34 → 917.56] It wasn't exciting or interesting for him.
[917.88 → 919.42] And he's not really apologizing for it.
[919.42 → 920.72] He's just saying this is kind of the way it was.
[920.76 → 924.10] It was someone else's problem to go and figure out whether it was the Philip By with step
[924.10 → 926.80] tools or, you know, the disutilized days, whatever it might be.
[926.96 → 929.88] It was really not a thing he was super interested in.
[930.34 → 934.72] And then when we came along, actually, there's the very first Pi Data workshop I put together
[934.72 → 936.84] March 2012, three months after we started the company.
[937.34 → 939.18] And Guido was working for Google at the time.
[939.24 → 940.46] He came by and stopped by.
[940.88 → 941.90] We're all very excited to see him.
[942.34 → 945.02] People gave him a lot of crap about like, hey, when are we going to get a matrix multiplication
[945.02 → 945.54] operator?
[945.94 → 947.38] But then we also asked him about packaging.
[947.38 → 952.74] We're like, hey, can you help us get the core packaging folks in the core dev to work
[952.74 → 955.90] with us on packaging stuff, you know, in the scientific Python ecosystem?
[956.08 → 957.66] Because it's just been a mess for a very long time.
[958.32 → 963.02] And his answer was, look, it's possible that your needs are so exotic that you should just
[963.02 → 963.98] go do your own thing.
[964.16 → 964.92] Like, don't worry about it.
[964.92 → 965.94] Just solve your own problem.
[966.38 → 967.44] So we're like, OK.
[967.74 → 968.68] So we did.
[968.84 → 972.96] You have to understand by that time that the people in the SciPy ecosystem had been fighting
[972.96 → 977.36] various multiple genealogies and multiple generations of Python packaging tools.
[977.38 → 978.34] for 10 years.
[978.74 → 978.84] Right.
[978.88 → 979.92] It had never really been great.
[980.54 → 984.52] And so by that time, we were like, OK, let's just solve this once and for all.
[984.90 → 986.26] And we realized something very fundamental.
[986.40 → 987.78] And this is true for any system.
[988.02 → 988.88] This has nothing to do with Conda.
[989.16 → 993.06] This is true for any system that touches compiled code.
[993.06 → 995.32] And this is now the second part of my question.
[995.60 → 996.56] The second part of my answer.
[996.64 → 998.74] The first part of my answer was that Guido didn't really care.
[999.00 → 1000.64] So it was kind of festering.
[1001.02 → 1006.64] The second part of it is that software development, basically every single operating system that
[1006.64 → 1008.68] is a PC-based operating system sucks.
[1009.12 → 1012.50] And so we have inherited the long shadow of 1970s technical debt.
[1012.90 → 1013.12] Right?
[1013.42 → 1017.28] If you're on Linux, any of you guys heard of a thing called Docker or use a thing called
[1017.28 → 1017.62] Docker?
[1018.18 → 1018.44] Maybe?
[1018.66 → 1019.64] Just a little thing, right?
[1019.70 → 1020.32] Love Docker.
[1020.40 → 1021.46] Why did Docker come about?
[1021.78 → 1022.54] Docker, what's that?
[1022.80 → 1024.12] Because you even have RPM.
[1024.40 → 1026.32] I mean, what Linux distro doesn't have a package manager?
[1026.52 → 1027.58] And yet you use Docker.
[1027.76 → 1033.58] Because the concept of having static linkage or dynamic linkage between software libraries,
[1033.58 → 1038.86] even though we have a tried and true robust dynamic linker system, it's terrible, right?
[1038.98 → 1040.04] You go to Macintosh.
[1040.18 → 1041.90] OK, so maybe use Homebrew, right?
[1041.94 → 1045.02] That's kind of the preferred kind of package manager on there.
[1045.14 → 1048.30] And of course, eventually Apple with App Store will kill all of that third party stuff.
[1048.50 → 1050.00] But for now, we have Homebrew.
[1050.32 → 1051.62] Well, you start building stuff with Homebrew.
[1051.78 → 1055.34] What if you want to have multiple different versions of libraries, and you have to build
[1055.34 → 1056.22] framework builds of them?
[1056.24 → 1057.86] And those framework builds are incompatible with each other.
[1058.14 → 1060.34] And some of them need access to like the raw GL context.
[1060.98 → 1063.30] God forbid you need to do any of that stuff, right?
[1063.30 → 1067.44] So every single system and Windows, notoriously, DLL hell, right?
[1067.52 → 1069.60] Literally is the Windows DLL format, right?
[1069.72 → 1071.20] And they do Windows side by side.
[1071.32 → 1072.98] They have all sorts of things that they do.
[1072.98 → 1077.78] It's an unsolved problem because we've inherited the C linker and loader.
[1078.44 → 1082.12] And ultimately, that is part of the core ABI spec of the underlying operating system.
[1083.00 → 1087.78] So now, if you're just a couple of physics-turned-software nerds like me and Travis,
[1088.36 → 1089.32] you're like, OK, holy crap.
[1089.38 → 1091.50] How do we ship LVM with our dynamic compiler?
[1091.92 → 1096.32] How do I ship a pile of JavaScript dependencies with like Bokeh and our interactive web this
[1096.32 → 1096.62] stuff?
[1096.96 → 1098.08] How do I do any of these things?
[1098.14 → 1098.62] How do we ship?
[1098.88 → 1101.66] For instance, you know, people, do you guys use Jupyter Notebooks?
[1101.78 → 1103.56] Or if you're familiar with Jupyter Notebooks, right?
[1103.60 → 1103.72] Yeah.
[1103.88 → 1105.02] And have you ever converted them?
[1105.02 → 1108.46] Have you ever used convert to convert from a notebook to like a PDF or something like
[1108.46 → 1108.70] that?
[1108.94 → 1109.06] Yeah.
[1109.22 → 1109.48] Yeah.
[1109.74 → 1114.70] Did you know, fun thing, that it uses a thing called Pandoc underneath, which has an embedded
[1114.70 → 1115.58] Haskell compiler?
[1116.34 → 1116.52] Okay.
[1116.52 → 1121.56] So like, in order to ship convert on Windows, you have to go and build a Haskell runtime
[1121.56 → 1122.38] on Windows.
[1123.08 → 1123.86] What a web of things.
[1123.94 → 1124.98] What a web of things, right?
[1125.30 → 1129.02] But this is the kind of nonsense that we end up having to deal with.
[1129.82 → 1133.98] I call it nonsense, but really, it's just, we realized that it was more than just the
[1133.98 → 1135.26] C, A, B, I, linkage, whatever.
[1135.44 → 1137.16] And this was back in 2012, pre-Docker.
[1137.54 → 1140.64] But even Docker then on Windows, not a really great story, right?
[1141.04 → 1142.76] And ultimately, we don't need Docker, actually.
[1142.76 → 1148.16] Turns out if you build things in the right way, you can have incredibly portable, side-by-side
[1148.16 → 1150.88] installable native executables that work just fine.
[1151.50 → 1153.50] And that's essentially what the Condos system is about.
[1153.62 → 1157.84] It's about, rather than wrapping everything up in a hermetic sort of Docker environment,
[1158.22 → 1163.74] we create a very simple specification of what packages do you want, and then we have a recipe
[1163.74 → 1168.86] system that then has a build system behind it that is able to build native binaries for
[1168.86 → 1172.56] every single platform, optimized for every single kind of hardware version that we support.
[1172.76 → 1175.34] And that's ultimately, you know, when it works well, it works well.
[1175.34 → 1178.94] When it falls over, then it can be a little bit hard to untangle exactly what the problem
[1178.94 → 1179.16] was.
[1179.32 → 1180.42] And we're working on that, of course.
[1180.64 → 1182.88] But that's ultimately the motivation there and why it's terrible.
[1182.98 → 1185.04] I think we inherited the long shadow of the 70s.
[1185.48 → 1187.28] C, you know, linker, loader, I'm looking at you.
[1187.48 → 1191.86] And then also we inherited some of Guido's, you know, preferences in language development.
[1192.20 → 1193.00] And I'm not blaming him.
[1193.02 → 1193.38] I love him.
[1193.40 → 1195.28] And I'm so grateful for what he's done with the language.
[1195.44 → 1197.14] But anyway, you guys asked.
[1197.24 → 1198.36] So that's the honest answer.
[1198.36 → 1215.32] What up, nerds?
[1215.38 → 1217.24] Jared Santo here, your humble producer.
[1217.66 → 1219.60] I'd like to tell you about something new.
[1219.72 → 1221.54] We're beta testing around practical AI.
[1221.96 → 1225.78] It's a membership program, which we think could be really valuable for the whole community.
[1225.78 → 1231.08] We call it Changelog++, and it's the best way to directly support practical AI and all
[1231.08 → 1234.26] of the podcasts, videos, and other stuff we create here at Changelog.
[1234.64 → 1238.48] We have big plans and ambitions for this, but we are experimenting for now to make sure
[1238.48 → 1239.10] there's interest.
[1239.56 → 1243.84] That means when you sign up today, you get practical AI and whatever Changelog shows you
[1243.84 → 1246.14] listen to now, except no ads.
[1246.56 → 1249.22] I guess that means this part you're listening to right now, it'll be gone.
[1249.78 → 1254.88] We also have some extended episodes planned, bonus content, merch store discounts, and a lot
[1254.88 → 1255.42] of ideas.
[1255.66 → 1260.10] But since it's such early days, we are offering memberships at a 40% discount for early adopters.
[1260.54 → 1262.32] That disappears at the end of August.
[1262.46 → 1267.50] So head to changelog.com slash plus to join today, lock in that discount, get closer
[1267.50 → 1269.28] to the metal, and make the ads disappear.
[1269.78 → 1273.32] Once again, that's changelog.com slash plus.
[1273.52 → 1275.98] We'd love to have you supporting us as a member.
[1284.88 → 1292.54] Okay, so I'm going to start off the next section as we're starting to dive into Anaconda itself
[1292.54 → 1295.68] with the obvious question you've probably been asked a billion times.
[1295.88 → 1302.12] I get Python, Snake, and Anaconda, but I am curious why specifically Anaconda and if
[1302.12 → 1305.74] there were any alternative names that might have been fun that you could share with us.
[1306.32 → 1306.76] Yeah.
[1306.96 → 1307.80] Well, it was.
[1307.92 → 1309.28] So I will give you the origin story.
[1309.28 → 1313.58] It was at a moment at that Data workshop when we were looking at trying to promote
[1313.58 → 1315.58] a Python alternative to Hadoop.
[1316.02 → 1320.38] At the time, there was a distributed Map Reduce system built around Erlang that had come out
[1320.38 → 1321.94] of Nokia, and it was called Disco.
[1322.66 → 1325.28] And so I was like, wow, this is nice.
[1325.36 → 1329.28] It's a nice Python Map Reduce if people really want Map Reduce, and we should get this
[1329.28 → 1329.66] to people.
[1330.04 → 1332.54] And then I realized I had this sort of like moment of truth.
[1332.62 → 1336.34] I was like, wait, we can't even ship SciPy to people after 10 years, 12 years.
[1336.62 → 1338.94] How are we going to ship Erlang runtimes to people, right?
[1339.28 → 1340.86] And so I turned around, and I looked at Travis.
[1340.90 → 1343.84] We're sitting in the back of the room and I looked at him and I said, we need to create,
[1343.92 → 1346.28] if we're going to really do this, we have to, you know, a bunch of stuff's going to have
[1346.28 → 1346.74] to go rolled in.
[1347.10 → 1349.90] We need to create a new distribution of Python for big data.
[1350.38 → 1353.02] So let's call it Anaconda because it's a big snake, right?
[1353.74 → 1355.86] It was no, it was like literally it happened in a flash.
[1355.86 → 1358.56] It was just, there was no great deliberation about this.
[1359.88 → 1364.54] And when you're saying, so just for listeners who are maybe, maybe a little bit newer to this
[1364.54 → 1366.82] world, when you're saying a specific distribution of Python.
[1366.82 → 1372.36] So what does that specifically change about your local environment that you're using this
[1372.36 → 1373.14] distribution of?
[1373.24 → 1379.86] Is it just around the like using Conda instead of pip or is it a whole different Python interpreter?
[1380.08 → 1383.10] What are the sort of specifics when you say specific distribution?
[1383.64 → 1383.76] Yeah.
[1383.84 → 1388.10] So the specifics are that we build the Python interpreter itself, and we build the installer
[1388.10 → 1388.70] around it.
[1388.70 → 1393.48] And then all the packages, because when you build packages that have binary or C extension
[1393.48 → 1398.82] module or C++, they have to be built with a compatible compiler set as what you built
[1398.82 → 1400.22] the interpreter with.
[1400.26 → 1401.68] Otherwise you SEG vault, right?
[1402.08 → 1406.36] And then every subsequent package that has C dependencies needs to be built with the same
[1406.36 → 1406.98] compiler set.
[1407.34 → 1411.02] Otherwise you end up with runtime SEG vaults, which is no fun for anybody.
[1411.02 → 1415.02] So we basically have created a normalized build system.
[1415.54 → 1419.90] It's like a Lego ground baseplate that has equal spaced studs and is level.
[1420.32 → 1422.74] And then you can put everything on it, but you need that first baseplate.
[1422.84 → 1425.22] So that's what the Anaconda runtime really is.
[1425.32 → 1427.22] So it's a Python interpreter that we've built.
[1427.46 → 1431.60] And then you can either get Minions, which is just that Python interpreter with the standard
[1431.60 → 1437.44] library and the Conda package manager, or you can get Anaconda, which comes with like
[1437.44 → 1440.84] 250 or something, 220 packages prebuilt as well.
[1440.92 → 1442.22] So pre-populated baseplate.
[1442.48 → 1448.28] But the idea of the Anaconda system is that using Conda, you can then install packages into
[1448.28 → 1450.64] this that fit on that baseplate and fit with each other.
[1451.00 → 1453.34] That being said, there's nothing stopping you from using PIP.
[1453.42 → 1454.42] I mean, I use PIP, right?
[1454.42 → 1460.36] You can PIP install other modules in, but if they use, if they have C dependencies or pre-compiled
[1460.36 → 1465.14] binary components, it's better to install those with Conda because then you know that
[1465.14 → 1466.16] those are compatible.
[1466.16 → 1469.84] And especially as we're talking about in the context of AI and ML and things like that,
[1470.22 → 1473.22] obviously accelerated hardware is a deeply important topic, right?
[1473.52 → 1478.76] And so you want to get the version of the package that's built for your piece of hardware.
[1479.06 → 1483.26] And sometimes when people go and build binaries, and they make PIP wheels available, they have
[1483.26 → 1486.76] to build those with the lowest common denominator of hardware flags.
[1486.82 → 1491.16] So you might be paying $3,000 for a Leon processor, but only getting basically a $500 or $200
[1491.16 → 1495.46] Leon processor worth of capability because certain flags are not turned on, right?
[1495.46 → 1499.50] And this is the kind of thing that is not important for like a huge number of users,
[1499.68 → 1501.74] but really important for some users.
[1502.02 → 1504.02] And of course, as time rolls on, more and more important for everyone.
[1504.48 → 1505.10] So that's what that means.
[1505.16 → 1507.94] We can install Anaconda into a user land directory.
[1508.08 → 1510.24] You don't need admin permissions, and can install stuff.
[1510.30 → 1511.22] It's all self-contained in there.
[1511.58 → 1514.40] If you don't like it, you can blow it away with one directory remove command.
[1514.40 → 1517.88] And it stands separate than your system Python than anything else.
[1518.32 → 1519.34] So that's really what...
[1519.34 → 1521.14] So people use Honda with Docker all the time.
[1521.20 → 1522.06] It's a very common pattern.
[1522.50 → 1523.32] Yeah, that makes sense.
[1523.60 → 1528.76] So a lot of these packages, like you're talking about, you know, Scikit-learn or Pandas or
[1528.76 → 1530.02] NumPy or these other things.
[1530.36 → 1534.62] Generally, people think of this sort of landscape of open source data science tool.
[1534.62 → 1540.06] So is what portions of the sort of Anaconda system are open source?
[1540.26 → 1546.28] And how did you, when you kind of entered into this journey, how did you go about navigating
[1546.28 → 1551.86] that open source landscape where, you know, there are all sorts of things that have all sorts
[1551.86 → 1558.48] of licenses and, you know, building a product around open source is kind of an interesting
[1558.48 → 1563.82] thing, especially I think it's, you know, it seems to be a lot of things like that are
[1563.82 → 1564.58] trending now.
[1564.76 → 1569.48] But I think, you know, when this whole field was getting started, you know, there probably
[1569.48 → 1574.98] weren't as many examples of businesses built around like open source.
[1575.30 → 1577.62] So yeah, how do you all think about that?
[1577.66 → 1580.48] And how did that grow as you were starting out?
[1581.02 → 1581.16] Yeah.
[1581.52 → 1586.58] So Travis and I are both ardent supporters of open source because I think it leads to open
[1586.58 → 1587.06] innovation.
[1587.06 → 1590.32] So for me, that's the almost like open source is almost a means to an end.
[1590.40 → 1591.46] It's not an end unto itself.
[1591.46 → 1596.10] So if something's open source, but it leads to single vendor innovation, that's still
[1596.10 → 1596.50] bad.
[1596.88 → 1600.64] And we have examples of that now, actually, in the burgeoning AI space.
[1600.70 → 1605.26] And I would encourage people to look beyond merely the kind of astroturf like, oh, well,
[1605.26 → 1606.02] this is open source.
[1606.38 → 1609.50] Well, all the contributors come from one company, whether it's a small one or a big one.
[1609.58 → 1610.90] It's like, who's going to get in there?
[1610.92 → 1611.70] Are you going to accept patches?
[1611.82 → 1612.64] Can we really fork it?
[1612.68 → 1614.98] And you're not going to sue us for something?
[1614.98 → 1621.68] For me and Travis, it's been watching what the open scientific software ecosystem was
[1621.68 → 1622.26] able to produce.
[1622.36 → 1624.58] That collaboration was so generative and so amazing.
[1625.08 → 1626.70] We want to ensure that that would endure.
[1627.44 → 1631.72] So in building a business and trying to build business models around open source, that was
[1631.72 → 1633.56] part of our entrepreneurial exploration of that.
[1633.84 → 1640.60] Can we build a company and have a good one that fosters and sustains open source innovation?
[1641.20 → 1642.84] So everything in Anaconda is open source.
[1642.90 → 1643.96] The recipes are open source.
[1644.16 → 1645.90] I mean, the Condon Package Manager is open source.
[1646.06 → 1648.14] That's always been the case from the very beginning, right?
[1648.16 → 1651.20] So we don't make our money by holding back any of that stuff.
[1651.74 → 1656.06] We started with a support and consulting kind of model because, again, Python for data science
[1656.06 → 1657.08] is kind of a new thing.
[1657.60 → 1660.14] And there are plenty of our projects that were nascent, right?
[1660.14 → 1664.34] Whether it was Numb or whether it was any of these other projects, we had a lot of consulting
[1664.34 → 1665.48] demands for those kinds of things.
[1665.52 → 1666.08] So we did that.
[1666.62 → 1670.58] As we shifted into product-oriented mode, what we realized was that enterprise payments,
[1670.60 → 1675.68] especially enterprise pains addressed by software, they're not really about proprietary
[1675.68 → 1676.62] closed source features.
[1677.18 → 1680.80] They're about enterprises wanting to have roadmap transparency, having a vendor, a throat
[1680.80 → 1683.82] to throttle when something goes wrong, all these other kinds of things.
[1684.02 → 1686.76] So Red Hat demonstrated how you can do this in a fairly sustainable way.
[1687.28 → 1691.60] So we, our first product that we actually shipped was a package server that you could
[1691.60 → 1693.36] have an IT guy could say, you know what?
[1693.56 → 1696.68] I don't want GPL packages coming in here because legal, right?
[1696.68 → 1701.34] So I want to have all the data scientists internally be able to point to my internal
[1701.34 → 1703.66] mirror of the Anaconda ecosystem.
[1703.90 → 1708.56] But I get to blacklist all of these or zero out all of these GPL packages.
[1708.82 → 1712.96] I get to set which versions are available in various channels.
[1713.16 → 1717.24] So the prod cluster that I manage will only ever get package updates from the prod channels.
[1717.36 → 1718.90] And I get to flip the bid on that one.
[1718.90 → 1722.84] But the devs, you know, the data scientists who have the sandbox, and they want the latest
[1722.84 → 1726.10] bleeding edge version of something or the other, they can knock themselves out, right?
[1726.16 → 1728.80] And now they're not complaining that I'm holding them back from their work.
[1729.02 → 1732.10] So that package repository server, I mean, we still sell that today.
[1732.18 → 1733.06] It's a very popular product.
[1733.14 → 1736.04] And it addresses a deep need that enterprises have.
[1736.12 → 1737.50] So that's kind of how we think about the product development.
[1737.82 → 1742.76] We also do have an enterprise machine learning platform, just as like a Domino or an H2O,
[1742.84 → 1743.54] whatever kind of thing.
[1743.88 → 1745.56] So we've had that we've been selling for a while.
[1745.56 → 1751.30] But I think that for us looking at kind of the growth of the packaging demand in the ecosystem,
[1752.02 → 1755.70] you know, the package server for us is really kind of a no-brainer enterprise offering.
[1756.04 → 1757.86] I'd like to actually follow up on that exact thing.
[1757.98 → 1763.16] And as you're looking at organizations, companies, businesses out there that are trying to find
[1763.16 → 1768.00] their way into data science and Anaconda being one of the major avenues on doing that,
[1768.38 → 1774.44] what is the value proposition that a CIO at some company should be looking at when they're
[1774.44 → 1778.82] thinking about, do I go Anaconda or do I go, you know, some other route?
[1778.94 → 1779.86] Do we mix and match?
[1780.30 → 1783.74] You know, because that is a question that companies are dealing with every day right now.
[1784.02 → 1784.14] Right.
[1784.36 → 1788.40] What should that CIO be thinking about when they're trying to decide whether they want
[1788.40 → 1789.40] to go with Anaconda or not?
[1789.72 → 1789.94] Yeah.
[1790.04 → 1794.14] So there's actually not very much that's competitive with our package, sort of package
[1794.14 → 1794.74] e-commercial.
[1795.06 → 1797.60] We'll call it the commercial license, you know, of Anaconda.
[1797.60 → 1802.82] Because ultimately what we're solving is a unique but important problem, which is
[1802.82 → 1804.44] the software supply chain.
[1804.98 → 1805.12] Right.
[1805.20 → 1806.52] Now you see a lot of companies.
[1806.70 → 1809.98] It's actually shocking to me because I've been involved in open source since like 95,
[1810.28 → 1811.40] right, in the early Linux days.
[1811.72 → 1815.74] But even today, there are companies that are just starting to understand like, oh, yeah,
[1815.76 → 1818.46] maybe we should figure out how to use open source in a governed way.
[1818.62 → 1818.80] Right.
[1818.98 → 1822.78] They're starting to have that conversation at the CIO and the IT leader level.
[1822.78 → 1828.76] And when it comes to ML and AI, you know what, the ecosystem moves so fast, it's a whole wild
[1828.76 → 1830.04] west of things out there.
[1830.60 → 1836.54] Anaconda is basically like the only company that is out there as your last outfitter between,
[1836.66 → 1838.24] you know, civilization and the wild west.
[1838.74 → 1845.60] And so if you actually want a build of NumPy or of Scikit-learn to go and run on your customer
[1845.60 → 1850.58] sensitive PII HIPAA data and not have it just come from some like grad students like, you
[1850.58 → 1854.52] know, server somewhere under their desk, you have to talk to a vendor.
[1854.66 → 1857.46] You have to have someone who will actually talk to your legal people, you know, sign
[1857.46 → 1858.02] us some lines.
[1858.50 → 1858.86] We're that.
[1858.98 → 1859.26] We're it.
[1859.34 → 1863.18] So we actually are compatible with a whole host of other, you know, I talk about how
[1863.18 → 1867.32] our ML platform is, you know, competitive with things like Domino or maybe a SageMaker
[1867.32 → 1868.02] or some of these other things.
[1868.40 → 1872.82] But our package server and our commercial license for the Anaconda distribution is not
[1872.82 → 1873.60] competitive with those things.
[1873.60 → 1875.04] It goes hand in hand with those things.
[1875.52 → 1878.54] So in fact, we have a partnership with Red Hat, a partnership with IBM that we've just announced
[1878.54 → 1884.10] earlier this year, where our package server and those commercial license packages that
[1884.10 → 1886.74] is going out to the world via those channels.
[1886.98 → 1888.66] Because again, there's not much competitive with that.
[1888.76 → 1893.04] So what the CIO should be thinking about is how do I govern the software bits that actually
[1893.04 → 1897.96] run, you know, like this Docker that, you know, this like three gigabyte opaque binary
[1897.96 → 1900.94] that my data scientist like intern just handed me.
[1901.34 → 1903.64] How do I how good do I feel about running that in production, right?
[1903.64 → 1908.14] If I want actually some transparency into it, if I want repeatability, like an aerospace
[1908.14 → 1912.04] manufacturer was talking to me at Pylon a couple of years ago and the data scientist and aerospace
[1912.04 → 1916.56] engineer there, he said, we have to demonstrate to the FAA that we can run these wing models
[1916.56 → 1919.96] 50 years, 50 years after the last plane rolls off the line.
[1921.08 → 1926.32] So it can't be some Docker file with a run command NPM install this or pseudo pip update
[1926.32 → 1926.88] that, right?
[1927.16 → 1931.50] You've got to have something that you can point to and everybody up and down the governance
[1931.50 → 1932.52] chain feels good about.
[1932.52 → 1939.86] And right now that topic of open source governance for MLI is not a broadly discussed topic.
[1940.04 → 1944.96] But of course, you guys, you know, as practitioners understand the importance of that, especially as
[1944.96 → 1947.58] predictions and predictive models come under more regulatory scrutiny.
[1948.30 → 1952.56] So, yeah, we have, I think, a relatively distinguished and unique offering in that regard.
[1952.86 → 1953.48] Yeah, I'm curious.
[1953.90 → 1959.56] You mentioned a couple of times, and I guess this is a product of kind of this shift in,
[1959.56 → 1964.62] you know, the first, the hype around data science and everybody's doing data science.
[1964.62 → 1966.20] Now we're kind of all shifting.
[1966.56 → 1968.52] We all want to do AI, right?
[1968.60 → 1973.02] And if we do AI, then we get bigger salaries and that sort of thing.
[1973.02 → 1981.52] So how have you seen this shift towards AI and wanting to do AI things as opposed to sort of maybe
[1981.52 → 1982.90] just data science?
[1983.00 → 1988.38] How has that influenced the way that you're interacting with clients and the things that they want to
[1988.38 → 1993.54] do and the open source projects that you're wanting to support within the Anaconda ecosystem?
[1993.86 → 1998.44] How has that shifted things and made you think about things differently or the same?
[1998.60 → 2000.02] Or what does that look like?
[2000.52 → 2004.86] Well, it's made, well, without getting too snarky, it's made me very cynical about the tech business
[2004.86 → 2005.24] press.
[2005.92 → 2007.60] But maybe I was already at maximum.
[2007.82 → 2009.40] I already maxed out my cynicism there already.
[2009.56 → 2009.80] So maybe.
[2010.02 → 2011.44] Yeah, you're just riding a plateau.
[2011.54 → 2012.76] Now it's now flipped around.
[2012.96 → 2014.66] Now it's now flipped around, right?
[2014.70 → 2015.76] Because I used a sign integer.
[2015.94 → 2017.10] Now I'm a negative cynicism.
[2017.10 → 2022.20] And the challenge is this, that as someone who kind of understands the technology in
[2022.20 → 2025.76] the space, I think we're very close to some things that are really very close to what
[2025.76 → 2027.02] we could call AI, right?
[2027.06 → 2029.32] So there's a real, there's a substance there.
[2029.72 → 2036.84] But the second order, third order, far field wave of interest and hype is way bigger than
[2036.84 → 2038.84] what's justified, I think.
[2039.28 → 2042.58] But at the same time, if we, I mean, GPT-3 is jaw dropping, right?
[2042.62 → 2045.22] I mean, you look at some of these things, it's like, holy cow.
[2045.22 → 2045.34] No.
[2045.94 → 2047.70] And then we, and there are deeper questions there.
[2047.74 → 2051.76] Like we have to think about this technology is like at an intellectual level, it's like
[2051.76 → 2052.92] a nuclear age revolution.
[2052.92 → 2054.40] We can't just put this in everybody's hands.
[2054.48 → 2056.46] There's, we have to be serious about how we use this stuff, right?
[2056.94 → 2062.46] But, but, but all that aside, I think that what people are maybe sometimes miss in that
[2062.46 → 2068.16] business level kind of up levelling of like AI and all this kind of stuff is that it is a
[2068.16 → 2071.28] ladder of needs or a Maslow hierarchy, right?
[2071.28 → 2075.42] If your business sucks at basic data management, if you can't even run SQL queries over your
[2075.42 → 2077.14] stuff, you're not going to get to do data science.
[2077.44 → 2080.20] And if you can't do data science, your AI is going to be kind of crap.
[2080.36 → 2081.60] Like you're not going to do any real AI.
[2081.68 → 2082.54] You're going to spend a lot of money.
[2083.08 → 2086.14] No one's going to stop taking your dollars just because of bad data infrastructure.
[2086.32 → 2088.58] Consultants will take your dollars all day long.
[2088.74 → 2092.74] They're going to produce some like clickable BI chart and charge a couple million dollars
[2092.74 → 2093.08] for it.
[2093.24 → 2094.86] You won't have gotten the value out of it, right?
[2095.16 → 2099.12] But then, you know, whoever has ever gotten fired for having a bad IT project, it's just somebody
[2099.12 → 2099.86] else's dollars, right?
[2100.24 → 2104.82] So again, like I said, I have a lot of cynicism about how this stuff works.
[2105.32 → 2109.24] But I do think that legitimately, but in a more serious tone to answer your question,
[2109.90 → 2112.98] in steering the ship at Anaconda and looking at where we make our investments, you know,
[2113.02 → 2115.06] we support the development of some of the fundamental tools.
[2115.40 → 2119.54] So we invest in things like Dark, which are next generation distributed computing in Python.
[2120.08 → 2124.12] We support things like Numb, which give us more performant just across the board.
[2124.12 → 2127.42] It makes the low level libraries very performant on next gen hardware, right?
[2127.42 → 2131.66] So hardware manufacturers like Intel and NVIDIA partner with us to, you know, add improvements
[2131.66 → 2132.24] to the compiler.
[2132.84 → 2134.98] Pandas, we support fundamental development of things like Pandas.
[2135.36 → 2137.42] So I think my thing is this.
[2137.48 → 2143.22] I'm fixated on empowering the practitioners and helping them up-level their data literacy
[2143.22 → 2144.24] across the organization.
[2144.82 → 2147.72] So my investment is not going to be at the cutting edge of the hype.
[2148.08 → 2151.52] The way I want to steer the community, the way I steer my friends who are, you know,
[2151.72 → 2154.82] movers and shakers in the community is to really think about this.
[2154.82 → 2160.26] If we are to have this technology be something that's transformative for humanity as a whole,
[2160.70 → 2166.16] then it cannot become an ivory tower where there are a few acolytes who know how to use a few
[2166.16 → 2171.28] privileged proprietary systems to go and tell the rest of us what the predictions are, right?
[2171.32 → 2172.32] This cannot be how this works.
[2172.40 → 2176.64] It has to be a democratized transformation of how every business, every person thinks about it.
[2176.68 → 2181.56] And in fact, an underlying thing at Anaconda is that we want to make sure that everyone gets
[2181.56 → 2182.14] data literacy.
[2182.14 → 2185.86] That's why we will always have this free capability.
[2186.12 → 2189.68] We don't charge for like a few hundred extra rows on this library or something like that.
[2190.14 → 2194.36] It's always free and unfettered access because I want every school kid in Bangladesh to be
[2194.36 → 2199.94] able to model quantitatively in a Jupyter notebook why some hotshot politician enacted some policy,
[2200.32 → 2200.48] right?
[2200.60 → 2201.64] Everybody, everywhere.
[2201.80 → 2202.98] Math is empowering for everyone.
[2203.36 → 2204.70] And this is just computational math.
[2205.20 → 2208.88] So from that perspective, there's a deep moral aspect to my mission and to the mission
[2208.88 → 2209.38] at Anaconda.
[2210.00 → 2215.42] Now for AI, ML and data science, the transformation I've seen in the field is that, yeah, everyone
[2215.42 → 2216.24] talks about AI.
[2216.46 → 2219.82] But then when you get all the practitioners together, you know, we all know to put the
[2219.82 → 2220.78] stuff on the side.
[2220.88 → 2223.46] Like we put the NBA speak to the side, and then we all just talk about the real stuff.
[2223.54 → 2224.96] And it's like usually data engineering.
[2225.28 → 2227.28] It's usually, well, software bits, right?
[2227.28 → 2228.52] Who's setting up the working environment?
[2228.78 → 2230.42] What version of pandas are you using?
[2230.76 → 2231.60] You know, et cetera, et cetera.
[2231.60 → 2235.98] GPUs that people are actually now starting to really model their hardware footprint as
[2235.98 → 2238.18] they're approaching data jobs, which I think is fantastic.
[2238.34 → 2240.14] It's what should have always been done, right?
[2240.62 → 2245.96] It's actually a practice that IT has left behind for like 15, 20 years in the Java era.
[2246.40 → 2247.44] Now hardware matters again.
[2247.52 → 2248.46] Vectorization matters again.
[2248.52 → 2249.42] And it's a beautiful thing.
[2249.92 → 2251.94] So maybe I sort of lost my point here.
[2252.20 → 2253.54] I'm just like, no, we're ranting.
[2254.54 → 2255.74] No, it's perfect.
[2255.94 → 2256.20] But it's fine.
[2256.34 → 2256.44] Yeah.
[2256.44 → 2260.08] I mean, I think some of those things that I see, like you're talking about, definitely
[2260.08 → 2260.86] resonate with me.
[2260.86 → 2265.74] I definitely think like when I first got into data science, like the hardware wasn't really,
[2266.12 → 2267.94] I wasn't thinking a ton about it.
[2268.16 → 2273.60] And I was also, like you're saying, you know, shipping off that like three gigabyte containers
[2273.60 → 2275.62] to, you know, DevOps Doug.
[2275.68 → 2280.34] And he was, you know, figuring out and, you know, hating me because it took however long
[2280.34 → 2282.20] to build and all of those things.
[2282.20 → 2285.52] So it's good to hear you talk about some of those things.
[2285.52 → 2290.48] And I definitely see how, you know, a lot of these main components that you're supporting
[2290.48 → 2292.04] are really fundamental.
[2292.36 → 2297.54] I was just doing some speech recognition stuff end of last week over the weekend on
[2297.54 → 2299.06] Video Nemo.
[2299.18 → 2304.04] And they were like, well, you need to install Numb to, you know, speed up some of these
[2304.04 → 2309.24] like data augmentation things for the speech files, which is like a main component of the
[2309.24 → 2309.46] thing.
[2309.54 → 2310.60] And it's really driving that.
[2310.60 → 2316.28] And, you know, that really influences the actual, you know, AI training and the quality
[2316.28 → 2316.76] of that.
[2317.00 → 2321.76] So this sort of pre-processing things and all of those are really, you know, really fundamental.
[2322.20 → 2326.70] I don't know if this factors into your thoughts around packaging and distribution and that
[2326.70 → 2327.08] sort of thing.
[2327.14 → 2331.90] I know a lot of people are talking about like these model hubs now and like, you know,
[2331.98 → 2335.60] TensorFlow Hub, PyTorch Hub, Hugging Faces Model Hub.
[2335.60 → 2339.86] You know, in addition to the code, there's sort of like there's the data, there's the
[2339.86 → 2340.16] code.
[2340.28 → 2344.94] And then there's these like these things that are kind of weird and maybe in the software
[2344.94 → 2349.32] engineering world that are like these different types of data, which are the serialized models
[2349.32 → 2352.02] and influence how this code runs.
[2352.34 → 2354.12] How do you think about that at Anaconda?
[2354.26 → 2359.18] And has that, you know, conversation been going on about, you know, packaging and distributing
[2359.18 → 2359.88] these things?
[2359.88 → 2362.84] Or are you mostly focused on the code at this point?
[2362.84 → 2366.34] We're still focused on the software supply chain, but of course, I'm very exposed to
[2366.34 → 2368.34] the kinds of dynamics you're talking about, right?
[2368.36 → 2373.08] Because I see these conversations happening in the practitioner ecosystem and in the conversations.
[2373.60 → 2379.10] There's a really important dynamic that's happening here that without getting too like
[2379.10 → 2384.88] hyperbolic and biblical about it, that data science, and we'll call AI or machine learning,
[2385.06 → 2388.44] this represents essentially the transformation of the software industry.
[2388.44 → 2393.94] So for the last probably 40 years, since the dawn of like the PC era, but even prior to
[2393.94 → 2398.98] that, even a little bit, software developers and software engineers have been able to think
[2398.98 → 2400.74] of themselves as a distinguished class.
[2400.86 → 2402.00] Like we do software.
[2402.26 → 2405.80] The harder people, they're writing Verilog and taping things out, whatever that means
[2405.80 → 2406.56] and making chips.
[2406.64 → 2407.68] They plug it in, power it on.
[2408.02 → 2410.14] Now, then we come in and we do our jobs, right?
[2410.44 → 2414.10] And then, of course, that's separate from the DBA's for this other weird class of like Oracle
[2414.10 → 2415.38] licensed whoever's, right?
[2415.42 → 2417.54] They just sit there speaking a bunch of weird SQL all day long.
[2417.54 → 2425.80] So this deconstruction of the information system into hardware, software and data management
[2425.80 → 2428.30] is deeply unnatural.
[2428.98 → 2431.04] And it's actually something that was not the case.
[2431.08 → 2434.60] If you go back to the Robber Wiener and to like the early cybernetics era, no one thought
[2434.60 → 2435.62] about it that way, right?
[2435.70 → 2439.68] You listen to any of these like the founding fathers and mothers of the space.
[2440.06 → 2442.34] It wasn't like, oh yeah, well, I'm going to focus on hardware, right?
[2442.66 → 2446.50] But the PC era and then everything that came afterwards and the server side on microprocessors,
[2446.50 → 2452.04] all these things led to this deconstruction of an information system into these three
[2452.04 → 2452.90] primary axes.
[2453.36 → 2455.52] Yeah, I guess it's a decomposition into three axes.
[2456.12 → 2461.90] And what we're seeing again now with data science and certainly with ML and AI is that
[2461.90 → 2463.72] we now have a synthesis again.
[2463.82 → 2464.90] We're forced to do a synthesis.
[2465.34 → 2466.72] We have to understand the runtime.
[2467.30 → 2471.64] And actually, the runtime characteristics of your software is data dependent, right?
[2471.74 → 2473.10] That's how weird is that?
[2473.10 → 2476.78] Can you imagine talking to Java head 15 years ago to say, well, okay, Mr. Java architect,
[2476.96 → 2477.44] check this out.
[2477.48 → 2482.14] If I pass in certain values out of this database, your code runs 10 times slower, right?
[2482.44 → 2484.68] That doesn't happen because you write a CRUD system.
[2484.78 → 2487.80] It pulls a row, does some crap and pushes a row, and it's done, right?
[2487.96 → 2490.68] So this idea that, okay, runtime performance.
[2491.06 → 2492.90] So the hardware footprint is dependent on data.
[2493.44 → 2496.18] And additionally, correctness is value dependent.
[2496.68 → 2498.18] Can you imagine writing a unit test?
[2498.28 → 2499.58] And you know, we have these for models.
[2499.64 → 2500.48] We have model tests, right?
[2500.48 → 2502.94] Prior to models, it was all just code.
[2503.00 → 2506.26] Can you imagine a unit test where it's like, well, one plus one is two.
[2506.80 → 2511.34] And so this function, my add function works, but it only works for even integers, right?
[2511.48 → 2512.86] Like that's weird, right?
[2512.90 → 2518.10] And yet we know that when we build these AI systems, these models, their performance,
[2518.22 → 2521.34] their correctness is actually value dependent.
[2521.80 → 2526.60] And this is a point that no, I don't hear anyone else making, maybe because I come at it
[2526.60 → 2527.54] from a physicist perspective.
[2527.54 → 2531.88] And I think about deconstructing everything to fundamentals, but deconstructing the computation
[2531.88 → 2533.64] concept into fundamentals.
[2534.00 → 2538.04] For the last 40 years, we've had value independent processing, right?
[2538.10 → 2541.54] And Jim Gray's written papers about this and people have talked about this, but like your
[2541.54 → 2543.62] average coder nerd doesn't think about this at all.
[2543.72 → 2544.76] They're like, I'm a software dev.
[2544.86 → 2545.64] I learned this thing.
[2545.70 → 2546.60] I'm going to learn go this year.
[2546.64 → 2547.60] I'm going to do something else next year.
[2548.00 → 2550.26] But the whole field of software is going away.
[2550.34 → 2552.92] It's melding into, we might call it model development.
[2553.00 → 2556.66] We might call it something else, but I call it value dependent or value sensitive computing.
[2556.66 → 2562.10] And now your management of your upstream data is as important as managing the upstream code,
[2562.18 → 2562.84] right?
[2562.88 → 2566.04] So the previous approaches to data management don't work anymore.
[2566.04 → 2569.76] But of course, checking in every row of a database into Git doesn't work either.
[2570.12 → 2574.08] So we have to develop an entire new set of practices for this new industry.
[2574.80 → 2579.52] All the previous components, those axes are important, but they can no longer be seen
[2579.52 → 2580.78] as separable, right?
[2580.82 → 2581.62] They're now integrated.
[2581.62 → 2584.54] So anyway, that's my welcome.
[2584.70 → 2587.06] Thank you for coming to my TED talk about that.
[2587.46 → 2590.18] But I think that really, that's the lens I look at all this stuff through.
[2590.50 → 2594.14] So it's no wonder that we have model hubs emerging, but I think the management of those
[2594.14 → 2597.90] things and how we talk about versioning of data, the model performance and characterizing
[2597.90 → 2600.00] it, all of that is in a nascent and emerging area.
[2600.06 → 2603.82] That'd be fascinating to watch how that really goes as it meets production in the real world.
[2603.82 → 2605.82] Okay.
[2627.46 → 2633.44] So a few minutes ago, we were touching on deployment and I know Daniel made his DevOps.
[2633.44 → 2635.88] DevOps Doug illusion there.
[2636.08 → 2637.74] And so I actually want to go back to that for a moment.
[2638.18 → 2638.44] Someday.
[2638.58 → 2640.68] I really hope DevOps Doug listens to this.
[2640.86 → 2641.76] He's going to get hate mail.
[2641.82 → 2646.68] So you know, Peter, Doug was my first like DevOps engineer that I work with when I first
[2646.68 → 2650.12] started out at a startup and, you know, he taught me all sorts of great things.
[2650.24 → 2651.10] Anyway, go ahead.
[2651.26 → 2651.58] Yeah.
[2651.64 → 2655.94] We're going to get our first practical AI hate mail, you know, from every Doug.
[2655.94 → 2657.68] I should contact him and have him on the show.
[2658.16 → 2658.44] Okay.
[2658.58 → 2659.54] So here's my question.
[2659.54 → 2659.90] Uh huh.
[2660.02 → 2665.04] I'm thinking about Anaconda kind of again in the organizational structure and thinking
[2665.04 → 2668.14] about, you know, having to put software together and move on to deployment.
[2668.32 → 2672.68] And, you know, one of the things that we're seeing a lot now is using Python in doing the
[2672.68 → 2674.70] data science and doing the modelling and stuff.
[2674.70 → 2679.46] But we're seeing a kind of move toward deploying in other languages, you know, where you may
[2679.46 → 2681.02] take a model and do that.
[2681.06 → 2684.88] And I'm kind of wondering what your thoughts are on how are you thinking like in a world
[2684.88 → 2690.28] where someone may for performance reasons, uh, maybe once upon a time or maybe still now
[2690.28 → 2695.94] they were deploying in Java or C++, but maybe they're thinking of Go or Rust just for pure
[2695.94 → 2696.86] performance issues.
[2697.08 → 2701.02] How do you see it fitting into that in terms of a pipeline?
[2701.28 → 2702.88] Do you think that's not necessary?
[2703.32 → 2704.12] What are your opinions?
[2704.12 → 2704.60] Wow.
[2704.80 → 2705.84] Yeah, that is a complex topic.
[2706.32 → 2710.48] So depending on which framework you're using and what you're doing with that, compiling
[2710.48 → 2714.48] down is always something that's going to be a part of the Python ecosystem, right?
[2714.52 → 2717.66] I mean, Daniel mentioned Numb before, like you don't have to convince me about compile
[2717.66 → 2718.12] down, right?
[2718.14 → 2719.60] There are times when you just need to go lower.
[2720.14 → 2720.26] Right.
[2720.62 → 2725.14] What pains me though is this idea that there are things that, because Numb goes not down
[2725.14 → 2726.50] to C, it goes to machine code.
[2726.60 → 2729.14] Like we literally are generating, we're skipping a level.
[2729.26 → 2731.08] We're going from Python to machine code, right?
[2731.08 → 2735.52] So in other places, I think in case like TensorFlow and there are tools like TAX, there's a whole
[2735.52 → 2740.30] bunch of stuff coming out now where you can go from high level Python to much lower level
[2740.30 → 2741.20] runtime primitives.
[2741.56 → 2742.28] And I think that's fine.
[2742.28 → 2747.48] And I think when people are doing rewriting, so compile down is something different from
[2747.48 → 2750.02] a translational perspective than rewriting, right?
[2750.04 → 2752.92] And I know that for instance, when people just the other day, someone was complaining
[2752.92 → 2756.50] to me about the fact that they build some models in Torch, and then they have to basically
[2756.50 → 2759.32] to go to TensorFlow serving, they have to rewrite everything in TensorFlow.
[2760.26 → 2761.64] That's deeply inefficient.
[2761.88 → 2763.20] It shouldn't have to be done that way.
[2763.42 → 2767.76] And so I think that the and the problems to solve there are not monumental.
[2767.76 → 2771.82] I think, I think they're mostly ecosystem tooling and some of these kinds of top things that
[2771.82 → 2773.04] we will solve in time.
[2773.28 → 2777.28] So I hope that Python compiling down is not an issue, and we'll keep doing that.
[2777.50 → 2782.26] Where people do feel a need to rewrite, I'm not sure what all they're doing in the Python.
[2782.50 → 2785.42] I think one of the problems with the Python's explosive growth over the last however many
[2785.42 → 2791.26] years is that there's simply not been enough instruction about idiomatic, how to think vectorially,
[2791.40 → 2795.58] how to do idiomatic things in Python or do things in Python in an idiomatic way that's
[2795.58 → 2796.00] faster.
[2796.00 → 2798.38] I mean, I just see all sorts of code in the wild.
[2798.50 → 2802.28] That's just like, oh, you know, that's, you don't have to do it that way, but you don't
[2802.28 → 2805.38] have time to educate everyone, but maybe we should, right?
[2805.38 → 2809.44] Because then what happens is you end up in organizations, businesses move at their own
[2809.44 → 2809.80] cadence.
[2810.00 → 2812.28] And now you've got a data science team that's all relatively green.
[2812.48 → 2813.40] They write some code.
[2813.46 → 2814.02] It's slow.
[2814.54 → 2817.42] The IT person, the IT team, the software dev team is like, well, that's Python.
[2817.52 → 2818.16] We know it's slow.
[2818.50 → 2821.76] Let us rewrite it in Go because I kind of like really, really like to use Go.
[2822.08 → 2824.56] And they do it, and they don't have to.
[2824.56 → 2826.10] And here's the cost of doing that.
[2826.48 → 2829.86] Now your iteration, your cycle time is way slower, right?
[2829.90 → 2832.86] Now when something goes wrong in production, you need to get two people on the line.
[2832.98 → 2835.16] And then where did the translation go wrong, right?
[2835.50 → 2840.14] For me, I think I still back to that point about what is the mission?
[2840.14 → 2846.10] The mission is to make data science literacy widespread and to empower everyone to ask
[2846.10 → 2849.80] questions of their world and to be able to use all of this powerful infrastructure.
[2850.14 → 2854.62] If to do that, they have to go and hire a dev team to rewrite their stuff from Python into
[2854.62 → 2858.92] Go or Rust or God knows what, then we failed in that mission, right?
[2858.96 → 2863.08] So I do, I don't have a language bigotry of like, it must be Python everywhere all the
[2863.08 → 2863.42] time.
[2863.42 → 2867.74] But it's like, I would like to make sure that, you know, Brett Victor has this concept
[2867.74 → 2869.24] of immediate connection, right?
[2869.26 → 2872.60] I want the data scientists when they're in a Jupyter notebook or in a dev environment,
[2872.88 → 2876.34] when they're doing data exploration, I want them to be able to feel like they can round
[2876.34 → 2878.08] trip and that's on their own terms.
[2878.62 → 2879.96] That's a really important thing.
[2880.42 → 2884.18] So I think, I think hopefully in time we'll get, we'll make sure that remains a possibility
[2884.18 → 2885.22] for most cases.
[2885.98 → 2886.96] Great explanation, by the way.
[2887.04 → 2887.42] Thank you.
[2887.42 → 2893.34] And I think that kind of leads into something I wanted to ask that you kind of started talking
[2893.34 → 2899.02] about some of the pain points that still exist between, you know, maybe data scientists and
[2899.02 → 2903.98] engineers, or maybe the, the, this sort of gap in, in data literacy and these things.
[2903.98 → 2909.02] I was wondering as you, and I also know that Anaconda does, um, you know, a state of data
[2909.02 → 2909.80] science survey.
[2909.80 → 2913.60] And of course you deal with, um, all sorts of people throughout the industry.
[2913.60 → 2919.38] I was wondering if if you could talk a little bit about maybe certain things looking back
[2919.38 → 2926.14] from maybe 2012 till now that you see as really encouraging things in, in terms of data science
[2926.14 → 2927.50] tooling and where we've come.
[2927.58 → 2932.10] And then maybe a few things that are still really open challenges that we haven't been
[2932.10 → 2933.52] able to solve yet.
[2934.02 → 2935.30] You mean specifically in the tooling?
[2935.90 → 2936.30] Is that the question?
[2936.44 → 2940.08] Or, or just in data science workflows, I guess that you see.
[2940.34 → 2940.48] Yeah.
[2940.90 → 2941.10] Yeah.
[2941.10 → 2943.44] Let's see here in data science workflows.
[2943.44 → 2948.48] I think a lot of like some table stakes things since 2012 have been resolved.
[2948.72 → 2954.44] We have much more capable just in terms of like, you know, input handling and just like
[2954.44 → 2958.14] there's a lot of the basic day-to-day quality of life stuff for data scientists, I think
[2958.14 → 2958.84] has improved.
[2959.56 → 2965.72] People have settled on some sorts of tools as standard, and they're good.
[2965.78 → 2970.52] So like using Jupyter notebooks, which I know gets, there's a there's a mixed feeling about
[2970.52 → 2970.94] notebooks.
[2970.94 → 2971.24] Right.
[2971.60 → 2976.10] And I can go on a length about them, but I think in general, we had Joel Ruse on the
[2976.10 → 2976.26] show.
[2976.30 → 2976.72] Oh yeah.
[2976.80 → 2977.08] Yeah.
[2977.34 → 2978.72] We've had all perspectives.
[2979.02 → 2979.30] All perspectives.
[2979.62 → 2983.12] You know, I like to talk about threes and I think that the notebook rolls up three different
[2983.12 → 2983.82] things into one.
[2983.82 → 2987.60] And in doing so unfortunately confuses the crap out of everyone because everyone thinks
[2987.60 → 2988.70] it's something else, you know?
[2988.86 → 2989.20] Right.
[2989.28 → 2989.46] Right.
[2989.46 → 2994.28] But basically I think that at least with notebooks, the idea that people can do somewhat literate
[2994.28 → 2999.10] programming is way better than it was a bunch of opaque code and then a PowerPoint.
[2999.88 → 3000.18] Right.
[3000.30 → 3004.18] So for all the hate and all the like, oh, line numbers out of sequence and like this,
[3004.36 → 3005.88] like, I don't know, you just gave me a notebook.
[3005.96 → 3006.68] I don't know what to do with it.
[3006.68 → 3011.48] For all of that hate aside, I think notebooks are a net good because they show people ultimately
[3011.48 → 3015.02] again, back to that data literacy thing, it gets people excited and interested.
[3015.24 → 3016.46] And here, here's another thing about Python.
[3016.46 → 3019.74] It's good that it's Python that has, that is in these notebooks.
[3020.48 → 3023.62] Python is very accessible and readable, even if you don't know how to write it.
[3023.82 → 3027.46] So if you're a business analyst who only does Excel and someone gives you a notebook with
[3027.46 → 3030.90] a little bit of Python code, you can actually still inspect that Python code and say, hey,
[3031.00 → 3034.64] it looks like you're pulling last quarter's data instead of this quarter's data in this
[3034.64 → 3038.86] particular thing where you sliced it here, but you zeroed out all of this zip code.
[3038.92 → 3039.54] Why did you do that?
[3040.46 → 3046.32] That bit of accessibility and communication, collaboration, collaboration kind of vernacular,
[3046.46 → 3048.86] power should not be underestimated.
[3048.94 → 3050.32] Imagine it was a pile of JavaScript.
[3050.70 → 3053.92] How many nested braces and functional embedded callbacks and some other crap.
[3054.42 → 3057.92] I mean, your, your business analyst has no hope of understanding what the heck you're
[3057.92 → 3058.26] doing, right?
[3058.54 → 3061.56] They don't know these 20 lines are just to try to strip out some ending semicolons.
[3061.70 → 3063.24] No, I, I totally agree.
[3063.36 → 3063.54] Yeah.
[3063.66 → 3067.86] There's actually, I've mentioned it a couple of times on the show, this group called Malakand,
[3067.86 → 3072.08] who is promoting new baselines for machine translation for African languages.
[3072.08 → 3074.34] And they're involving local communities in that.
[3074.50 → 3078.44] And they have a whole paper about this, how they like to develop the community and all of
[3078.44 → 3078.54] that.
[3078.54 → 3083.78] But a really central, a central piece of that was Jupyter Notebooks because they wanted
[3083.78 → 3086.54] to involve, you know, local communities in the work.
[3086.54 → 3090.64] And of course, like you say, it's not like you're just going to go up to a new group
[3090.64 → 3095.00] of people and say, Hey, you know, clone this GitHub repo and like, you know, run this bash
[3095.00 → 3096.88] script and like all this stuff.
[3097.02 → 3101.72] And so they were able to, you know, utilize Notebooks and specifically like hosted Notebooks
[3101.72 → 3106.56] or like Cola and, and all of these things to really like to get people going and like,
[3106.80 → 3107.74] Hey, you just opened the notebook.
[3107.74 → 3109.36] There's like notes in there.
[3109.50 → 3111.52] There's explanation, and you can just like go.
[3111.52 → 3116.66] And of course, you know, you want people to, to advance from there and to, you know,
[3116.72 → 3120.78] really dig into things when things are, you know, there's weird behaviour or something.
[3120.96 → 3125.02] Maybe you kind of learn some new things, but yeah, I was really impressed with their usage
[3125.02 → 3125.40] of that.
[3125.44 → 3127.32] And I think that resonates with, with what you're saying.
[3127.48 → 3129.64] Well, it's the web has become unwritable, right?
[3129.64 → 3130.60] Let's just be very clear.
[3130.74 → 3133.48] Like, I don't know the last time you guys set up a website from scratch.
[3133.54 → 3136.50] I mean, you have a website for the podcast, obviously maybe you had a web dev for it.
[3136.50 → 3141.42] I don't know, but to set up a website from scratch, forget putting widgets in
[3141.42 → 3145.40] there, forget embedding, you know, interactive graphics, just a website from scratch.
[3145.68 → 3147.40] Most data scientists won't be able to do that.
[3147.52 → 3147.94] That's true.
[3148.04 → 3152.94] I mean, just configuring Nginx or setting up Apache, you know, getting SSL cert in there,
[3153.24 → 3156.38] doing all this other, you know, happy, like whatever, like that's impossible.
[3156.38 → 3156.70] Right.
[3156.74 → 3159.40] And even for a dev like myself, it's really just annoying.
[3160.12 → 3165.10] So what the Jupyter Notebook did, believe it or not, a lot of the value is simply making
[3165.10 → 3171.12] the web writeable, making a writeable web technology accessible for people who were not even programmers,
[3171.12 → 3172.82] who are not familiar or comfortable with the shell.
[3172.90 → 3174.40] That's the other thing that's true about data scientists.
[3174.48 → 3176.04] A lot of them are not comfortable with the terminal at all.
[3176.50 → 3176.68] Right.
[3177.04 → 3178.06] A lot of them are on Windows.
[3178.34 → 3182.74] And now they can build websites on Windows with interactive widgets running massive scale
[3182.74 → 3183.28] computation.
[3184.18 → 3184.74] Holy crap.
[3184.82 → 3188.20] Let's like, you know, complain about the Jupyter Notebook at that point.
[3188.26 → 3191.46] It's like complaining about, I don't know, the cupholders in the Starship Enterprise or
[3191.46 → 3191.64] something.
[3191.72 → 3192.68] It's like, stop it.
[3192.70 → 3193.82] You're moving at warp nine.
[3194.16 → 3194.90] Just shut up.
[3194.90 → 3195.10] Right.
[3195.50 → 3200.50] So I think that's the thing that devs like myself who have a dev background, we look at
[3200.50 → 3203.12] the space of technology, and it's a relatively flat landscape.
[3203.38 → 3204.62] Yeah, I can go learn this language.
[3204.72 → 3205.38] I can do that thing.
[3205.44 → 3207.72] I can go grab a search, spin up that AWS credential.
[3208.14 → 3208.64] No problem.
[3209.08 → 3212.70] For the average person, every single one of these things is a cliff that's insurmountable.
[3213.14 → 3214.96] And this is kind of to the point of Anaconda as well.
[3215.10 → 3215.22] Right.
[3215.72 → 3219.48] Advanced users, actually, a lot of advanced users do use Minions as their deployment technology,
[3219.48 → 3220.82] like I said, within Dockers and whatnot.
[3220.82 → 3224.34] But there's also others who are like, well, I can do my own thing.
[3224.42 → 3226.14] I don't really want to use this big package manager thing.
[3226.54 → 3228.66] But there's so many people out there learning how to do this stuff.
[3229.10 → 3229.60] They're on Windows.
[3229.72 → 3231.40] They have no idea what a compiler is.
[3231.62 → 3233.88] They just want to do their jobs for their police homework.
[3234.50 → 3239.68] And so that is where accessibility, again, kind of building on the Python motif of being
[3239.68 → 3242.64] accessible as a language, want the tooling around this to be accessible.
[3242.82 → 3246.34] And this is now, to answer the second part of your question, where have we fallen short?
[3246.34 → 3252.56] I think that as the technical space of data science and machine learning has grown up,
[3252.62 → 3256.94] put on a suit, got a real job, we've got software developers coming in saying, hey,
[3256.96 → 3258.16] I'm going to retool as an ML engineer.
[3258.32 → 3259.10] I can learn the stats.
[3259.22 → 3259.66] And they can.
[3259.74 → 3260.38] They're smart people.
[3260.88 → 3261.66] They can do all these things.
[3262.00 → 3265.92] Part of what's being lost nowadays that I see in the more modern tooling is there's
[3265.92 → 3268.02] kind of taste is lost.
[3268.10 → 3271.70] And the taste of making this accessible for people who are not ops geeks.
[3272.00 → 3273.66] I think some of that drive has gone away.
[3273.66 → 3277.76] So when I go and look at the documentation for any kind of ML framework, and this is
[3277.76 → 3278.64] not to put a ding on them.
[3278.70 → 3280.68] I mean, this is you're doing complex orchestration.
[3280.90 → 3282.00] There's going to be some work involved.
[3282.66 → 3286.50] But just in general, that sense of like, how do we make this dirt simple for that poor
[3286.50 → 3289.72] atmospheric scientist trying to model hurricanes, trying to understand climate change?
[3289.80 → 3292.90] How do we make it simple for these guys trying to build better translation, machine
[3292.90 → 3294.08] translation for African languages?
[3294.20 → 3297.22] And they're out in an African village trying to get the locals involved.
[3297.60 → 3299.40] How do we make stuff really easy to use for them?
[3299.40 → 3305.48] That kind of thing is, I think, being crowded out a little bit, right?
[3305.56 → 3307.66] That kind of sensibility and taste is gone, I think.
[3308.04 → 3309.02] And it's unfortunate.
[3309.58 → 3314.94] There's also a willingness to embrace a huge corporate open source, which is not, again,
[3315.02 → 3317.34] I salute the companies for open sourcing their technologies.
[3317.80 → 3324.18] But I think the open source ecosystem around SciPy and whatnot never really had some of the
[3324.18 → 3328.34] corporate open source like hegemony kind of thing happen to them that happened in the
[3328.34 → 3328.90] Linux space.
[3329.28 → 3330.64] So they've never seen weaponized open source.
[3331.02 → 3333.76] And I'm one of the few people trying to go in there and raise the banner and be like,
[3333.80 → 3338.96] hey, guys, recognize there's community grassroots kind of open source community
[3338.96 → 3339.36] innovation.
[3339.76 → 3343.88] And there's a big company saying, here's our big old toolkit, a million man-hours.
[3344.26 → 3344.92] And it's all yours.
[3345.00 → 3345.52] Use it, please.
[3345.64 → 3347.10] And by the way, it runs best in our cloud framework.
[3347.60 → 3350.56] Like that's, you know, I don't know how I feel about that exactly.
[3350.92 → 3352.20] It's more than a license, right?
[3352.26 → 3353.38] It's more than the license.
[3353.48 → 3355.16] It's about community innovation and open standards.
[3355.34 → 3355.82] Yes, absolutely.
[3355.82 → 3360.42] So as we finish up, I just kind of wanted to get your sense of what does the future of
[3360.42 → 3361.50] Anaconda look like?
[3362.10 → 3364.76] What's in your mind that you'd like to do that you haven't gotten to yet?
[3365.34 → 3368.84] What should your users be looking forward to at this point?
[3368.96 → 3369.20] Yeah.
[3369.34 → 3369.70] So that's great.
[3369.76 → 3370.06] Thank you.
[3370.12 → 3370.50] Great question.
[3371.04 → 3374.20] So we've been working a lot of infrastructure technologies for the last several years trying
[3374.20 → 3379.44] to help get the commercial adoption of data science and open data science successful,
[3379.60 → 3379.72] right?
[3379.72 → 3381.64] Which is why we sell like a package server, things like that.
[3381.64 → 3385.98] We don't want IT raising exceptions saying you cannot use, thou shall not use Python because
[3385.98 → 3387.40] we're a Java shop, right?
[3387.44 → 3389.52] I wanted to put that argument to rest.
[3389.66 → 3393.16] So I think we've been pretty successful with some of the things we've done to help smooth
[3393.16 → 3393.64] those things out.
[3394.60 → 3398.66] Going forward, though, I want us to kind of lean more into the practitioner community,
[3399.06 → 3404.04] help the community and thought leaders and practitioners, diverse voices, right?
[3404.06 → 3409.56] Across culture, across background and whatnot to surface organically in the community and
[3409.56 → 3415.40] really drive a conversation about the practice of data science and quantifying our world,
[3415.76 → 3420.30] modelling our world, predicting our world, but doing it in an open way, in an ethical way
[3420.30 → 3422.74] and in an intentional way.
[3422.88 → 3425.84] I don't want us to do, I don't want data science to end up where social media has, where it's
[3425.84 → 3427.36] like, oh, we accidentally destroyed democracy.
[3427.50 → 3427.74] Crap.
[3428.16 → 3432.32] You know, like you want data science and predictive analytics to be sort of like, hey, we know
[3432.32 → 3434.70] exactly, well, we know we're going into it eyes wide open.
[3434.70 → 3439.98] So I want to create a community, community tools, so tools for ethical practice of data
[3439.98 → 3446.08] science, as well as then facilities, site, you know, some of the next generation capabilities
[3446.08 → 3447.52] that our practitioner are facing.
[3447.98 → 3449.84] So we're going to be, you know, look forward to a lot more of that.
[3449.90 → 3451.66] We're going to try to engage with the user community a lot more.
[3452.64 → 3455.66] We'll be revving our product offerings there, as well as some of the things that will be
[3455.66 → 3457.80] standing up on the website itself, on the Anaconda Cloud.
[3458.08 → 3459.80] So we're really excited about those kinds of things.
[3460.22 → 3461.36] It's beyond tools at this point.
[3461.40 → 3461.94] It's about people.
[3461.94 → 3465.22] It's always been about people, but now the emphasis is kind of coming back around to
[3465.22 → 3466.58] being about the practitioners in the community.
[3467.82 → 3468.62] Well, thank you so much.
[3468.68 → 3469.92] I think that's a great way to end.
[3470.02 → 3472.98] We'll, of course, link to a bunch of Anaconda things in the show notes.
[3473.12 → 3474.56] So make sure and check those out.
[3475.00 → 3477.24] Connect with us on Slack and LinkedIn and Twitter.
[3477.36 → 3481.96] Let us know how much you appreciate Condo over the years and, you know, what they're doing.
[3482.22 → 3483.98] Thank you so much, Peter, for joining us.
[3484.22 → 3484.86] It's been a pleasure.
[3485.02 → 3485.36] Thanks, Daniel.
[3485.42 → 3485.80] Thanks, Chris.
[3485.86 → 3486.54] This has been a lot of fun.
[3486.62 → 3487.46] Thanks for listening to my rants.
[3488.20 → 3488.78] It was fun.
[3488.92 → 3489.18] Thanks.
[3489.30 → 3489.62] Thank you.
[3491.94 → 3497.98] Don't forget we have a giveaway going on in celebration of episode 100.
[3499.10 → 3503.34] Enter for your chance to win some awesome AI hardware from NVIDIA, Intel, and Google,
[3503.54 → 3505.80] plus practical AI and Pachyderm swag.
[3506.10 → 3508.40] We're giving away three bundles, so you have a good shot at them.
[3508.90 → 3512.48] Check your show notes for details on entry you have until the end of the month.
[3512.48 → 3517.16] Speaking of Pachyderm, a little birdie told me they have a big announcement coming soon,
[3517.32 → 3519.48] and you should join their Slack channel to stay tuned.
[3519.98 → 3522.18] Learn more about that at Pachyderm.com.
[3522.86 → 3525.60] Thanks to our longtime sponsors for their continued support.
[3525.94 → 3530.52] Shout out to Vastly, Linde, and Rollbar, and to the mysterious Brake master Cylinder for
[3530.52 → 3531.48] these awesome beats.
[3531.98 → 3532.96] That's all for now.
[3533.16 → 3534.50] We'll talk to you again next week.
[3534.50 → 3564.48] We'll see you then.
