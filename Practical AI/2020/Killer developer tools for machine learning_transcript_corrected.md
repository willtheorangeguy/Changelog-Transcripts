[0.00 → 3.02] I feel like with deep learning, your runs often take days, right?
[3.04 → 5.56] So you want to get a sense for if they're working right away
[5.56 → 8.38] and you want to really have a good record of everything that happened,
[8.58 → 10.98] you know, from like system metrics to like exactly
[10.98 → 14.12] what was the last commit that went into your code to,
[14.32 → 16.70] and you know, everyone has these like notebooks, you know,
[16.76 → 19.70] like in their Emacs or VS Code or like maybe a Google Doc
[19.70 → 22.42] if you're really advanced, you know, where they're just kind of typing like,
[22.52 → 24.80] okay, here's all the things I did, you know, and here's what happened.
[24.80 → 27.66] Or in file names, extra long file names.
[28.20 → 28.70] Yeah, yeah.
[28.70 → 31.54] That's a perfect point as well is the fact that as you move
[31.54 → 33.74] through the different phases of your workflow,
[34.02 → 36.72] and you know, you're kind of, you know, doing research in a notebook
[36.72 → 39.26] and then you need to deploy it as a software component and stuff,
[39.60 → 43.66] there is still friction in the process in terms of moving through
[43.66 → 46.84] each of those very distinct phases of trying to get your workflow
[46.84 → 49.28] from the very, very beginning to the very, very end and deployed.
[49.46 → 52.86] And I think people still, everyone kind of customizes that quite a lot.
[52.86 → 55.44] There's another opportunity out there for someone.
[55.44 → 59.58] Bandwidth for Changelog is provided by Vastly.
[59.90 → 61.84] Learn more at Fastly.com.
[62.06 → 65.16] We move fast and fix things here at Changelog because of Rollbar.
[65.28 → 66.96] Check them out at Rollbar.com.
[67.18 → 69.40] And we're hosted on Linde cloud servers.
[69.74 → 71.74] Head to linode.com slash Changelog.
[71.74 → 74.64] This episode is brought to you by DigitalOcean.
[75.20 → 75.76] Droplets.
[76.00 → 76.76] Managed Kubernetes.
[77.12 → 77.98] Managed databases.
[78.50 → 79.10] Spaces.
[79.34 → 80.22] Object storage.
[80.50 → 81.74] Volume block storage.
[82.00 → 85.48] Advanced networking like virtual private clouds and cloud firewalls.
[85.70 → 88.92] Developer tooling like the robust API and CLI
[88.92 → 91.94] to make sure you can interact with your infrastructure the way you want to.
[92.34 → 95.86] DigitalOcean is designed for developers and built for businesses.
[95.86 → 102.98] Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[103.26 → 106.70] Head to do.co slash Changelog to get started with a $100 credit.
[107.04 → 109.18] Again, do.co slash Changelog.
[109.18 → 133.56] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[133.90 → 135.64] productive, and accessible to everyone.
[135.64 → 140.06] This is where conversations around AI, machine learning, and data science happen.
[140.48 → 144.52] Join the community and Slack with us around various topics of the show at ChangeLog.com
[144.52 → 146.40] slash community and follow us on Twitter.
[146.56 → 148.18] We're at Practical AI FM.
[154.46 → 157.72] Well, welcome to another episode of Practical AI.
[158.10 → 159.74] This is Daniel Whiten ack.
[159.84 → 162.70] I'm a data scientist with SIL International.
[162.70 → 170.16] And I'm joined, as always, by my co-host, Chris Benson, who is a principal emerging technology
[170.16 → 172.42] strategist at Lockheed Martin.
[172.74 → 175.42] Every time, Chris, I've got to get those words in the right order.
[175.90 → 177.44] It's an impressive title, I have to say.
[177.44 → 178.62] It's a terrible title.
[178.80 → 179.80] It's a mouthful.
[180.24 → 181.86] So, yeah, it's funny.
[181.98 → 182.94] I'll go ahead and make fun of him.
[183.06 → 184.18] I'm hoping he doesn't listen to this.
[184.32 → 188.20] My boss will be introducing me in a meeting, and he can't even say it.
[188.20 → 191.70] And it just makes, you know, I'm like, no one's like, who's this guy that joined us?
[191.82 → 191.92] Yeah.
[192.04 → 192.58] So, yeah.
[192.66 → 197.40] I mean, you could do an acronym that's like pet strategist.
[197.46 → 201.12] That sounds also very animal friendly, you know, PET.
[201.48 → 202.32] That's very applicable.
[202.52 → 202.68] Yeah.
[202.78 → 204.02] Principal emerging technologies.
[204.26 → 204.44] Yeah.
[204.98 → 205.38] Exactly.
[205.72 → 208.30] I love animals for anyone that, yeah.
[208.44 → 211.14] So anyone who's listened for a while has heard me carry on about it.
[211.34 → 212.94] So how are things going for you, Chris?
[212.94 → 217.70] You're excited about a crazy week in the U.S. at least?
[218.08 → 218.32] Yeah.
[218.54 → 221.74] So as we record this, it's the day before election day.
[221.98 → 226.44] So, you know, I guess everyone is holding their breath no matter what side of the aisle
[226.44 → 226.96] you're on.
[227.14 → 232.26] And we'll see what happens through the rest of the week and maybe beyond, depending on
[232.26 → 232.88] how things go.
[233.14 → 238.36] I'm remembering the election of 2000 and, you know, it went on for months to get a resolution.
[238.54 → 239.00] So we'll see.
[239.08 → 239.68] It'll be interesting.
[240.06 → 240.40] We'll see.
[240.64 → 240.84] Yep.
[240.84 → 249.22] Well, we decided that at least, you know, on my end, I wanted a break from anything political
[249.22 → 254.44] and a little bit of a chance to be practical as we are here at Practical AI.
[254.76 → 260.74] So this week we've asked Lucas Piebald, whose founder and CEO at Weights and Biases, to join
[260.74 → 265.30] us and talk about a lot of the things that they're doing in terms of developer tools for
[265.30 → 267.20] ML and maybe some other stuff.
[267.38 → 268.20] So welcome, Lucas.
[268.26 → 269.34] It's great to have you with us.
[269.80 → 270.28] Thanks so much.
[270.28 → 271.08] Great to be here.
[271.46 → 271.70] Yeah.
[272.10 → 278.04] Could we maybe start by just having you give us a little bit of information about your background
[278.04 → 283.58] and how you got interested in AI and computing and ended up where you're at now?
[283.90 → 284.46] Yeah, totally.
[284.66 → 286.88] I mean, I was always interested in AI.
[287.00 → 292.00] I mean, ever since I was a little kid writing software to play video games against me.
[292.00 → 298.50] And then, you know, I wanted to go into academia and study AI and machine learning.
[298.76 → 302.02] And I got as far as a master's degree and did some research.
[302.38 → 306.04] And then I left to do more practical AI.
[306.04 → 309.40] So I love the title of this podcast.
[309.40 → 309.42] Yeah, it's good.
[309.42 → 313.42] I mean, this is like back in 2003, 2004.
[313.80 → 317.38] And it was super fun because it was like, you know, the really early days of ML systems
[317.38 → 323.42] and deploying, you know, big ML stuff in production for Yahoo back when that was a super relevant
[323.42 → 323.98] company.
[323.98 → 325.94] And then at some startups.
[326.16 → 330.96] And then, you know, I got really interested in data labelling, which, you know, you'll probably
[330.96 → 335.64] understand just because it felt like actually in research and in industry, it felt like the
[335.64 → 340.80] quality of the data labelling completely determined, you know, the quality of the ML systems to play.
[340.98 → 342.30] Oftentimes still does.
[343.00 → 343.72] Yeah, totally.
[344.58 → 349.68] And so I started a company originally called Crowd flower that was changed the name to figure
[349.68 → 349.96] eight.
[349.96 → 355.18] We were really maybe the first data labelling company for ML practitioners.
[355.72 → 355.82] Yep.
[355.98 → 358.62] And I ran that for about 10 years.
[358.86 → 363.80] It sold to a company called Happen, which is a big Australian public company that also does
[363.80 → 364.28] data labelling.
[365.22 → 369.52] And then in that process, I saw kind of deep learning take off.
[369.62 → 374.64] And I saw, you know, suddenly all these applications, these very awesome practical applications across
[374.64 → 375.40] tons of industries.
[375.40 → 379.72] Like when I was first coming out of school, it sort of felt like all the jobs available was,
[379.72 → 384.92] you know, ranking ads or ranking, you know, search terms and or, you know, going to go into Wall
[384.92 → 386.10] Street and being quant.
[386.36 → 391.54] And I mean, those aren't horrible jobs, but I feel like the really practical stuff is more exciting
[391.54 → 391.86] to me.
[391.90 → 396.58] And so, you know, it felt like there's just so many real world applications happening.
[397.00 → 400.56] And kind of what I saw was, you know, the tooling just seemed nascent.
[400.56 → 405.30] And it felt like a lot of the developer tools that we all take for granted don't quite translate
[405.30 → 409.62] into, you know, machine learning applications because it's inherently statistical and I
[409.62 → 410.32] go on and on why.
[410.44 → 412.26] But, you know, basically they don't seem to translate.
[412.62 → 416.78] And you know it because you see ML practitioners not using a lot of software best practices.
[417.62 → 423.10] And so me and my same co-founder from Figure 8 and actually a third co-founder, we decided
[423.10 → 427.70] to start a company that was just focused on making great tools for ML practitioners.
[427.70 → 428.14] Yeah.
[429.08 → 436.02] And we should say, too, so you mentioned the name of this podcast, but you've also hosted
[436.02 → 445.08] a podcast with a pretty great name, Gradient Descent, spelled D-I-S-S-E-N-T.
[445.64 → 448.44] So great work with the naming there.
[448.88 → 448.92] Excellent.
[450.38 → 450.98] Yeah.
[451.12 → 454.26] So definitely check out that podcast as well.
[454.34 → 456.06] We'll put the link in the show notes.
[456.06 → 462.14] Has it been interested in terms of, you know, after kind of being a practitioner, being a
[462.14 → 468.12] founder for a while, has it been interesting having conversations on your podcast with other
[468.12 → 468.70] practitioners?
[469.08 → 474.86] Have there been sort of viewpoints that have surprised you or insights that you've gained
[474.86 → 480.60] that maybe you didn't expect to as, you know, as you started having some conversations
[480.60 → 483.40] with people, you know, in various parts of the industry?
[483.40 → 488.52] You know, when you run a company, especially as a founder, a CEO, most of what you do is
[488.52 → 489.52] you talk to customers.
[489.64 → 491.12] It's a huge part of what you do.
[491.28 → 497.14] And so the podcast is really kind of just recording the conversations that I was having and giving
[497.14 → 501.84] me an excuse to kind of ask a little bit higher level questions to people.
[501.98 → 505.80] You know, we kind of get into the details really quick, you know, with the user.
[505.80 → 509.70] But we thought it would be fun to sort of step back a little bit and just have kind of open
[509.70 → 512.42] ended conversations, which you're kind of doing anyway, when we're starting Weights and
[512.42 → 517.68] Biases, because at first we weren't really sure what the first best tool would be to make.
[517.74 → 520.18] And so we had a lot of these, and they were so much fun.
[520.26 → 523.44] We kind of thought, you know, maybe we'll record these and other people find them useful
[523.44 → 524.60] because we were citing them a lot.
[524.98 → 527.62] But I mean, I would say it's been absolutely fascinating.
[527.62 → 531.52] And it's been really fun to step way back and ask questions because you hear surprising
[531.52 → 531.86] stuff.
[532.08 → 537.60] Like I'll say, you know, Anand ta Banker from Lyft was a longtime customer of Weights
[537.60 → 539.28] and Biases, and he's a great guy.
[539.86 → 542.80] But he was basically like, you know, ML is just the same as anything else.
[542.80 → 548.02] It's just a discipline of engineering, which I thought was a bold statement from a guy running
[548.02 → 550.06] the level five team there.
[550.42 → 555.86] Or I remember Jeremy Howard was like, basically, Python can't possibly be the future of machine
[555.86 → 559.18] learning, which is another kind of controversial topic.
[559.36 → 562.04] So, you know, it's funny you ask people, and usually they say the same stuff.
[562.12 → 565.16] But then every so often you get these gems, and you really think, huh, interesting.
[565.68 → 566.14] And dig in.
[566.52 → 567.06] Yeah, yeah.
[567.94 → 572.36] Statements that would provoke a lot of discussion at any conference.
[573.26 → 574.04] Yeah, yeah, exactly.
[574.22 → 574.74] Anything like that.
[574.86 → 578.76] It's like people just assume certain things like, oh, you're going to use Python.
[579.60 → 581.16] That's kind of what people do.
[581.16 → 586.04] But people really thinking about the foundations of those things and why we're using those things
[586.04 → 587.16] is fascinating.
[587.38 → 589.68] We've had those experiences here as well, for sure.
[590.78 → 595.40] So I'm actually wanted to take you back for a moment to your introductory bio a little bit
[595.40 → 598.56] and hit a particular point that you kind of went over there.
[598.68 → 604.78] And when you were talking about founding Figure 8, which used to be, I can't say it now, Crowd flower.
[604.92 → 605.36] I apologize.
[605.86 → 607.60] Which is really how I think of it.
[607.60 → 610.78] Because I've worked for several companies which have been your customers.
[611.20 → 612.54] Oh, fantastic.
[612.92 → 613.38] There you go.
[614.20 → 615.32] I'm just kind of curious.
[615.76 → 622.02] At that point in time, relatively early, certainly based on where we are with machine learning
[622.02 → 625.38] today and Figure 8 is a well-known name in this industry.
[625.78 → 627.74] And you have a lot of big customers and stuff.
[627.88 → 632.96] But going back to when you founded it, at that moment in time, what was it that made you say,
[633.06 → 634.44] this is the thing I'm going to go do?
[634.68 → 636.52] What was the problem that you saw?
[636.52 → 638.64] How did you want to solve it?
[639.12 → 643.72] If you can take yourself back to that year and tell us a little bit about what that moment
[643.72 → 644.16] was like.
[644.80 → 645.22] Yeah, totally.
[645.36 → 649.70] Well, I think it started in my master's program in grad school.
[649.84 → 653.84] And I was doing research on a thing called word sense disambiguation, where you try to
[653.84 → 658.28] figure out if plant means the power plant or the living plant, right?
[658.30 → 660.28] Kind of classic problem in NLP.
[660.28 → 666.04] And I spent all this time with a data set that's called WordNet is the ontology, but
[666.04 → 670.86] there's a data set of documents labelled with the meaning into WordNet.
[671.42 → 674.30] And it turns out word sense disambiguation is kind of tricky.
[674.30 → 678.16] It's a tricky thing to know really what the senses of a word should be.
[678.30 → 681.86] And I think my personal opinion is WordNet makes way too many senses.
[682.04 → 685.00] So they'll have like 15 meanings of plant.
[685.16 → 689.26] There's sort of two main ones, like I said, like plant, the living thing and the power plant.
[689.34 → 692.34] But they'll also have like plant a block into someone.
[692.48 → 694.88] Like in football, it's like its own meaning, which is questionable.
[694.88 → 696.38] And just all this kind of like-
[696.38 → 699.88] Yeah, like domain specific or like very niche.
[700.24 → 700.64] Metaphorical.
[700.80 → 705.56] I mean, it's almost like, it sounds so obvious, the senses of a word when you talk about those
[705.56 → 705.90] two.
[706.42 → 706.56] Yeah.
[707.02 → 710.26] But when you think about like planting a block or planting your foot into the ground,
[710.84 → 714.70] it actually gets a lot trickier of like what meaning is different from what.
[714.80 → 719.24] And you kind of only learn that once you spent a long time with that ontology.
[720.06 → 722.80] Anyway, what happened was I was finding all these patterns in the data set.
[722.80 → 724.56] And I was really excited to like to publish a paper.
[725.38 → 730.96] And then I realized that actually what I was doing is not finding interesting patterns.
[730.96 → 734.76] I was basically figuring out who the annotators were.
[735.52 → 738.94] So like, you know, I was doing this sort of like cross document classification.
[739.08 → 741.72] I was realizing if you could look at the classifications of one part of the document,
[741.88 → 744.12] it can help you the classifications of the other part of the document.
[744.36 → 746.46] And I thought what I was doing was topic detection.
[747.16 → 751.42] But then actually what I realized I was doing is I was basically doing annotator detection.
[752.02 → 752.14] Right.
[752.14 → 756.12] And it was so like heartbreaking because I had spent like months like, you know,
[756.12 → 757.94] doing this research, and it seemed like really promising.
[758.64 → 761.76] And then suddenly I realized that I was just finding this like artifact of the labelling.
[761.92 → 765.58] And like the labeler shouldn't really matter, you know, for like, you know, like documents.
[765.64 → 766.44] But of course it does.
[767.14 → 769.90] And then so that was really like top of mind.
[770.06 → 775.06] And then when I was working at Yahoo, I was actually switching their search engine from
[775.06 → 777.96] kind of rule based system to an ML system.
[777.96 → 780.04] And I was doing it in all these different languages.
[781.06 → 785.82] And it was funny because like each country that I'd go into, sometimes they'd be super
[785.82 → 788.88] happy with me, and sometimes they would be like really pissed off.
[789.44 → 792.34] And it had nothing to do with me because I was doing the same algorithm in each country.
[792.58 → 796.40] But it was totally based on how seriously they took the labelling process.
[796.90 → 797.02] Right.
[797.02 → 800.44] So like some countries, I mean, I guess now I could probably name names like, you know,
[800.46 → 803.86] he took like China was totally not taking the labelling process seriously.
[804.00 → 805.38] They're just trying to do it as fast as possible.
[805.70 → 806.92] They'd always like miss labelling.
[807.02 → 811.26] And so it was really hard to get a system out where like Japan was taking it very
[811.26 → 815.40] seriously because they had like they had a kind of for historical reasons.
[815.40 → 818.74] They just had a bunch of labels that really cared, and they were labelling it much more
[818.74 → 819.08] carefully.
[819.08 → 821.52] And so it was much easier to launch something there.
[821.68 → 826.20] And I was sitting there like, hey, I'm I'm this, you know, I'm the ML guy like, you know,
[826.50 → 829.58] I'm doing the same thing in each country, but you seem to have very different like takes
[829.58 → 829.86] on it.
[829.92 → 834.16] And so it just made it so obvious that the labels are kind of what matters.
[834.16 → 838.32] And so I sort of felt like if you want to make ML real, that's something I've always
[838.32 → 839.00] really cared about.
[839.04 → 842.80] Like, it's so exciting when you get something really deployed for a real application.
[843.64 → 847.68] If you want to do that, most of what you should spend your time on probably is the
[847.68 → 848.44] labelling process.
[848.44 → 853.74] I think at the time what was happening a lot was ML teams were kind of relying on some
[853.74 → 858.48] other function in the company that was already kind of doing a lot of data collection to do
[858.48 → 858.94] the labelling.
[859.72 → 863.42] And so the ML teams would be kind of divorced from the labelling process.
[864.02 → 866.82] And so I think what, you know, Crowd flare at the time then became figure eight.
[866.92 → 871.40] What it really did was it gave the ML practitioners control over the labelling process, right?
[871.40 → 874.32] So it wasn't like an outsourcing firm that was really like finance using.
[874.50 → 877.70] And then you're sort of like, you know, kind of like sneaking your project like into their
[877.70 → 878.20] budget.
[878.20 → 882.84] It's like now you actually are running a labelling process, and you're really looking at the
[882.84 → 884.98] data, and you're like writing the instructions.
[884.98 → 889.70] And I really deeply believe that that's essential in almost every case for making a machine learning
[889.70 → 892.24] thing work in production.
[892.24 → 898.32] Yeah, it almost seems like, you know, when you were doing your research work, you really
[898.32 → 903.86] found these issues with the foundational, the underlying data itself and the annotation
[903.86 → 904.40] process.
[904.40 → 910.38] And then like assuming you have some data to work with, it seems like the next sort of level
[910.38 → 917.64] up are these developer tools that were either non-existent or really rough or not being used
[917.64 → 918.44] or something like that.
[918.44 → 921.82] And that seems like at the level of weights and biases.
[922.18 → 926.40] I'm curious if that's how your thought process like went, because it seems like, you know,
[926.58 → 928.32] it seems like a natural progression to me.
[928.40 → 933.54] But I'm not sure if, you know, after you had thought about the data, the data and annotation
[933.54 → 938.58] problems for a while, you just, you know, your sort of next pain point or your next obvious
[938.58 → 942.12] layer in that stack was that layer up of developer tools.
[942.68 → 946.02] Well, actually, I'll be a little more specific since we're on a long podcast.
[946.02 → 950.88] I normally kind of skip over these details, but honestly, what happened really was I got
[950.88 → 955.46] kind of worried when I was running figure eight that I was getting out of date.
[955.70 → 960.26] Like I remember at my first job, there was a big fight between rule-based systems and
[960.26 → 961.22] machine learning systems.
[961.82 → 966.88] And I remember kind of looking at the, you know, mid-30s guys or 40-something guys who
[966.88 → 970.34] had, you know, kind of invested a lot in rule-based systems.
[970.34 → 973.44] And they were kind of like, oh, this machine learning stuff is stupid.
[973.76 → 977.38] Like, you know, it's like hard to scale, requires a lot of training data, like hard to deploy.
[978.00 → 980.02] And I remember just looking at them and thinking, you guys are like idiots.
[980.02 → 983.94] Like you've just like committed yourself to this one thing, and you can't see that this
[983.94 → 984.52] new thing's better.
[984.52 → 984.74] Right.
[984.74 → 989.26] And I, I kind of found myself, I hadn't done a lot of, you know, training models in a
[989.26 → 989.62] long time.
[989.70 → 994.32] You know, I was running a company, and I was kind of saying the same stuff about deep learning.
[994.32 → 996.50] Like I was like, you know, like, is this really better?
[996.50 → 998.06] Like it seems really hard to deploy.
[998.40 → 1001.68] And I was kind of looking in the mirror, like, man, I am like out of date.
[1001.76 → 1002.46] Like, I don't know.
[1002.76 → 1005.42] I don't really know how, like what TensorFlow does.
[1005.60 → 1007.96] Like I pretend I do, but I haven't like messed with it.
[1008.44 → 1009.84] I was feeling terrible about that.
[1009.84 → 1015.46] And then I, I got myself in a like an internship at OpenAI where I worked for like, you know,
[1015.54 → 1018.38] a really, really smart 24-year-old for a little while.
[1018.88 → 1021.82] And I just was like, just make me do all your dirty work.
[1022.00 → 1025.38] I just want to kind of get back into doing something real.
[1025.38 → 1030.94] And it was kind of a shocking experience, I think, because I think the tooling had been
[1030.94 → 1037.26] bad for ML, but it's like strikingly, shockingly bad for deep learning, right?
[1037.26 → 1040.26] I think it just sort of exacerbates, you know, the problems even more.
[1040.42 → 1044.96] And so, you know, I quickly, like my entrepreneur brain is just like, I have to, I have to build
[1044.96 → 1046.50] tools to fix this up.
[1046.56 → 1050.64] And so I didn't last very long as an intern because I just really wanted to fix these
[1050.64 → 1052.34] underlying problems for everyone else.
[1052.42 → 1053.64] But I'd love to kind of go back.
[1053.64 → 1055.60] I mean, training models and doing research is so fun.
[1055.66 → 1058.62] I guess I just, I don't stick with it very well.
[1059.34 → 1063.42] Before we go on from that point though, I just wanted to draw, I mean, it's very insightful
[1063.42 → 1068.16] of you to recognize that, that thing that you had noticed before about, you know, the
[1068.22 → 1072.80] the older, you know, contingent at the work and then recognizing that you were in danger
[1072.80 → 1073.58] of doing that yourself.
[1073.58 → 1079.82] And I know I'm definitely older than Daniel and have certainly found myself in the same
[1079.82 → 1084.14] position when I was younger saying, oh, look at those older people that are doing it.
[1084.14 → 1085.50] And then when I got older, I did that.
[1085.54 → 1086.54] And I recognize that.
[1086.70 → 1090.06] And I think that's a great lesson for people out there is don't ever do that.
[1090.14 → 1093.50] Don't ever, no matter what age you're at, don't ever lock down on your technology.
[1093.50 → 1095.72] Don't ever be in love with it because it's going to change.
[1095.92 → 1096.62] It's going to change.
[1096.68 → 1098.56] And there's going to be a new best thing out there.
[1098.56 → 1101.46] Yeah, I think that there's, there's definitely a balance.
[1101.58 → 1107.08] I mean, maybe I'm saying this because like, I'm too, too stubborn, but I think there's
[1107.08 → 1111.18] definitely a balance because there's like the side of things where like, if you're not
[1111.18 → 1116.30] passionate enough about something and stick with something long enough, it takes a good
[1116.30 → 1120.24] amount of time to like, really like make a difference in a certain area.
[1120.36 → 1126.14] But then also like, you have to be willing to sort of jump ship onto other things occasionally.
[1126.14 → 1129.22] So yeah, I definitely think that there's a cycle with that.
[1129.42 → 1130.52] And it's hard to do.
[1130.74 → 1131.56] It is hard to do.
[1131.68 → 1136.68] It's hard to find that sweet spot of committing enough to becoming very good at what you're
[1136.68 → 1139.40] trying to get done at the moment and knowing when to shift.
[1139.70 → 1141.38] Yeah, it's not an automatic thing.
[1141.58 → 1142.76] So I just want to draw that out.
[1142.82 → 1143.80] It was a great point you made there.
[1144.16 → 1150.04] Yeah, I'm curious if you could go into like, we do like to get into the weeds sometimes here,
[1150.04 → 1154.84] but like in that state, when you're doing that internship with OpenAI and when you're
[1154.84 → 1160.44] talking about the tooling, quote unquote, like what was your workflow like during that time
[1160.44 → 1162.64] in terms of training models and that sort of thing?
[1162.72 → 1165.86] Like what were the tools at your disposal for you to use?
[1166.36 → 1166.54] Totally.
[1166.64 → 1166.80] Yeah.
[1166.90 → 1170.24] I mean, it was funny actually, because I also was like, you know, kind of working for a
[1170.24 → 1171.32] 24-year-old, 25-year-old.
[1171.54 → 1175.06] I felt really embarrassed that I was like using Emacs, which like, not my employees think
[1175.06 → 1177.76] that's kind of cool, but like, you know, I was like, I'm going to use VS Code.
[1177.92 → 1179.22] Like, I'm just going to use the latest stuff.
[1179.32 → 1182.38] I'm not going to, you know, I can't be using these crap tools.
[1182.38 → 1185.60] We're not offending any of the Emacs users out there.
[1185.94 → 1186.64] Right, right.
[1187.06 → 1188.86] I gave up my.Emacs files.
[1189.44 → 1192.38] Now it's super, you know, it's hardcore, you know.
[1192.38 → 1195.58] I know now people think it's hardcore, but come on, like VS Code is good.
[1195.74 → 1196.02] I don't know.
[1196.26 → 1197.48] Yeah, VS Code is good.
[1197.66 → 1197.76] Yeah.
[1197.90 → 1202.34] A lot of people have moved off of Vim and Emacs finally, you know, after resisting for years
[1202.34 → 1203.06] to VS Code.
[1203.16 → 1204.78] I mean, it's made a big difference in the industry.
[1205.06 → 1206.22] I strongly recommend it.
[1206.48 → 1207.28] That's what I use.
[1207.32 → 1209.30] I moved away from the other stuff into that, so.
[1209.30 → 1209.50] Yeah.
[1210.00 → 1212.46] But it's actually, it's another one where, you know, you build up these, like, you know,
[1212.50 → 1213.88] your.Emacs file.
[1214.02 → 1215.06] You don't want to give it up.
[1215.16 → 1216.10] And my hand's still, like.
[1216.10 → 1217.00] You've invested so much.
[1217.24 → 1218.20] Yeah, yeah, exactly.
[1219.04 → 1219.32] Yeah.
[1219.66 → 1222.92] But, you know, so OpenAI was unique in that they had a ton of compute resources.
[1223.44 → 1229.24] But at the time, it was actually basic stuff, like just trying to train across multiple GPUs
[1229.24 → 1230.70] was an enormous pain.
[1230.70 → 1234.60] I mean, even setting things up was painful.
[1234.66 → 1237.10] I think still is way more painful than it needs to be.
[1237.10 → 1241.12] Like, just like, you know, you buy a GPU at the store, and then you want to train a model
[1241.12 → 1241.48] on it.
[1241.84 → 1247.12] I mean, expect to wait a day, you know, while you go through the latest iteration.
[1247.26 → 1250.80] And then, like, you know, you have to find something that came out in the last, like,
[1250.82 → 1254.06] three or four months or else it's, you know, the instructions are going to be wrong.
[1254.74 → 1256.30] And this is totally NVIDIA's fault.
[1257.80 → 1259.24] Look at it squarely there.
[1259.24 → 1264.50] But yeah, I mean, the startup workflow definitely has room for improvement.
[1264.66 → 1265.02] Absolutely.
[1265.76 → 1265.96] Yeah.
[1265.96 → 1267.42] I found that as well over time.
[1267.42 → 1271.84] And you'd love for those artifacts that, like, or implementations from, like, a year
[1271.84 → 1274.82] and a half ago, it seems like this is exactly what I want to do.
[1274.98 → 1280.78] But, like, I haven't got to start over because it doesn't, you know, it's some compatibility
[1280.78 → 1281.76] issue or something.
[1281.76 → 1285.48] Yeah, like, I thought, you know, I thought I would never see, like, a linker error in
[1285.48 → 1289.60] my life, you know, after, like, 2006, you know, but, like, you know, now you see them
[1289.60 → 1292.88] when you're just trying to, you know, get your situation set up.
[1292.98 → 1296.96] And, you know, I think, like, collabs and stuff have really helped with this and made the
[1296.96 → 1301.20] onboarding smoother because even this is, you know, three years ago, maybe two, three years
[1301.20 → 1301.36] ago.
[1301.46 → 1303.06] So, look at me, I'm out of date again.
[1303.52 → 1307.54] But this wasn't even the problem that I was trying to solve, weights and biases, initially.
[1307.54 → 1313.50] And, actually, the thing that was really striking to me was just that you, it's really
[1313.50 → 1317.68] hard to go back and look at a run that you did in the past.
[1317.78 → 1321.38] And, I mean, this is something that's always been true, like, any kind of long-running thing.
[1321.44 → 1325.58] But I feel like with deep learning, your runs often take, like, days, right?
[1325.58 → 1329.12] So, you want to get a sense for if they're working right away, and you want to really have
[1329.12 → 1333.36] a good record of everything that happened, you know, from, like, system metrics to, like,
[1333.36 → 1337.00] exactly what was the last commit that went into your code to,
[1337.00 → 1341.66] and, you know, everyone has these, like, notebooks, you know, like, in their Emacs or VS Code
[1341.66 → 1345.14] or, like, maybe a Google Doc if you're really advanced, you know, where they're just kind
[1345.14 → 1348.44] of typing, like, okay, here's all the things I did, you know, and here's what happened.
[1348.46 → 1351.56] Or in file names, extra long file names.
[1352.10 → 1352.24] Yeah.
[1352.24 → 1352.60] Yeah, yeah.
[1353.22 → 1357.02] You know, that's a perfect point as well is the fact that as you move through the
[1357.02 → 1361.74] different phases of your workflow and, you know, you're kind of, you know, doing research
[1361.74 → 1365.86] in a notebook, and then you need to deploy it as a software component and stuff, there is still
[1365.86 → 1372.52] friction in the process in terms of moving through each of those very distinct phases of trying to
[1372.52 → 1375.54] get your workflow from the very, very beginning to the very, very end and deployed.
[1376.18 → 1379.90] And I think people still, everyone kind of customizes that quite a lot.
[1380.12 → 1382.74] That's a there's another opportunity out there for someone.
[1382.74 → 1387.66] I think there are a lot of opportunities right now in the like, tooling space for ML.
[1387.84 → 1391.26] I think it's like, you know, companies are really seriously doing it and I think every step
[1391.26 → 1392.34] is basically broken, right?
[1392.44 → 1396.54] Like, you know, from like, you know, you're visualizing your data to tracking your data
[1396.54 → 1401.24] to tracking your experiments to like, you know, deciding like gating deployments with
[1401.24 → 1403.68] like continuous integration to production monitoring.
[1403.80 → 1406.92] I actually think all of these things are huge pain points.
[1407.00 → 1410.16] I think there's going to be a lot of fascinating companies that spring up solving
[1410.16 → 1411.18] them in different ways.
[1411.56 → 1412.06] I think so.
[1412.28 → 1412.82] I'm curious.
[1413.10 → 1417.50] You talked a little bit about like, you know, wanting to go into this internship to figure
[1417.50 → 1421.90] out or once you started, you know, figuring out that there was this problem, like you
[1421.90 → 1427.26] had to start somewhere with like the tooling, like for a specific thing, where, where did
[1427.26 → 1433.58] you end up landing in terms of like the particular rough edges that you wanted to smooth off in
[1433.58 → 1434.00] the tooling?
[1434.16 → 1437.90] Like, where did you focus when you first started thinking about weights and biases?
[1438.32 → 1441.86] It's funny that, so the thing that we first started focusing on is now the thing that weights
[1441.86 → 1442.90] and biases is known for.
[1442.90 → 1447.52] I sort of expected to do, you know, a couple of different iterations and kind of like hit
[1447.52 → 1447.90] walls.
[1447.98 → 1451.54] But I think this is an example of like, you know, the second time you do a company when
[1451.54 → 1455.74] you've kind of been in the space for 10 years, you have better instincts about what the needs
[1455.74 → 1455.92] are.
[1456.08 → 1460.38] So the thing that I started with, which is really what weights and biases is known for,
[1460.74 → 1463.44] is essentially tracking, tracking your training.
[1464.02 → 1468.22] And it was basically like, you know, Tensor Board was doing this, but it really only worked with
[1468.22 → 1469.08] TensorFlow at the time.
[1469.08 → 1473.28] And it was hard to look at multiple runs, which is really what you want.
[1473.98 → 1477.64] And so, you know, they sort of have a way of doing, putting hyperparameters into the
[1477.64 → 1479.16] name of the run, which I think is kind of awful.
[1479.32 → 1480.58] I really don't recommend that.
[1481.00 → 1486.46] And then it's clearly not designed to show you like runs in the context of other runs,
[1486.52 → 1486.66] right?
[1486.68 → 1489.72] Like, you know, the fact that like your model has like this accuracy after like eight
[1489.72 → 1492.24] epics, it's kind of not that interesting.
[1492.34 → 1495.48] Like, what's more interesting is like, how did the accuracy change from the previous thing
[1495.48 → 1495.96] you did?
[1496.30 → 1499.90] And then also, you know, being able to dive in and look at exactly what was that previous
[1499.90 → 1501.26] thing you did like that.
[1501.34 → 1504.26] That was sort of the core of the beginning of weights and biases.
[1504.26 → 1510.08] And still, I think the thing that people appreciate most about us is like saving all the metrics
[1510.08 → 1514.38] of a run, you know, all the performance metrics, the system metrics and the sort of like accuracy
[1514.38 → 1519.06] loss and those kinds of performance metrics and being able to quickly compare them with lots
[1519.06 → 1519.74] of other runs.
[1519.74 → 1524.14] Could you describe that a little bit about how, you know, how that contextual comparison
[1524.14 → 1529.40] is realized and how that's different from previous tools people might have used?
[1529.72 → 1529.98] Totally.
[1530.06 → 1532.22] And I think Tensor Board is the best comparison.
[1532.38 → 1534.38] But, you know, I mean, let's pick a concrete example.
[1534.52 → 1536.50] Like, say you're trying to train a self-driving car.
[1536.96 → 1537.14] So, right.
[1537.18 → 1538.68] So, say you're doing perception of self-driving cars.
[1538.78 → 1542.12] So, you know, you're looking at these images, and you're doing semantic segmentation where you
[1542.12 → 1545.02] want to like to label each pixel with what's in that pixel.
[1545.10 → 1548.06] Is it a pedestrian or is it like a road or like what's going on?
[1548.10 → 1548.22] Right.
[1548.22 → 1552.46] So, you know, the first cut of what you can do is as the model trains, you can look at
[1552.46 → 1553.84] the loss function.
[1553.98 → 1554.08] Right.
[1554.12 → 1557.24] And, you know, whatever that loss function is, you can see if it's, you know, going up
[1557.24 → 1559.80] or down and hope it's going down because it's what you're optimizing.
[1560.12 → 1563.58] And you might want to compare that to like other runs you did, maybe with different hyper
[1563.58 → 1565.06] parameters or different state of the code.
[1565.08 → 1567.54] But say like you have one with a higher learning rate and a lower learning rate.
[1568.04 → 1568.98] You want to see which is better.
[1569.04 → 1569.20] Right.
[1569.86 → 1574.52] Now, what turns out the second you start to do this is you realize that better worse is more
[1574.52 → 1575.62] complicated than you think.
[1575.62 → 1575.84] Right.
[1575.90 → 1576.30] So, like.
[1576.30 → 1576.66] Yeah.
[1576.66 → 1578.24] How do you define that?
[1579.54 → 1579.90] Exactly.
[1580.12 → 1582.52] So, you know, first you're looking at the loss, and you're like, oh, great.
[1582.58 → 1584.24] This run has like better loss.
[1584.30 → 1584.40] Right.
[1584.42 → 1588.50] But then, you know, it actually might be that when you look at accuracy, which is a more
[1588.50 → 1590.88] actionable thing, it completely flips.
[1591.06 → 1591.20] Right.
[1591.24 → 1594.50] So like the lower learning rate has actually higher accuracy at the end.
[1594.54 → 1594.68] Right.
[1594.68 → 1597.46] But then you might say, well, what is accuracy really like?
[1597.46 → 1601.32] You know, like maybe it's just predicting that everywhere is a road, you know, just ignoring
[1601.32 → 1604.26] the pedestrians because there are not many pixels that correspond to a pedestrian.
[1604.76 → 1605.52] So now you say, you know what?
[1605.52 → 1609.48] I don't want to have anything with like under ninety-nine point nine percent pixel accuracy
[1609.48 → 1610.12] on pedestrians.
[1610.12 → 1610.54] Right.
[1610.54 → 1615.08] And so now, you know, maybe you didn't check that the first couple of times you changed
[1615.08 → 1615.36] your model.
[1615.42 → 1617.92] So you want to go back and look at what those were.
[1617.92 → 1621.44] And so, like, you know, the requirements as you do this in the real world, they
[1621.44 → 1625.66] keep changing as the businesses change, and you realize, you know, that things are different.
[1626.06 → 1630.04] And so fundamentally, what, you know, what the kind of core weights and biases tool does
[1630.04 → 1632.74] is it tracks all this stuff for you, and it shows it to you in graphs.
[1633.02 → 1637.32] But then why you might really want this is like, you know, six months from now, you've
[1637.32 → 1640.54] deployed this model into a car and the car crashes.
[1641.04 → 1641.44] Right.
[1642.06 → 1645.76] Now you really want to know, OK, what was that what was that model trained on?
[1645.76 → 1648.76] Like what was happening in the training that made you think you could deploy it?
[1649.10 → 1650.90] You know, like where could things have gone better?
[1650.90 → 1651.16] Right.
[1651.20 → 1655.32] And like if you don't do this in like a systematic way, like with weights and biases, you can
[1655.32 → 1656.38] imagine it's going to be really hard.
[1656.44 → 1660.88] Like if you're just tracking like notes, you know, in your Emacs file, it's probably not
[1660.88 → 1662.64] going to include all the detail that you wish you had.
[1662.76 → 1665.92] So what we try to do is capture lots of stuff passively.
[1666.70 → 1667.06] Right.
[1667.10 → 1671.90] And we think that like when you capture like everything passively, and you don't put a burden
[1671.90 → 1677.44] on the person training, you get a lot more useful information because usually
[1677.44 → 1679.26] you want this information like after the fact.
[1680.04 → 1685.58] And when you say passively, you're meaning like you don't want a user to decide like,
[1686.12 → 1690.62] you know, weights and biases, save this parameter and save this parameter, but not like these
[1690.62 → 1697.54] other things you want to kind of enable or disable rather than like having a user like
[1697.54 → 1701.58] click a bunch of boxes for all the things that they want to that they want to save.
[1701.68 → 1702.30] Is that what you mean?
[1702.78 → 1703.70] Yeah, I'll give you an example.
[1703.70 → 1707.40] I mean, so just fundamentally the way this works is you import a library and then our
[1707.40 → 1711.42] library basically collects lots of, you know, system metrics and other metrics as it runs
[1711.42 → 1714.60] kind of similar to Tensor Board, but we collect a lot more stuff.
[1715.12 → 1717.00] I'll give you an example of the sort of passiveness of it.
[1717.08 → 1720.98] Like, you know, one thing you should probably do before a big training run is like commit
[1720.98 → 1722.28] your code into Git.
[1722.74 → 1722.90] Right.
[1722.90 → 1727.28] And so like, you know, we could just like to connect each training run you do to the commit
[1727.28 → 1727.52] shot.
[1727.58 → 1729.48] And we do that if you want us to.
[1729.94 → 1733.68] But one thing we found, right, because we're talking to people all the time is like, you
[1733.68 → 1736.66] know, most of the time people don't actually commit that code before it runs.
[1736.72 → 1736.88] Right.
[1736.90 → 1741.02] So, you know, we capture not just the commit shot, but also a diff against the latest
[1741.02 → 1741.70] commit shot.
[1741.84 → 1747.52] So that way, like every time, you know, every time you do a training run, we keep track for
[1747.52 → 1751.22] you the exact state of the code, the way it was when it trained.
[1751.32 → 1751.46] Right.
[1751.46 → 1755.08] And that way, you know, like a month later, you know, you want to go back and like look
[1755.08 → 1757.54] at something and be absolutely sure what the state of the code was.
[1757.88 → 1759.88] You can do that, but you never need to think about it.
[1759.92 → 1760.02] Right.
[1760.02 → 1764.92] Like once you turn that on one time, now you'll be sure that every single time your model trains,
[1765.36 → 1767.40] there's a snapshot of exactly the state of the code.
[1767.42 → 1769.34] And you might say, well, that's like a waste of space.
[1769.34 → 1772.52] But like, come on, like if you look at the size of training data sets, you know, they're
[1772.52 → 1773.58] going to be like petabytes.
[1773.74 → 1773.84] Right.
[1773.84 → 1777.36] So, you know, you could do this kind of all day long, like capture every metric you might care
[1777.36 → 1781.34] about, all the state of the code, everything going on, like, you know, exactly what kind
[1781.34 → 1782.14] of hardware it was on.
[1782.18 → 1786.76] You can capture all this without really making a dent into a modern machine's storage.
[1787.18 → 1791.58] Would it be fair, as you say that, you know, I know that certainly Daniel and I come from
[1791.58 → 1794.04] a developer background in addition to a data background.
[1794.04 → 1798.68] And, you know, something that we've talked about lots over time is kind of the maturity
[1798.68 → 1801.66] of DevOps relative to the maturity of data ops.
[1801.96 → 1805.56] And you're clearly, you know, as you just, as you were just explaining that, you know,
[1805.56 → 1808.02] you're clearly kind of addressing some of that.
[1808.46 → 1813.84] Is that maybe the core participants in those two arenas are coming from fundamentally different
[1813.84 → 1814.88] places, do you think?
[1814.92 → 1819.58] Or those of us who have been developers prior to doing machine learning, and we're kind of
[1819.58 → 1822.34] carrying some of that in, and we try to put that in place.
[1822.44 → 1825.58] I mean, is this just different constituents that this arises from?
[1825.66 → 1829.34] And maybe a data scientist wasn't worried about data ops because it wasn't a mature enough
[1829.34 → 1832.76] field prior to this, but now it's important?
[1833.42 → 1834.46] What's your take on that?
[1834.92 → 1837.38] Yeah, I mean, look, I think, like, I'll say a couple of things on that.
[1837.46 → 1843.84] So first, I think data science trains you to be bad at DevOps, right?
[1843.84 → 1846.02] It's actually a different thing than engineering.
[1846.20 → 1851.32] And most of the code that you write as a data scientist or an ML practitioner, most of it's
[1851.32 → 1851.80] throwaway.
[1851.94 → 1853.14] And I can really relate to this, right?
[1853.16 → 1857.02] Because I came from this world, and I was kind of surprised when I got, I remember I got to
[1857.02 → 1860.72] Yahoo and I checked in some code that actually crashed the search engine, and they were like,
[1860.80 → 1861.96] man, you are a moron.
[1863.54 → 1864.76] That's a claim to fame, though.
[1864.92 → 1865.58] That is.
[1865.74 → 1866.34] That's a good one.
[1866.44 → 1868.16] You can work that into conversation now.
[1868.64 → 1870.98] Yeah, I mean, they should have put some more controls around me, honestly.
[1870.98 → 1874.98] But I just really like didn't, you don't get trained in like testing.
[1875.36 → 1879.06] And not only that, but what you do get trained is that like most of your stuff is throwaway.
[1879.14 → 1883.20] So you have this very, very 80-20 rule of I just want to write a lot of fast code, kind
[1883.20 → 1886.98] of figure out what's going on, and then like toss it over the fence to someone to kind of
[1886.98 → 1887.80] harden it, right?
[1888.04 → 1894.20] I think that that breaks now that AI is getting used in, so many like mission-critical applications,
[1894.30 → 1898.64] even like applications where, you know, someone could get seriously hurt or like terrible
[1898.64 → 1899.26] things could happen.
[1899.26 → 1905.44] And so I think the other thing that happens is that DevOps doesn't really understand machine
[1905.44 → 1910.58] learning and data science that well, and they're not really prepared for the statistical nature
[1910.58 → 1911.04] of it, right?
[1911.10 → 1915.28] So for example, I mean, just, you know, like continuous integration tools, they crash if
[1915.28 → 1916.40] any test fails, right?
[1916.42 → 1920.22] And that totally makes sense, you know, from like a normal engineering perspective.
[1920.56 → 1920.64] Yeah.
[1920.72 → 1925.82] But it's just not realistic to have a suite of continuous integration, like real world continuous
[1925.82 → 1927.38] integration tests for a machine learning thing, right?
[1927.38 → 1931.88] The machine learning stuff that we put into production, we know that it has like a failure
[1931.88 → 1932.72] rate that's non-zero.
[1933.50 → 1937.60] And so instead we have to like deal with that versus trying to drive the failure rate down
[1937.60 → 1938.50] to exactly zero.
[1938.64 → 1942.96] And so I think there's a real culture gap and there's very, very few people trained in
[1942.96 → 1944.90] both DevOps and machine learning.
[1945.00 → 1947.50] And those people make tons of money as I've seen.
[1947.50 → 1952.88] So it's cool when someone has both skills, but it's natural that people don't have both
[1952.88 → 1953.10] skills.
[1953.22 → 1958.10] And I think the skills in a way teach you very different styles of development.
[1958.72 → 1963.02] As a two-second follow up to that, as we get to where we're deploying out there and
[1963.02 → 1967.84] you're addressing it with the workflow that you guys have been creating, how do you address
[1967.84 → 1973.58] the use cases, the variability in the use cases in terms of if it is something that is
[1973.58 → 1977.28] more just kind of typical consumer than totally see your point.
[1977.60 → 1981.50] But there are use cases where you have these models that are going into, that are starting
[1981.50 → 1986.64] to go into life and death, you know, issues, you know, where people's safety is becoming
[1986.64 → 1988.88] dependent upon it, and they are trained.
[1989.18 → 1990.88] 99% is not going to be acceptable.
[1991.36 → 1996.52] Is there a point there where you evaluate or cross over or acknowledge that in some way
[1996.52 → 2000.50] or how, whether now or in the future, how would you address that kind of variability
[2000.50 → 2004.78] in your starting to get models in so many different real life situations that you have
[2004.78 → 2005.80] to account for that issue?
[2006.58 → 2012.52] Well, I mean, look, Ways and Bias' mission is to support the ML practitioners to see what's
[2012.52 → 2013.30] going on, right?
[2013.36 → 2018.30] So, you know, we're not trying to tell you if 95% accuracy is good enough.
[2018.54 → 2023.20] What we're trying to be sure is that you know what you have, and you know if it's 95% or 99%.
[2023.20 → 2028.68] And then you can also dig in and say, okay, this is 99% on roads, but only 8% on pedestrians.
[2028.68 → 2031.14] And that's, you know, I should flag it.
[2031.40 → 2033.72] I also think like, I think it would be nice.
[2033.86 → 2038.80] It's hard to acknowledge, but I think the industry does have to acknowledge that 100%
[2038.80 → 2042.54] accuracy in most applications is not attainable even in life or death ones, right?
[2042.56 → 2046.96] So I think it's really hard to come out and say like, look, like, you know, this self-driving
[2046.96 → 2050.36] car is going to get it wrong, you know, 0.001% of the time or whatever.
[2050.54 → 2055.34] But, you know, people talk about miles between intervention, and it's not infinity miles between
[2055.34 → 2055.80] intervention.
[2055.80 → 2058.36] And humans also, by the way, are not 100% accurate.
[2058.72 → 2062.20] So, you know, that's a little bit outside the scope of what we try to do.
[2062.30 → 2067.68] But I think fundamentally, as we do more and more complicated things, it's better to acknowledge
[2067.68 → 2072.58] that errors are inevitable and have plans to deal with them than try to claim that there
[2072.58 → 2073.22] are no errors.
[2073.64 → 2073.72] Gotcha.
[2074.22 → 2079.08] I'm curious about a sort of different side of variability, not so much on the performance
[2079.08 → 2085.30] of the actual model side, but as a package that someone imports into all sorts of different
[2085.30 → 2085.76] workflows.
[2086.22 → 2091.48] There's such variety now in terms of like the tooling that people are using for their
[2091.48 → 2092.16] ML workflows.
[2092.28 → 2096.14] And I see like on your website, you're talking about, you know, kind of integrating weights
[2096.14 → 2102.02] and biases into all sorts of workflows, TensorFlow, PyTorch, Keras, Scikit-learn, you know, hugging
[2102.02 → 2104.82] face, transformers, all sorts of things.
[2105.28 → 2110.70] You know, could you speak a little bit to that challenge in terms of, you know, I'm sure as
[2110.70 → 2116.42] a company and as a, you know, sort of product roadmap, it is extremely difficult to sort of
[2116.42 → 2122.70] understand and navigate like how tightly you're integrated with various things versus other
[2122.70 → 2128.70] things and how to reasonably support the variety of tooling that's out there in AI right now.
[2128.92 → 2131.86] How do you, in general, do you think about that and approach that?
[2132.44 → 2134.34] Well, it's a conversation with our customers.
[2134.58 → 2137.92] So, you know, when you sign up for weights and biases, we really only ask you two or three
[2137.92 → 2138.60] questions, right?
[2138.64 → 2141.36] And, you know, one question is how often do you train models?
[2141.92 → 2145.86] And if you answer that, that you train models frequently, then we take very seriously
[2145.86 → 2149.16] to answer the next question, which is what frameworks and other tools do you use?
[2149.22 → 2153.14] And so, you know, when we see something like TAX being used by lots of people that train
[2153.14 → 2157.58] their models frequently, we say, okay, we should prioritize a good TAX integration.
[2158.48 → 2159.92] And you're right, it's tricky.
[2160.04 → 2162.54] I mean, I think it's nice that you appreciate the work that we do.
[2162.62 → 2165.26] I mean, a lot of people look at what we do, and it's just like we generate these graphs
[2165.26 → 2171.26] really quickly and making these graphs, I hope that it's kind of a simple experience for
[2171.26 → 2175.62] the user, but it's a tough challenge for engineers to make sure that those all kind of
[2175.62 → 2180.00] reliably generate in a way that's useful to our users, regardless of what framework.
[2180.14 → 2182.48] I mean, forget about framework, like Python version.
[2182.94 → 2189.54] Also, like PyTorch and TensorFlow, both incredibly cavalier about making breaking changes to their
[2189.54 → 2190.00] libraries.
[2190.16 → 2191.36] So it's definitely a challenge.
[2191.36 → 2191.88] Yeah.
[2191.88 → 2191.94] Yeah.
[2191.94 → 2192.00] Yeah.
[2192.00 → 2192.06] Yeah.
[2192.06 → 2192.40] Yeah.
[2192.40 → 2192.94] Yeah.
[2192.94 → 2193.94] Yeah.
[2193.94 → 2194.06] Yeah.
[2194.06 → 2194.12] Yeah.
[2194.12 → 2194.16] Yeah.
[2194.16 → 2194.18] Yeah.
[2194.18 → 2194.68] Yeah.
[2194.68 → 2195.18] Yeah.
[2195.18 → 2195.28] Yeah.
[2195.28 → 2195.68] Yeah.
[2195.68 → 2196.18] Yeah.
[2196.18 → 2196.22] Yeah.
[2196.22 → 2197.12] Yeah.
[2197.12 → 2198.12] Yeah.
[2198.12 → 2198.18] Yeah.
[2198.18 → 2198.22] Yeah.
[2198.22 → 2199.12] Yeah.
[2199.12 → 2200.12] Yeah.
[2200.12 → 2200.22] Yeah.
[2200.22 → 2201.12] Yeah.
[2201.12 → 2202.12] Yeah.
[2202.12 → 2202.22] Yeah.
[2202.22 → 2203.12] Yeah.
[2203.12 → 2206.62] Sure.
[2206.62 → 2207.12] Sure.
[2207.12 → 2213.40] The best way for you to directly support Practical AI.
[2213.40 → 2220.56] Join today and unlock access to a private feed that makes the ads disappear, gets you closer
[2220.56 → 2225.60] to the metal, and help sustain our production of Practical AI into the future.
[2225.60 → 2229.50] Simply follow the changelog++ link in your show notes
[2229.50 → 2233.92] or point your favourite web browser to changelog.com slash plus.
[2233.92 → 2238.14] Once again, that's changelog.com slash plus.
[2239.42 → 2241.88] Changelog++ is better.
[2255.60 → 2263.02] So, Lucas, I would be curious to hear a little bit.
[2263.02 → 2266.74] So we talked a lot about experiment tracking, which I know is, like you say,
[2266.82 → 2272.58] where you kind of started with this journey and maybe what Weights and Biases is most known for.
[2272.74 → 2277.00] But as I'm exploring the website and the feature set that you're supporting,
[2277.20 → 2278.50] there are some other things.
[2278.66 → 2283.78] In particular, I see like sweeps, which I think is related to hyperparameter tuning,
[2283.78 → 2287.98] and then artifacts, which is related to data set versioning.
[2288.40 → 2290.36] I'm really curious about the latter one, actually.
[2290.36 → 2293.32] I'm really passionate about data versioning, actually.
[2293.98 → 2297.50] And so I was curious, you know, when this came about,
[2297.90 → 2301.08] it seems to me like maybe a couple of years ago,
[2301.08 → 2302.96] if I was talking about like data versioning,
[2303.02 → 2306.72] like people just like had no idea what I was talking about.
[2306.78 → 2310.78] And now there is this sort of acknowledgement that there's something here.
[2310.78 → 2315.62] And maybe that's, you know, fed into the support of that and Weights and Biases.
[2315.94 → 2319.26] So, yeah, could you tell us a little bit about your support for that
[2319.26 → 2323.24] and also your thought process around data versioning and how you think about it?
[2323.80 → 2328.02] Sure. I mean, I would say all the things that we add are 100% customer driven.
[2328.28 → 2332.28] So, you know, if you're a practitioner, and you want us to make tools for you,
[2332.68 → 2336.52] come into our Slack channel and talk about what you're doing and tell us what you need.
[2336.56 → 2338.20] And we would love to make things to support that.
[2338.20 → 2339.56] So that's how all this stuff came about.
[2340.10 → 2342.98] I would say, you know, hyperparameter, we call it sweeps,
[2343.08 → 2344.86] hyperparameter search or hyperparameter sweeps.
[2345.24 → 2349.12] We built because everyone kept telling us, yeah, we know this is best practice.
[2349.70 → 2351.16] We know there are a lot of tools available.
[2351.92 → 2354.70] But when you ask them, okay, which of these tools are you using?
[2354.80 → 2355.32] How are you doing it?
[2355.34 → 2359.82] They'd always be like, I'm kind of doing a random search with my own home-grown stuff.
[2359.88 → 2362.46] And when I hear that as an entrepreneur making tools, it's like, okay,
[2362.56 → 2364.32] these tools aren't working for you.
[2364.36 → 2365.32] Like, why aren't they working for you?
[2365.32 → 2369.56] And I think it's because the reality of hyperparameter search is messier than the theory of it, right?
[2369.58 → 2374.56] Like the math behind doing Bayesian optimization or things like that, it's not so complicated.
[2375.04 → 2380.22] What is complicated is the real world where you start to do it in a distributed way and six of your runs break.
[2380.22 → 2384.32] And then you decide to change the code midway through your search, but you don't want to throw away your old data.
[2384.32 → 2390.66] And so we've really tried to focus on that and kind of making it simple to do and simple to see what's going on.
[2391.10 → 2396.34] And in fact, you can use other optimization libraries that would even tell you maybe better than ours, right?
[2396.34 → 2401.88] So you can use Cartoon, which I think is a fantastic library to do advanced stuff that you can't do with us.
[2401.94 → 2403.10] So that's how we think about that.
[2403.68 → 2411.28] And I would actually say data versioning is almost the same thought process where people know that they should be versioning their data, right?
[2411.28 → 2414.16] They know that it's dangerous to not version their data.
[2414.24 → 2418.98] And you know that you can't have real reproducibility unless you version your data.
[2419.30 → 2423.48] But I think that all the existing solutions were kind of causing problems.
[2423.48 → 2429.78] So I think Git has the large file store system, which seems like it should be made for this kind of thing.
[2429.88 → 2434.12] But when we talked to practitioners, most of them weren't actually using that.
[2434.40 → 2435.84] And so we kind of dug into why.
[2435.94 → 2439.18] And it's like, well, a lot of datasets these days are in object stores.
[2439.18 → 2442.78] So supporting an object store is incredibly important for versioning data, I think.
[2443.00 → 2450.24] And then another detail that shouldn't be overlooked is most ML practitioners are not super fluent with Git, right?
[2450.24 → 2453.24] They find Git to be kind of a scary interface.
[2453.44 → 2454.68] DevOps people find it trivial.
[2454.80 → 2461.30] In fact, my co-founder, Sean, comes from less of an ML background, and it's more of a kind of DevOps background.
[2461.30 → 2465.80] And he just constantly makes fun of me for how bad I am at Git.
[2465.96 → 2473.00] In his view, I just kind of type in random commands into Git until I break everything and then ask him to fix the stuff.
[2473.12 → 2481.60] But I think that was a little bit eye-opening for him when he was designing the versioning because he's like, I have to really dumb this down to make something that Lucas can understand and use.
[2482.64 → 2483.78] Yeah, I think that's a real thing.
[2484.74 → 2487.18] You're representing your customers in that way too, though.
[2487.28 → 2488.52] I mean, there's something to be said for that.
[2488.52 → 2498.98] Yeah, no, I mean, I remember this a couple of years ago, our conference, New York, which they're going to be having another one here soon, which Chris and I are going to lead a panel or moderate a panel on.
[2498.98 → 2504.30] I remember in that conference, they had like a Git workshop sort of deal.
[2504.42 → 2514.68] And it was like one of the most popular, like people were just like so into it because there is this sort of like, yeah, I can create a repo and like maybe make an initial commit.
[2514.68 → 2519.04] But then I like all this stuff happens, and I have no idea and get scared.
[2519.34 → 2519.92] It gets scared.
[2520.14 → 2522.18] When stuff gets weird, it's just like, oh, like.
[2523.52 → 2523.90] No, really.
[2524.02 → 2528.22] I mean, if you haven't been doing professional software development for a while, Git is scary.
[2528.56 → 2529.34] It really is.
[2529.42 → 2533.16] I mean, I've seen a lot of people getting into the field, and they struggle with it and stuff.
[2533.22 → 2539.54] So I totally I'm very empathetic to people who are coming from a data science background, and they're trying to figure out how to do this.
[2539.88 → 2541.84] Either Git or something similar to that.
[2541.84 → 2542.76] It's a new concept.
[2542.76 → 2546.66] So there's a cultural barrier that has to be surmounted there.
[2547.20 → 2547.24] Right.
[2547.36 → 2547.56] Right.
[2547.98 → 2548.64] Yeah, definitely.
[2549.08 → 2557.06] So when you are kind of seeing, and I'm sure I was looking through your website, there are lots of good stories and that sort of thing on there.
[2557.30 → 2569.76] But in terms of like success stories with weights and biases and like the workflow that people used, you know, could you give us like tease us with sort of example?
[2569.76 → 2586.36] I know I'm putting you on the spot, but in terms of, you know, maybe a team that was doing something, you know, rolling, trying to roll their own before and then was able to switch over to some tooling, maybe a combination of what you offer and other things to accomplish something.
[2586.50 → 2588.34] Do you have one of those stories you could share?
[2588.34 → 2589.46] Yeah, totally.
[2589.66 → 2594.34] I'll tell you my one of my favourite ones because it's so practical and just so great.
[2594.86 → 2597.20] Although it's been told, the application has been told a couple of times.
[2597.30 → 2599.76] You may have heard it before, but I feel really proud of it.
[2599.80 → 2602.78] So this is a team at John Deere called Blue River.
[2602.78 → 2608.96] And they basically make a system that looks down at lettuce and tractors.
[2609.62 → 2612.46] And if it sees weeds, it sprays the weeds.
[2612.64 → 2613.78] I believe it's with fertilizer.
[2613.94 → 2617.48] So it burns the weeds, and then it becomes fertilizer for the lettuce.
[2617.62 → 2617.74] Right.
[2617.74 → 2624.22] So instead of blanketing the fields with pesticides, they aim a sprayer at the weeds.
[2624.22 → 2625.06] I've seen those videos.
[2625.26 → 2625.78] It's amazing.
[2626.28 → 2626.42] Yeah.
[2626.48 → 2627.68] And they did a whole case study with us.
[2627.68 → 2633.30] So I know I can go into detail, and you could maybe post the case study where they actually show their weights and biases runs and how they think about it.
[2633.70 → 2642.60] But, you know, when we went in there, they were, you know, having the problem of they were training tons and tons of models and trying to keep track of which models they were making and what they were learning.
[2642.60 → 2645.52] And then also kind of what was getting put into production.
[2645.62 → 2645.70] Right.
[2645.72 → 2646.32] Because it's kind of high.
[2646.42 → 2647.30] I mean, it's kind of high stakes.
[2647.30 → 2647.94] It's very high stakes.
[2647.94 → 2654.52] If you're a farmer, you can't have your crops get killed by your AI eating machine.
[2654.52 → 2660.36] And a single percentage over, you know, hundreds of thousands of acres is not trivial.
[2661.10 → 2661.28] Yeah.
[2661.40 → 2661.56] Yeah.
[2661.62 → 2663.24] So, I mean, they're a super smart team.
[2663.54 → 2664.08] Super technical.
[2664.18 → 2670.24] Actually, I remember when we went in there, we had this funny feature where we would try to pull up a web browser to do authentication.
[2671.06 → 2673.44] And they actually had links installed on their system.
[2673.50 → 2673.94] Do you remember this?
[2674.00 → 2678.52] It's like a Unix terminal based like web browser that it then popped up.
[2678.60 → 2680.62] And I thought, oh, man, there's like a bug.
[2681.24 → 2681.44] Yeah.
[2681.44 → 2685.48] But anyway, so it was kind of a rough initial meeting with them.
[2685.70 → 2687.90] But they, you know, they got it working.
[2688.02 → 2690.72] And so then the whole team can, they can look at what they're doing.
[2690.72 → 2701.14] And I should say maybe the most important thing for them is that like each unit of work, kind of each thing that they try, they put it into a report, which they attach to a pull request.
[2701.14 → 2705.34] And so they can go, and they can look at kind of, and it's not like necessarily one run, right?
[2705.34 → 2710.52] It might be like, okay, you know, I tried this new thing and I tried like 10 different sets of hyperparameters.
[2710.60 → 2711.68] Like I tried a new data set.
[2711.96 → 2714.14] Like maybe there's a new camera that picked up like UV light.
[2714.94 → 2717.78] And then I tried like these 10 hyperparameters with it.
[2717.90 → 2718.84] And here's what I concluded.
[2718.94 → 2719.76] Like the camera was good.
[2719.76 → 2720.82] We should explore it further.
[2720.96 → 2724.54] And so they'll actually kind of write that all into a report and then attach it.
[2724.60 → 2728.02] And they actually put an example report that they gave to us to use for a case study.
[2728.16 → 2729.22] So it's really cool to look at.
[2729.24 → 2732.32] You can see they're trying different types of gradient descent on their data set.
[2732.50 → 2737.12] So, you know, that was like the initial case was them using it to track their experiments like that.
[2737.12 → 2743.66] But then they started to use it to look at their data sets too because they have so many different data sets, and it's constantly being collected in these fields.
[2743.66 → 2753.08] So they use our versioning system, and they attach it to our experiment tracking system to really know kind of end-to-end reproducibility of the stuff that they're deploying into tractors.
[2753.76 → 2754.12] Pretty cool.
[2754.34 → 2764.22] I guess as we start winding up, if you could wax poetic a little bit for us for a moment about kind of what you are aspiring to in terms of future of tooling.
[2764.22 → 2769.44] What are some of the things in your head that you have this vision for you would like to move into?
[2769.62 → 2772.88] You're not there yet, but you realize what a big impact it would make.
[2772.94 → 2779.56] I'd love to see kind of where the future of tooling is going because I know that will directly affect both Daniel and my lives.
[2779.74 → 2781.30] And so any insight there?
[2781.76 → 2781.92] Totally.
[2782.02 → 2788.92] I mean, what I love to do is make simple tools that really help the day-to-day lives of people trying to do practical AI.
[2788.92 → 2796.80] So I would say the thing that we haven't done that I'm kind of dying to do, but it's a huge undertaking, is stuff around production monitoring.
[2797.40 → 2807.22] You know, we do have some stuff today where we have a lot of customers use us implicitly for continuous integration, but we don't support that case explicitly yet.
[2807.60 → 2811.10] And I think that that's a big deal to, because, you know, AI safety is so important.
[2811.10 → 2817.26] And I really believe that all the ML practitioners are good people that care more than society gives them credit for AI safety.
[2817.40 → 2818.40] I actually just think it's really hard.
[2818.78 → 2822.76] And so I think these ethical issues are real, but they're hard.
[2822.96 → 2826.58] You know, and I think actually tooling can help here by showing people what's going on.
[2827.00 → 2831.44] And, you know, it's like developers, when you deploy a bad piece of code, right?
[2831.46 → 2833.84] It's like, you know, you should improve the systems.
[2833.84 → 2838.72] I think a lot of the tooling is missing for ML practitioners, and so it's dangerous, right?
[2838.80 → 2840.88] So continuous integration is a big one.
[2841.44 → 2849.40] You know, production monitoring, detecting things like model drift or data drift and things like that, you know, I think makes me nervous, should make anyone nervous.
[2850.02 → 2860.06] I think, you know, Andrej Karpathy had this really evocative talk he gave at one of Figure 8's conferences around sort of like a new IDE for ML that I keep kind of kicking around in my head where it's like,
[2860.06 → 2870.52] what would that really mean, right, to really, like, be able to tweak all the things that go into the model, like not just the hyperparameters and the code, but maybe even like the data that flows into your model.
[2870.66 → 2872.34] So those are kind of ideas I have.
[2872.58 → 2875.92] But, you know, these ideas always take forever to actually get into the world.
[2876.00 → 2876.44] So I don't know.
[2876.70 → 2877.72] I don't know what we'll get to.
[2877.88 → 2879.00] That's what we're looking for.
[2879.10 → 2880.80] Not today, but, you know, down the road.
[2880.98 → 2886.28] You know, what are people aspiring for today that they might work on in the future, you know, without commitment there?
[2886.96 → 2888.64] It's always interesting to hear that.
[2888.64 → 2889.04] Yeah.
[2889.04 → 2889.12] Yeah.
[2889.50 → 2896.50] We'll definitely link to the website of Weights and Biases and some articles and other things.
[2896.90 → 2901.42] And, of course, your awesome podcast, which people can find and listen to.
[2901.74 → 2903.88] I definitely encourage people to do that.
[2904.24 → 2910.56] It sounds like Weights and Biases has a Slack community that we can link to where you can connect with them.
[2910.92 → 2915.24] If you're having trouble finding that, you can always reach out to us as well on our Slack community.
[2915.24 → 2919.82] You can find that at changelog.com slash community or on LinkedIn or Twitter or anywhere.
[2920.40 → 2923.08] But really appreciate the insight today, Lucas.
[2923.20 → 2925.08] It's been a real joy to talk to you.
[2925.28 → 2930.30] And I'm looking forward to all the great things that will be coming from Weights and Biases.
[2930.30 → 2931.58] So thank you so much.
[2931.90 → 2932.36] Thanks so much.
[2932.42 → 2932.82] That was fun.
[2932.82 → 2933.34] Thanks so much.
[2933.34 → 2933.60] Thanks.
[2933.60 → 2947.24] If you enjoy Practical AI, we would enjoy a five-star review on Apple Podcasts, a blog post in response to something said on the show, and or a recommendation to a friend or colleague.
[2947.24 → 2952.72] those word of mouth recommendations really do make a difference practical AI is hosted by Chris
[2952.72 → 2957.74] Benson and Daniel whiten ack it is produced by jarred Santa with music by the mysterious break
[2957.74 → 2962.96] master cylinder thanks again to our partners who support this show's existence shout out to fast
[2962.96 → 2967.24] Linde and roar that's all we have for you today we'll talk to you again next week
[2977.24 → 3002.22] sorry I think you're frozen can you hear me still yeah we can just totally still
[3002.22 → 3006.36] that's amazing that's the thing about the Zoom meeting I'm like that I'm just listening
[3006.36 → 3012.68] we're just on the edge of our seat you know oh good okay you had me wrapped
[3012.68 → 3019.38] I'll try to wrap it up I'm going to like ticktock a little bit just to make sure that you say I was
[3019.38 → 3024.72] like really into your story so I was sitting still and listening the audience can't yeah we're watching
[3024.72 → 3029.00] each other on zoom we can see each other's facial expressions so it's not just audio for us as we're
[3029.00 → 3033.60] having it and yeah I think with Daniel and I were really, really still nice
[3033.60 → 3039.92] you
[3039.92 → 3040.42] you
