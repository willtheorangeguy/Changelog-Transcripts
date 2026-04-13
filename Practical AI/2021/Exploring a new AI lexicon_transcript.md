[0.00 --> 2.12]  Maybe it's the scaffolding around those terms.
[2.34 --> 4.64]  It sets people up for failure if you're saying,
[4.86 --> 10.10]  I'm going to train my artificial intelligence model
[10.10 --> 15.84]  on accelerated hardware using an optimization scheme
[15.84 --> 18.48]  of mini batch gradient descent.
[18.48 --> 22.98]  That whole sentence there just excludes so many people
[22.98 --> 24.52]  because they're just like, oh, I give up.
[24.70 --> 25.66]  You're probably right.
[25.66 --> 31.20]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[31.58 --> 32.14]  We love Linode.
[32.22 --> 33.64]  They keep it fast and simple.
[33.76 --> 36.12]  Check them out at linode.com slash changelog.
[36.36 --> 38.44]  Our bandwidth is provided by Fastly.
[38.78 --> 41.38]  Learn more at Fastly.com and get your feature flags
[41.38 --> 42.34]  powered by LaunchDarkly.
[42.60 --> 44.30]  Get a demo at launchdarkly.com.
[44.78 --> 48.18]  This episode is brought to you by our friends at Rudderstack
[48.18 --> 50.74]  and we're calling all data engineers to check out Rudderstack Cloud
[50.74 --> 52.90]  and start building smart customer data pipelines.
[53.40 --> 55.14]  Rudderstack is warehouse first.
[55.14 --> 56.48]  No more silos.
[56.80 --> 59.38]  Rudderstack builds your customer data lake on your data warehouse,
[59.52 --> 62.46]  not theirs, enabling all functionality of a CDP
[62.46 --> 65.82]  with more security and retaining full ownership of your data.
[66.16 --> 68.58]  It's open source and API first.
[68.90 --> 72.34]  Rudderstack can be easily integrated into your existing development processes
[72.34 --> 75.64]  and because they're open source, you can see all their code
[75.64 --> 78.28]  so you don't have to worry about vendor lock-in or black boxes.
[78.84 --> 80.42]  And best of all, they have transparent pricing.
[80.60 --> 82.86]  Stop paying your CDP a premium to store your data.
[82.86 --> 88.22]  Rudderstack is free up to 500,000 events and pricing scales transparently from there.
[88.64 --> 90.68]  Learn more and get started at Rudderstack.com.
[90.98 --> 93.22]  Again, Rudderstack.com.
[93.38 --> 96.92]  That's R-U-D-D-E-R-S-T-A-C-K.com.
[96.92 --> 111.74]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[112.06 --> 113.80]  productive, and accessible to everyone.
[114.14 --> 118.20]  This is where conversations around AI, machine learning, and data science happen.
[118.46 --> 121.76]  Join the community and Slack with us around various topics of the show
[121.76 --> 124.58]  at changeon.com slash community and follow us on Twitter.
[124.74 --> 126.30]  We're at Practical AI FM.
[132.30 --> 137.10]  Welcome to another fully connected episode of Practical AI,
[137.50 --> 143.44]  where Chris and I keep you fully connected with everything that's happening in the AI community.
[143.44 --> 147.94]  We'll talk a little bit about some AI news or articles,
[147.94 --> 153.38]  and we'll dig into some learning resources to help you level up your machine learning game.
[154.06 --> 156.88]  I'm Daniel Whitenack from SIL International,
[157.24 --> 161.92]  and I'm joined as always by Chris Benson, who is a strategist at Lockheed Martin.
[162.24 --> 162.92]  How are you doing, Chris?
[163.26 --> 164.56]  I am doing very well, Daniel.
[164.66 --> 166.52]  Looking forward to today's conversation.
[166.72 --> 170.64]  I always love our fully connected episodes because we can kind of go wherever we want,
[170.70 --> 171.94]  whatever captures our interest.
[171.94 --> 177.80]  Wherever we want, yeah, the no constraints, we can say whatever might pop into our minds.
[177.90 --> 179.62]  What's on your mind these days?
[179.72 --> 180.72]  How's work and life?
[181.00 --> 182.22]  Work and life is good.
[182.38 --> 187.38]  The little bit of travel lately, which has coincided with our third big wave of COVID
[187.38 --> 190.18]  as we are recording this and will release shortly.
[190.44 --> 195.38]  So other than the terror of sitting shoulder to shoulder with a bunch of people on an airplane,
[195.94 --> 199.10]  a third of which are statistically not vaccinated.
[199.10 --> 205.70]  Other than that and me trying to superglue my mask to my face around the edges, I'm doing great.
[205.88 --> 206.34]  Doing great.
[206.56 --> 207.64]  Yeah, good, good.
[207.96 --> 213.06]  Yeah, I feel like this week for me was just a tiring week, but it was like really good.
[213.18 --> 218.62]  There's a few milestones on various projects that we hit and or deadlines that came up,
[218.70 --> 219.90]  but everything went good.
[219.90 --> 227.48]  But it was just one of those weeks, you know, like you have this backlog of tasks and then everything sort of coincides in one week occasionally.
[227.82 --> 229.36]  That was this week for me.
[229.48 --> 237.90]  But thankfully, I got a good team and worked through all of that together and was able to release a couple new releases and train some new models
[237.90 --> 241.50]  and get some infrastructure things set up.
[241.50 --> 252.62]  I've been toying around with ClearML a little bit more, which we had an episode about a while back and doing some experiment tracking and queuing up jobs for GPUs and that sort of thing.
[253.00 --> 257.60]  And that's been that's been quite fun to sort of dive into their tooling for that.
[257.60 --> 259.42]  That does sound like a nice week indeed.
[259.68 --> 259.84]  Yeah.
[259.94 --> 268.94]  Otherwise, I watched Sliced the other night, which we just talked to Meg and Nick from Sliced, which is a live data science competition.
[269.28 --> 273.00]  And I watched that the other night and that was that was quite fun.
[273.20 --> 281.64]  It's just interesting to see you sort of have a stigma of certain people that like they're like a data science like hero.
[281.64 --> 293.32]  And when they sit down to code, like they're not, you know, going to Stack Overflow and they're not like doing a thing that just like barfs up a bunch of exceptions on them.
[293.46 --> 295.66]  But that's definitely not the case.
[295.66 --> 296.04]  Right.
[296.16 --> 301.70]  So it's just cool to like kind of sit back and see people live, you know, oh, I'm going to pull up Stack Overflow.
[301.84 --> 303.64]  I'm going to pull up Plotly documentation.
[303.78 --> 308.04]  Like, how do I do grouped, you know, bar plot in Plotly?
[308.18 --> 310.04]  And that's that's like the same thing I do.
[310.04 --> 314.16]  It's like whenever I hit one of those things, I just go straight to Google and, you know.
[314.36 --> 314.98]  Don't we all?
[315.10 --> 315.30]  Yeah.
[315.54 --> 325.32]  You know, the same thing on the software development side as opposed to the data science side is even the great gods of software development, just as data science, they they go through the same process.
[325.60 --> 325.78]  Yeah.
[325.98 --> 326.82]  They are human.
[327.04 --> 333.48]  Speaking of human versus AI, a couple of things have happened in recent days.
[333.48 --> 345.30]  One of these is like the next thing in like AI code generation or I guess not a next different thing, but sort of a new interface to something that we've already talked about, GitHub Copilot.
[346.00 --> 359.38]  But OpenAI released the individual, you know, access to their codex model, which is this model that does the functionality of like I'm going to write in natural language what I want my code to do.
[359.38 --> 364.74]  And then the model takes in that natural language and generates the code to do the thing.
[365.28 --> 366.48]  So they released that.
[366.66 --> 373.38]  That's one thing that's sort of interesting and thinking about like AI creating code is always interesting idea.
[374.48 --> 376.82]  I don't know if you've had any other thoughts on that recently.
[376.82 --> 385.64]  I've been having a conversation, an ongoing conversation with a good friend about no code solutions that applies to deep learning technologies as well.
[385.76 --> 389.72]  So I am keenly interested in seeing how these come together.
[389.88 --> 393.84]  I'm looking at the OpenAI codex page and where it says join the wait list.
[394.36 --> 399.62]  I noticed that it mentions that it is proficient in more than a dozen programming languages.
[399.88 --> 402.02]  Have you found any place where it actually tells you which ones?
[402.38 --> 406.34]  I haven't done as much digging on that side of things.
[406.34 --> 413.96]  I know just from my experience on Twitter and seeing what people are generating, I've seen Python, I've seen JavaScript.
[414.58 --> 417.42]  But I assume it's more than that.
[417.58 --> 422.54]  I know when GitHub Copilot released, they talked about all sorts of different programming languages.
[423.02 --> 425.76]  But yeah, I don't have any other context other than that.
[425.86 --> 428.84]  But I even saw some sort of interesting scripting.
[429.02 --> 432.36]  And one of the examples I saw was a Microsoft Word document.
[432.36 --> 437.82]  Maybe I want all of these lines re-indented a certain way or something.
[437.92 --> 439.58]  So I do it a couple of times.
[439.64 --> 442.68]  And I'm like, I don't want to do this for like 14 pages of documents.
[442.68 --> 450.22]  So they gave a little narrative of what removed spaces in this way that they said in natural language.
[450.82 --> 455.06]  And I don't know the plug-in to Microsoft Word that enabled this.
[455.06 --> 461.42]  But a little script was written and then it did the thing and re-oriented things, which is kind of a cool idea.
[461.84 --> 462.08]  It is.
[462.40 --> 464.32]  Yeah, especially for non-technical people.
[464.44 --> 466.26]  This model, it's like code generation.
[467.00 --> 473.06]  So I think the one thought is like, oh, this is for coders or technical people to aid them.
[473.22 --> 478.32]  But that example actually has an impact potentially for non-technical people.
[478.32 --> 480.02]  I'm just using a Word document.
[480.02 --> 486.90]  And actually before this thing existed, maybe I wasn't able to write cool scripts because I'm not a programmer.
[487.16 --> 504.90]  But now I can like have the superpower to like do these sort of tasks over my document or over my data that, you know, I didn't have the ability to do before because I didn't know a complicated like pivot table map function things in Excel or whatever.
[505.14 --> 507.12]  However, people do those things that don't code.
[507.12 --> 519.30]  I think we're kind of coming into this point where we're seeing these capabilities like what OpenAI is putting out and more and more these types of kind of sophisticated, let us do this for you, let us get that.
[519.48 --> 523.44]  It's bringing more and more people into this field to take advantage of it.
[523.62 --> 528.02]  If there's anything that we have seen in the last, this is where the innovation is happening right now.
[528.16 --> 536.16]  We're not seeing giant new architectures the way we did a few years ago where, you know, entirely new paradigms of deep learning architectures.
[536.16 --> 543.90]  What we're seeing now are novel ways of using it, making it more accessible to people and being able to get more productive and stuff.
[544.26 --> 550.10]  But just for the record, I'm still waiting for somebody to bring us some novel new architectures as well.
[550.18 --> 551.42]  I'm ready for some more right now.
[551.48 --> 552.58]  Just just for the record.
[552.74 --> 552.94]  Yeah.
[553.04 --> 555.44]  Anyone out there is about to release a breakthrough.
[555.80 --> 556.24]  Yeah.
[556.28 --> 557.68]  Come on the show and talk about it.
[558.02 --> 558.46]  Absolutely.
[558.76 --> 559.58]  Do it right here.
[559.68 --> 560.76]  This is the place to do it.
[560.76 --> 563.92]  We can release the show the same day as your paper.
[564.84 --> 565.68]  Yeah, that would be cool.
[565.96 --> 567.56]  It'd be cool to coordinate that at some point.
[568.06 --> 569.00]  That's a good example.
[569.50 --> 583.44]  Like AI is sort of doing this incursion or infiltration of all sorts of things that maybe we didn't anticipate before, like including Microsoft Word and scripting and Microsoft Word.
[583.44 --> 598.44]  One of the things that I wanted to bring to your attention and maybe chat through a bit today was this series of articles that the AI Now is putting together, which is a series of blog posts called A New AI Lexicon.
[598.44 --> 606.12]  And they talk about, hey, AI is having this sort of incursion into all bits of our life.
[606.36 --> 616.54]  And they talk about needing to generate narratives that can offer both perspectives from other places, but also crucial anticipatory knowledge and strategy.
[616.80 --> 625.82]  So in my mind, people might not be familiar with the term lexicon, at least before I worked for an organization that did a bunch of language stuff.
[625.82 --> 631.26]  It wasn't a term that I used very, very much, but I'm just looking at the definition here.
[631.44 --> 637.98]  And a lexicon is the vocabulary of a person, language or branch of knowledge.
[638.50 --> 646.40]  So I think when they're talking about a new AI lexicon, AI would maybe fit into this branch of knowledge category.
[647.10 --> 650.98]  And we're talking about the vocabulary of this branch of knowledge.
[651.26 --> 652.20]  For the moment, you know.
[652.38 --> 653.38]  For the moment, yeah.
[653.38 --> 661.18]  Yeah, and I think one of the hardest things for me when I was getting into this field was the jargon and vocabulary.
[661.70 --> 670.58]  Because even from a technical background, I had run across certain things like, you know, whatever it is, ordinarily squares or something.
[670.76 --> 678.32]  But the way and the jargon in which AI people or data science people talked about these things was different vocabulary and jargon.
[678.32 --> 683.34]  And so it wasn't so much that like the thing was scary or complicated.
[683.34 --> 687.60]  It was that the vocabulary actually made it scary and complicated.
[687.84 --> 689.14]  What's your experience there?
[689.14 --> 693.48]  I agree with you because language is powerful and how we label things is powerful.
[693.72 --> 695.20]  I have strong opinions there.
[695.28 --> 697.12]  We can get into them as we go forward.
[697.60 --> 705.24]  But even in the time that we've been doing the show, for those who might have been listening to us since the early days, it's evolved quite a bit.
[705.24 --> 708.20]  And so I think this is a timely topic personally.
[708.66 --> 709.28]  Yeah, for sure.
[709.44 --> 716.30]  Maybe I'll just illustrate what I'm talking about with one of these articles, which I think is a good starting point for this discussion.
[716.86 --> 719.52]  It's the article called An Electronic Brain.
[720.30 --> 723.38]  Naming, Categorizing, and the Futures of AI.
[724.00 --> 728.70]  That's a guest post by a doctoral researcher at Oxford, Yang Ao.
[728.98 --> 730.82]  Sorry if I mispronounce your name.
[731.18 --> 734.00]  But this article I thought was just fascinating.
[734.30 --> 734.86]  I did too.
[734.86 --> 740.68]  I think all of these articles, if I was to put them in a category, it would be like thought-provoking or something.
[740.98 --> 749.32]  Because I don't know, you know, reading through the bulk of them, I don't think maybe anyone could read through all of them and maybe say,
[749.48 --> 752.24]  hey, I fully agree with everything that's written here.
[752.44 --> 753.70]  That's my perspective too.
[754.14 --> 756.92]  It's different perspectives on the subject of AI, right?
[757.00 --> 759.16]  So I think it's like thought-provoking.
[759.16 --> 764.80]  It helps you sort of reformulate how you think about AI and the language that you use around AI.
[764.98 --> 771.44]  And in this article, The Electronic Brain, Yang, the author, talks about Cantonese terms.
[771.44 --> 777.56]  And the way that Cantonese terms are made up is that they're composed of a set of characters.
[778.26 --> 782.14]  And each individual character and its components have some sort of meaning.
[782.14 --> 789.68]  And so what the author did was look through various terms for things related to AI.
[789.96 --> 794.32]  So like computer, artificial intelligence, automation, etc.
[794.32 --> 810.24]  And looked at these components in the Cantonese language for sort of insights, maybe about how these terms from the Cantonese perspective might sort of shed light on how we think about AI related things.
[810.64 --> 820.08]  And by the way, just as a two second aside for anybody that is not familiar with Cantonese out there, it is the second most dominant language in China.
[820.08 --> 826.50]  Its usage lags far behind Mandarin at this point because that is the Communist Party's official language.
[826.72 --> 830.82]  But Cantonese would be the second most widely spoken language in China.
[831.10 --> 832.60]  I love language related things.
[832.76 --> 844.64]  Just to plug, if you're wanting some knowledge about like languages and their relationships and populations and all of that, you can look at the ethnologue as one good place to look for that information.
[844.64 --> 854.88]  But there's also sort of open versions that are sort of you'll see these trees of language varieties and how many people speak them and populations and all that stuff.
[855.76 --> 860.64]  The author goes through and breaks apart some of these common terms.
[860.64 --> 870.56]  So, for example, for computer, the sort of breakdown of that in terms of the characters that he brought out was called electric brain, which I don't know.
[870.62 --> 873.06]  When you look at a computer, what is your thought?
[873.30 --> 874.94]  Are you thinking electric brain?
[875.30 --> 876.24]  Indeed, I do not.
[876.60 --> 877.38]  In what way?
[877.48 --> 878.72]  I mean, is it the brain part?
[878.88 --> 880.50]  I mean, it's definitely electric, right?
[880.78 --> 881.52]  It is electric.
[881.78 --> 883.24]  You don't doubt that.
[883.32 --> 884.96]  And our brains are electric as well.
[885.34 --> 889.94]  So maybe you're saying that electric brain is redundant because brain implies electric.
[889.94 --> 893.64]  Actually, that's not where my head was at, but that is in fact true.
[894.12 --> 898.42]  They both have electrical signals in them that are core to their functionality.
[899.08 --> 902.28]  But I think that's about the limit of my analogy there.
[902.58 --> 902.74]  Yeah.
[902.92 --> 906.62]  So that's computer, which is, I think, pretty interesting.
[907.04 --> 910.48]  He gives sort of alternatives and breaks down the individual characters.
[910.48 --> 919.38]  I showed one of my colleagues the breakdown and he was seeing that, you know, computer could also maybe be like, what do you say, like meat rain or something.
[919.94 --> 924.52]  Which I don't know what that tells us about how we think about computers.
[924.52 --> 936.26]  But he goes in and he talks about, you know, these components also of how we frame the term artificial intelligence, which I think is very thought provoking for me.
[936.26 --> 950.10]  And he draws out this idea that the term itself in Cantonese and the way it's made up talks about, you could think about it sort of primarily as artificial intelligent.
[950.10 --> 973.44]  But also a sort of parallel to that that's in the language is really more focused on like manual labor or manpower and like able or a system or smart able to do manpower or manual labor, which is much more of a sort of practical idea about artificial intelligence.
[973.68 --> 974.74]  How does that strike you?
[974.74 --> 981.62]  It feels more like the feelings that we have when we say machine learning instead of artificial intelligence, you know, the way they do that.
[981.92 --> 989.50]  I think practitioners tend to think of machine learning as the pragmatic, fundamental, you know, stick with the science kind of mentality.
[989.88 --> 994.86]  Whereas AI is a little bit more glossy marketing, even though that you're speaking of the AI translation.
[995.32 --> 999.10]  It feels like that's how I would think of it as machine learning in my own context.
[999.10 --> 1023.14]  Signal Wire is real time video tech to help you create interactive video experiences previously not possible.
[1023.14 --> 1032.62]  It gives you access to broadcast quality, ultra low latency video that's proven and trusted by Amazon, Ring Doorbell, Zoom and others.
[1032.96 --> 1036.96]  See why the future of video communication is being built on Signal Wire.
[1037.26 --> 1046.60]  They have easy to deploy APIs, SDKs for the most popular programming languages and expert support from the OGs of software defined telecom tech.
[1046.60 --> 1052.64]  Try it today at SignalWire.com and use code AI for $25 in developer credit.
[1053.18 --> 1055.24]  Just visit SignalWire.com.
[1055.46 --> 1060.06]  That's SignalWire.com and use code AI to receive that 25 bucks.
[1060.42 --> 1063.84]  Once again, that's SignalWire.com, code AI.
[1063.84 --> 1084.98]  So, Chris, we were just getting into some of this discussion about how AI is represented in the Cantonese context.
[1084.98 --> 1092.92]  And starting to talk about how there is embedded within the term this idea of manual labor or something very practical.
[1093.50 --> 1093.70]  Yes.
[1093.84 --> 1116.24]  One of the things that's mentioned in this article is thinking about, you know, what if these systems, what if AI systems or automated systems or augmented systems, what if these systems were seen less exceptional or very sophisticated or whatever that term is and more ordinary or less exceptional?
[1116.36 --> 1120.00]  You don't want to take me down this path because I have strong opinions on this one.
[1120.12 --> 1121.24]  You don't want to do that, do you?
[1121.24 --> 1121.60]  Yeah.
[1121.60 --> 1121.64]  Yeah.
[1121.74 --> 1133.00]  So, there's like the things that he draws out are more ordinary and less exceptional or more human and less machine, more labor and less enchantment.
[1133.20 --> 1136.08]  I thought that was a cool like a pairing of terms.
[1136.30 --> 1148.88]  So, like there is this perception, maybe not by the practitioner like you were talking about, but definitely by people at large that AI systems have some sort of enchantment around them.
[1148.88 --> 1149.44]  Yeah.
[1149.44 --> 1161.56]  When I'm teaching classes, I think oftentimes when I get into like, okay, well, if we think about most AI systems, and there's certainly exceptions that don't fit into this pattern that I'm about to say.
[1161.56 --> 1168.32]  But if we think about most AI systems, what we're talking about is essentially an automated process of trial and error.
[1168.72 --> 1171.24]  It's actually a very dumb process, right?
[1171.42 --> 1174.60]  In the sense that we have a set of examples.
[1174.60 --> 1179.64]  We're trying to recreate the data transformation from that input to an output.
[1180.02 --> 1184.02]  And the way in which we do it is we try a bunch of times.
[1184.38 --> 1185.42]  So, we put the examples in.
[1185.54 --> 1189.50]  We try to make the prediction based on some encoded parameters.
[1189.50 --> 1192.06]  And when it's not good, we change the parameters.
[1192.06 --> 1199.42]  And then we just do that a bajillion times until we get the right set or the, quote, best set of parameters.
[1199.68 --> 1207.20]  And then out comes the model, which so many people see as enchantment or like you put fairy dust on the computer in the corner.
[1207.20 --> 1214.52]  And, you know, I see some faces in training sometimes where it's like, oh, it's a little bit disappointing for people.
[1214.74 --> 1231.04]  In other ways, it's like maybe reassuring because they came into it thinking it's harder to get into this practice than they thought because there's some like fundamentally subtle and mysterious thing that they need to understand in order to do the work.
[1231.38 --> 1232.88]  Daniel, they hear it's a black box.
[1233.48 --> 1234.88]  It's a black box.
[1234.94 --> 1235.60]  It's magical.
[1235.60 --> 1237.38]  Well, this is their way into Hogwarts.
[1237.76 --> 1239.74]  There's another term, black box, right?
[1239.80 --> 1240.06]  It is.
[1240.10 --> 1244.34]  What does that terminology imply about how we think about?
[1244.64 --> 1249.02]  At least I don't know how people are thinking about it now, but early on it was it's unknowable.
[1249.80 --> 1249.94]  Yeah.
[1249.94 --> 1253.62]  And that was really before the rise of explainable AI as a field.
[1254.20 --> 1254.36]  Yeah.
[1254.48 --> 1260.22]  I mean, that's what black box was intended to be is this is unknowable what we're doing here, which, of course, is a little bit silly.
[1260.22 --> 1260.64]  Yeah.
[1260.64 --> 1274.50]  And there's also this very unfortunate connotation with black, just meaning it does have a negative connotation in the context of like most of the times these terms that people have used through time, like a black list or something.
[1274.50 --> 1274.90]  Yeah.
[1274.90 --> 1287.26]  Which now we're sort of trying to get away from those terms because we definitely don't want that connotation in many cases with like black shouldn't have this sort of preexisting negative connotation.
[1287.26 --> 1294.52]  And so when you say black box, there's like this part of part of that term is like this unknowingness about it.
[1294.66 --> 1306.30]  But from the start, at least in our culture, you also get this sense of maybe you're trying to say something, something negative about the AI thing, that it's black box.
[1306.62 --> 1311.22]  It's unknowing, but maybe in an unknowing, threatening sort of way.
[1311.22 --> 1317.64]  There has always been kind of a mysticism around the term artificial intelligence or AI.
[1317.88 --> 1322.70]  And frankly, there have been many marketers out there who have taken great advantage of that.
[1322.84 --> 1328.06]  But what we do, the deep learning techniques that we do is just mathematics.
[1328.18 --> 1330.18]  And it's very, very pragmatic.
[1330.46 --> 1333.94]  It's very down to earth and there's nothing mystical about it.
[1334.06 --> 1336.66]  So I think that's one of the places I've arrived.
[1336.66 --> 1344.68]  When we started the show and named our show Practical AI, I was probably pretty high on the term AI then.
[1344.84 --> 1353.26]  But as we have really delved into this and the black box nature of the math has changed, it's hard for me to think of it as, I certainly don't think of it as intelligent.
[1353.38 --> 1355.48]  It's hard for me to even think of it as AI at this point.
[1355.60 --> 1361.62]  So I think my term AI has gotten more aspirational as we've gone on, meaning that we have not yet achieved it.
[1361.62 --> 1366.64]  Yeah, it's this system or machinery like was talking about in that.
[1366.66 --> 1378.12]  Sort of breakdown of the Cantonese, the system or machinery that is doing some kind of man or woman related power labor.
[1378.82 --> 1383.32]  And so, yeah, I think that's a very practical way to look at it.
[1383.32 --> 1394.18]  And I know in the past, you know, just speaking of lexicons and how we talk about AI, even this recent episode where we chatted with the people from Slice.
[1394.18 --> 1397.54]  So Meg and Nick, I already mentioned I've been watching that.
[1397.96 --> 1402.52]  The sort of premise of that show was their concept around Chopped, the cooking show.
[1402.52 --> 1408.56]  And I found it very interesting that that's also in my lexicon of AI terms.
[1409.04 --> 1424.52]  That's very much how I think about actual AI development and the practicalities of AI development is much more like cooking than it is this sort of like pure research topic of people standing at a chalkboard and doing various things.
[1424.52 --> 1436.44]  And so that in the spirit of what AI now is trying to do, you know, I would think that, for example, like a recipe is a good term to have in an AI lexicon.
[1436.68 --> 1437.02]  I agree.
[1437.02 --> 1453.34]  It's not because even like if you think about a model, model has certain connotations, especially for people that aren't like deeply rooted in maybe scientific discipline like physics or chemistry or mathematical simulations.
[1453.98 --> 1459.36]  They may think that that model term is also quite intimidating.
[1459.36 --> 1465.38]  But this is another maybe earth shattering thing for people when I'm doing trainings is, you know, a model.
[1465.72 --> 1466.38]  What is a model?
[1466.38 --> 1473.24]  Well, maybe I'll ask you, Chris, if someone was to ask you, what is an AI model at its core?
[1473.44 --> 1479.62]  Like when you get your magnifying glass and you look at the AI model, what is it composed of?
[1479.70 --> 1481.70]  I guess maybe it's another way.
[1482.06 --> 1484.00]  Well, the composed of threw me off a little bit.
[1484.08 --> 1494.30]  I mean, I think of a model in a generically, and this isn't specific necessarily to deep learning, but as a representation of an entity that is real in some sense.
[1494.30 --> 1496.14]  That doesn't mean it necessarily is physical.
[1496.48 --> 1496.66]  Yeah.
[1496.74 --> 1498.82]  It represents the characteristics and stuff.
[1498.82 --> 1508.10]  But really, I mean, when we talk about a model in the context of deep learning and we're producing a model at the end, we love to talk about, you know, the word inference and such.
[1508.10 --> 1509.92]  But I think of it as a filter, honestly.
[1510.12 --> 1510.34]  Yeah.
[1510.46 --> 1511.18]  Type of filter.
[1511.48 --> 1518.40]  And so you give it an input and it is arrived as a set function that produces an output based on that input.
[1518.40 --> 1525.42]  And until you change the model with further training, it's a filter that gives you a particular set of outputs.
[1525.58 --> 1527.60]  And that's down to earth the way I think about it.
[1527.86 --> 1529.16]  I like the filter idea.
[1529.44 --> 1533.52]  I think that's something that people can grab onto in terms of their lexicon.
[1533.74 --> 1536.92]  Like everyone's interacted with a coffee filter, right?
[1537.18 --> 1537.36]  Yeah.
[1537.36 --> 1542.36]  Or at least in most cultures, there's some idea of that sort of filtering or straining.
[1542.36 --> 1549.16]  And also like a data transformation, I think, is a less scary terminology than model.
[1549.58 --> 1560.86]  But when I am teaching, oftentimes I'll ask this question and there's a bunch of ideas about like, oh, it's like a thing that mimics human brains.
[1560.86 --> 1566.00]  Or it's like this, like very enchanted ideas of models, right?
[1566.38 --> 1572.02]  And eventually I break them down and I say, here's what a model is.
[1572.30 --> 1574.66]  Oh, I thought you were breaking the person down for a moment there.
[1574.74 --> 1576.30]  You're breaking the model explanation.
[1576.46 --> 1578.30]  I was like, here comes Daniel, you know?
[1578.48 --> 1578.66]  Yeah.
[1578.72 --> 1585.56]  So eventually if you get down to the roots of it and you say, hey, so you have a Jupyter notebook, right?
[1585.58 --> 1587.12]  And you trained a model.
[1587.28 --> 1588.96]  Which bit of that code is the model?
[1588.96 --> 1591.64]  Well, I mean, there's some definitions.
[1592.00 --> 1595.14]  There's a function or a class that defines your model, right?
[1595.86 --> 1599.40]  But then at the end, you, quote, save your model, right?
[1599.42 --> 1600.98]  Because you want to use your model later.
[1601.54 --> 1604.56]  So if you save your model, what is save?
[1604.76 --> 1610.00]  It's not sort of like spoken into reality with some incantation, right?
[1610.10 --> 1610.24]  Yeah.
[1610.38 --> 1612.70]  Like you're saving numbers, right?
[1612.82 --> 1613.20]  You are.
[1613.30 --> 1615.88]  What you're doing is you're serializing a bunch of parameters.
[1615.88 --> 1622.44]  And the model in my mind is the parameters that you save, which are just numbers.
[1622.78 --> 1624.36]  It's a static snapshot.
[1624.80 --> 1624.98]  Yeah.
[1625.10 --> 1631.18]  Like a class or a function that defines how to use those numbers to either filter something
[1631.18 --> 1637.60]  like you're talking about, to filter it, to transform data, to produce certain types
[1637.60 --> 1638.28]  of outputs.
[1638.28 --> 1641.58]  It's really just a parameterized function, right?
[1641.58 --> 1645.72]  And the parameters plus the definition of that function is your model.
[1646.00 --> 1648.52]  There's no sort of like beyond that in my mind.
[1648.60 --> 1649.98]  Now, there's certainly like-
[1649.98 --> 1650.46]  I agree with you.
[1650.54 --> 1653.30]  Other terms, like these terms like meta learning.
[1653.62 --> 1655.96]  Oh, that's like super meta, right?
[1656.64 --> 1658.26]  How many thousands of people though?
[1658.32 --> 1660.04]  You just took the enchantment right out of it.
[1660.10 --> 1661.00]  The whole mysticism.
[1661.22 --> 1661.34]  Yeah.
[1661.38 --> 1662.90]  I've destroyed lots of-
[1662.90 --> 1666.70]  There are thousands of listeners out there that are going to turn away from this field
[1666.70 --> 1667.06]  now.
[1667.70 --> 1669.02]  You've demystified it.
[1669.08 --> 1670.56]  You have taken the magic from it.
[1670.56 --> 1671.66]  It's no longer Hogwarts.
[1671.78 --> 1672.76]  We're all muggles still.
[1674.74 --> 1679.32]  Maybe we need some terminology from Harry Potter and our AI lexicon.
[1679.76 --> 1680.16]  Excellent.
[1680.32 --> 1681.12]  I could do with that.
[1681.32 --> 1687.14]  I don't know if that crosses all cultures, but that gets to the idea that some of these
[1687.14 --> 1693.16]  terms just from the start, like artificial intelligence model, gradient descent, and that's
[1693.16 --> 1696.28]  not a bad term for the method of optimization, right?
[1696.34 --> 1698.16]  It's actually a very appropriate term.
[1698.32 --> 1699.28]  Very accurate, actually.
[1699.28 --> 1702.20]  I don't have a problem with that one because I think it describes what you're doing.
[1702.62 --> 1702.74]  Right.
[1702.88 --> 1706.40]  It definitely is a, can be a scary term though.
[1706.66 --> 1711.08]  It's like stochastic gradient descent or mini batch gradient descent.
[1711.56 --> 1716.86]  So maybe it's the scaffolding around those terms that like it sets people up for failure.
[1716.86 --> 1726.96]  If you're saying I'm going to train my artificial intelligence model on accelerated hardware using
[1726.96 --> 1731.28]  an optimization scheme of mini batch gradient descent.
[1731.48 --> 1731.58]  Yes.
[1731.70 --> 1737.30]  That whole like sentence there is like just excludes so many people because they're just
[1737.30 --> 1738.26]  like, oh, I give up.
[1738.38 --> 1739.46]  You're probably right.
[1739.46 --> 1744.48]  And then on the opposite thing without going that way, going for the cheap thing that doesn't
[1744.48 --> 1745.32]  represent it well.
[1745.52 --> 1752.00]  I think maybe, maybe the term, the description that just makes me cringe more than any other
[1752.00 --> 1754.38]  is the use of the word cognitive.
[1754.38 --> 1755.46]  Oh, cognitive.
[1755.74 --> 1755.88]  Yeah.
[1755.88 --> 1757.50]  That's really gotten popular.
[1757.96 --> 1761.84]  Oh, and I just, oh, if you're going to talk to me about.
[1761.84 --> 1762.04]  Yeah.
[1762.16 --> 1764.72]  The electronic brain sort of idea.
[1764.90 --> 1765.18]  Yeah.
[1765.40 --> 1770.04]  If we're talking deep learning, don't talk to me about cognitive because I will turn off
[1770.04 --> 1770.74]  right away.
[1770.84 --> 1772.82]  I'll be like, this person doesn't know what they're talking about.
[1772.82 --> 1778.42]  I also listened to the NLP highlights podcast from the Allen NLP group.
[1778.90 --> 1778.98]  Yeah.
[1778.98 --> 1784.62]  And their recent episode was really relevant to this topic because they were talking about
[1784.62 --> 1792.32]  language models and how they process language data versus like a human cognitively processes
[1792.32 --> 1793.06]  language.
[1793.06 --> 1802.12]  And actually, this is like very much like a huge area of research, which is not very well
[1802.12 --> 1803.44]  defined at this point.
[1803.62 --> 1808.78]  And even just thinking about the guest on the show, her name is Lisa Bainborn.
[1808.98 --> 1814.62]  And she did this work where she tried to match up certain layers of a neural network or operations
[1814.62 --> 1821.04]  in a neural network like attention with cognitive signals from doing imaging of brains to see
[1821.04 --> 1826.92]  if there was sort of a similarity with how a brain process this information versus like
[1826.92 --> 1831.24]  a computer processes this through a modern language model.
[1831.72 --> 1837.92]  And she talks about how it was very hard for her to find any signal that had that sort of
[1837.92 --> 1838.42]  correlation.
[1838.78 --> 1845.02]  And eventually she found some like metrics within the world of machine learning interpretability
[1845.02 --> 1849.26]  that matched up a bit with the cognitive signals.
[1849.26 --> 1852.72]  But it was very, very far from a clear cut.
[1853.36 --> 1857.26]  So I would recommend people, you know, look at we'll include the link in our show notes.
[1857.26 --> 1862.14]  But if you're interested in hearing that discussion, yeah, this idea of matching up neural networks
[1862.14 --> 1868.04]  with cognitive things is very interesting and definitely an area of active research.
[1868.46 --> 1873.08]  We've talked about a number of these terms in our AI lexicon.
[1873.08 --> 1880.06]  And that's definitely one way to think about what AI now is doing with their series in this
[1880.06 --> 1881.12]  AI lexicon.
[1881.12 --> 1889.60]  But they're also kind of exploring various subjects that are thought provoking around how AI models
[1889.60 --> 1896.10]  behave, not just how we describe them, but how we describe their behavior and also think about
[1896.10 --> 1898.28]  how they behave and interact with humans.
[1898.46 --> 1905.22]  For example, they talk about those words smart, like we talk about like a smart fridge or a smart
[1905.22 --> 1906.48]  home or a smart city.
[1906.88 --> 1910.30]  What does it fundamentally mean that a thing is smart?
[1910.48 --> 1910.78]  I don't know.
[1910.86 --> 1912.24]  Maybe that's another question to you.
[1912.46 --> 1912.48]  What?
[1912.78 --> 1914.88]  Oh, that puts it right up there with cognitive with me.
[1915.08 --> 1915.64]  Yeah, yeah.
[1915.76 --> 1917.86]  It's one of those words that's alluding.
[1917.98 --> 1918.90]  It's a marketing thing.
[1918.90 --> 1924.82]  It's alluding to this thing, as you just pointed out before the break, doesn't often show itself
[1924.82 --> 1925.58]  to be a reality.
[1925.90 --> 1925.98]  Yeah.
[1926.10 --> 1931.82]  And they talk about, you know, this is maybe driven by claims of technology companies to
[1931.82 --> 1935.64]  drive marketing in various ways.
[1935.78 --> 1940.38]  And in some ways, it's harmful because people want their stuff to be smart, right?
[1940.38 --> 1943.40]  But they don't think about like, where is this data going?
[1943.98 --> 1946.60]  What risk does this expose me to?
[1946.70 --> 1952.48]  Which we've definitely seen some issues with that over time in terms of IoT and smart devices
[1952.48 --> 1955.26]  and security and all of those things.
[1955.54 --> 1959.40]  You know, that's a great point is that when you see smart something, you know, the something
[1959.40 --> 1962.60]  was already an existing thing and then they add smart to it.
[1963.04 --> 1965.82]  And it rather implies that something has changed.
[1966.00 --> 1972.28]  And usually that something that has changed is the use of data in some way, which begs all
[1972.28 --> 1976.20]  these questions that not only are we asking now, but we've talked about over many episodes.
[1976.90 --> 1980.32]  But the consumer isn't necessarily data savvy.
[1980.60 --> 1984.88]  They're not necessarily familiar with these technologies that we and our listeners are talking
[1984.88 --> 1986.28]  about week in and week out.
[1986.40 --> 1987.70]  So there's a danger there.
[1987.70 --> 1991.46]  There's a danger of what are you opening yourself to in the name of smart?
[1991.46 --> 1996.70]  I think a similar thing, maybe related to the smart discussion, they talk about function
[1996.70 --> 1997.14]  creep.
[1997.34 --> 1997.44]  Yep.
[1997.66 --> 2003.10]  I know also people use the term model drift and other things that that's a kind of separate
[2003.10 --> 2009.76]  idea where the function you're so model drift is when the functionality that you're doing
[2009.76 --> 2015.82]  with your model initially matches the distribution of the data that you're putting into your model.
[2015.82 --> 2018.68]  But eventually that distribution of data actually changes.
[2019.50 --> 2023.04]  And so your model may behave in sort of interesting, weird ways.
[2023.56 --> 2029.40]  But also you could think about function creep or function drift, which is, hey, we created this
[2029.40 --> 2033.54]  facial recognition model to do X thing.
[2033.54 --> 2042.52]  Maybe it's to ensure that people are identified securely when they enter a building or something.
[2042.86 --> 2042.88]  Right.
[2042.94 --> 2045.90]  But then that's pretty easily, you know, COVID happens.
[2046.00 --> 2050.98]  And then you can say, well, it's also a really good way to see if people are wearing their masks
[2050.98 --> 2059.64]  or, you know, do some type of more analytical analysis of this in a sort of surveillance type
[2059.64 --> 2060.56]  of way.
[2060.96 --> 2062.86]  And that happens a lot as well.
[2063.12 --> 2063.36]  Yeah.
[2063.46 --> 2065.00]  What do you think that's driven by?
[2065.32 --> 2069.18]  What is the thought process and the discussions behind the scene when that happens?
[2069.36 --> 2073.36]  I think things that I've observed as people go, well, it costs us nothing extra.
[2073.50 --> 2077.32]  The model we have for purpose A will actually serve purpose B as well.
[2077.32 --> 2082.88]  The decision to ever create the model was only analyzed against the circumstances around
[2082.88 --> 2083.18]  A.
[2083.38 --> 2089.54]  And so it's a way of circumventing many of the due diligence processes, in some cases,
[2089.64 --> 2091.96]  maybe even ethical considerations that are there.
[2092.16 --> 2092.26]  Yeah.
[2092.32 --> 2093.52]  I think that happens quite a lot.
[2093.74 --> 2101.52]  Also, there's a lot of companies that provide AI tooling, but they're not the end user of that.
[2101.66 --> 2101.82]  Right.
[2101.82 --> 2108.90]  So let's say that I'm a company and I'm doing facial recognition technology and I provide
[2108.90 --> 2114.20]  an API or some tool for companies to do facial recognition and I release this to them.
[2114.72 --> 2120.86]  How could I ever understand how they're actually using this or how my technology is actually being
[2120.86 --> 2121.26]  used?
[2121.42 --> 2124.02]  And maybe in terms of this function creep idea.
[2124.02 --> 2130.98]  Is there any mechanism to monitor that or to help understand how people are using the
[2130.98 --> 2134.26]  things that you're creating, specifically AI models?
[2134.62 --> 2138.12]  Yeah, I don't think there's any standard approach that I'm aware of, at least.
[2138.26 --> 2140.64]  This reminds me, it's not exact, but it's close.
[2141.14 --> 2146.84]  A year or two ago, we were talking about how AWS was offering facial recognition services
[2146.84 --> 2148.82]  to law enforcement agencies.
[2149.40 --> 2152.88]  And there were some civil liberty concerns around that.
[2152.88 --> 2157.02]  And I believe AWS ended up pulling back from that as offering it.
[2157.28 --> 2164.12]  But the point is, is that AWS may not have felt as a service provider that they needed
[2164.12 --> 2165.14]  to evaluate that.
[2165.24 --> 2170.98]  But if you're talking about a tool that can be used in ways that may not be strictly ethical
[2170.98 --> 2176.26]  in every context, then there's a big question mark hanging over that entire thing is what
[2176.26 --> 2179.50]  are your responsibilities when you release such a capability to the public?
[2179.50 --> 2185.68]  I mean, at the end of the day, you can't have total control over what your end users do with
[2185.68 --> 2186.50]  their thing.
[2186.62 --> 2194.76]  Because at the end of the day, humans are tricky and deceptive and all of those things in various
[2194.76 --> 2195.32]  scenarios.
[2195.84 --> 2201.30]  I think you can, maybe this gets to the principles and how you structure your licenses and that
[2201.30 --> 2202.84]  sort of thing as a provider.
[2202.84 --> 2209.42]  For example, I know there's well accepted and widely used guidance from the United Nations
[2209.42 --> 2215.28]  around malicious use of technology to oppress indigenous populations.
[2215.72 --> 2215.82]  Right.
[2215.92 --> 2221.86]  And so this is language that you can include in like licenses that you sign with, with companies.
[2221.86 --> 2227.32]  And certainly like a license and their company signing, you know, a license on that doesn't
[2227.32 --> 2231.46]  mean that they won't do that or oppress some population or something like that.
[2231.68 --> 2234.18]  It's a self-regulatory kind of approach.
[2234.42 --> 2234.74]  Yeah.
[2235.14 --> 2240.94]  But at least there is a precedent to where like, if you are aware that something like this
[2240.94 --> 2247.14]  is going on, then, you know, you have in your license an agreement that allows you to, you
[2247.14 --> 2254.18]  know, terminate things or recoup costs that maybe you could push back to that population
[2254.18 --> 2258.00]  or what, you know, whatever the thing is, there could be a mechanism around it.
[2258.08 --> 2262.38]  But if you don't have that, then like, hey, you're just not thinking about it up front.
[2262.54 --> 2264.52]  That's maybe a poor excuse.
[2264.52 --> 2268.62]  Like, I didn't think about the scenario where this could be used in this way.
[2268.62 --> 2274.04]  I think that draws inspiration from the software world because, you know, often we see software
[2274.04 --> 2277.98]  licenses, including open source licenses that start with a particular intent.
[2278.18 --> 2283.14]  And it's not until you figure out whether or not that is appropriate for the situation.
[2283.56 --> 2284.68]  And there's some learning there.
[2285.04 --> 2289.92]  There's a whole variety of these articles, which I would recommend, you know, people check
[2289.92 --> 2290.26]  out.
[2290.70 --> 2296.94]  There's new terms in there that, you know, me as a technical person and not, you know, not
[2296.94 --> 2299.88]  having taken an English class since high school.
[2300.14 --> 2305.74]  I wasn't familiar with, but it was good to learn about those things and glad to see people
[2305.74 --> 2309.80]  writing these sort of thought provoking articles in this way.
[2309.96 --> 2314.16]  So we'll include links to a number of these and the series in our show notes.
[2314.16 --> 2315.42]  So definitely check it out.
[2315.96 --> 2320.62]  But one of the things that we like to do on these fully connected shows is share with people
[2320.62 --> 2323.02]  some learning resources that we've run across.
[2323.02 --> 2326.64]  Because as you mentioned, Chris, things are moving so rapidly.
[2327.32 --> 2330.86]  People use all sorts of fancy jargon, which is confusing.
[2331.16 --> 2335.96]  So having a good set of resources to turn to is really important.
[2336.32 --> 2341.38]  One of the ones that I found, actually, I don't know if it was yesterday or today, was a new
[2341.38 --> 2349.52]  free book, PDF book that's posted onto Archive from Jeff Heaton, who's teaching a course at
[2349.52 --> 2355.50]  Washington University in St. Louis entitled Applications of Deep Learning.
[2355.88 --> 2360.28]  And you can just go straight to the archive and download the PDF.
[2360.92 --> 2365.90]  I was really impressed with my initial inspection of this resource.
[2365.90 --> 2368.84]  So it's Applications of Deep Neural Networks with Keras.
[2368.84 --> 2377.22]  And it seems like there's this sort of very consistent and practical treatment of everything
[2377.22 --> 2385.20]  from kind of preliminaries of how to read in a CSV file through to like, how do I interact
[2385.20 --> 2387.58]  with TensorFlow to do various things?
[2387.94 --> 2393.96]  All the way down to like reinforcement learning and setting up environments for reinforcement
[2393.96 --> 2394.42]  learning.
[2394.42 --> 2400.72]  And all of this is treated seemingly, you know, very consistently with Keras and very
[2400.72 --> 2402.96]  much in a code first sort of way.
[2403.08 --> 2407.72]  So as soon as you start scrolling through the book, you'll see very explicit sections, which
[2407.72 --> 2413.30]  are, hey, here is the Python code that does this thing.
[2413.32 --> 2416.80]  And here is the expected output from that Python code.
[2416.94 --> 2421.58]  And of course, there's, you know, equations and figures and stuff in there as well.
[2421.58 --> 2427.56]  But I like that there's this very clear call out of how this is code based, how it's all
[2427.56 --> 2428.40]  with Keras.
[2428.76 --> 2433.02]  I haven't gone through the whole thing, obviously, since I just found it in the last couple of
[2433.02 --> 2433.32]  days.
[2433.44 --> 2435.10]  But I know I'll use it as a reference.
[2435.10 --> 2439.52]  But I think it would also be a good alternative for people that are out there maybe thinking,
[2440.04 --> 2445.30]  hey, what is that sort of comprehensive resource that I could turn to to really get into this
[2445.30 --> 2445.74]  field?
[2445.74 --> 2451.28]  And maybe starting with a little bit of Python knowledge, work into some of these more complicated
[2451.28 --> 2458.18]  topics like adversarial networks or convolutional neural networks or other things with TensorFlow
[2458.18 --> 2458.92]  and Keras.
[2459.06 --> 2464.12]  I think this would be a really good one to check out and maybe include in your list of things
[2464.12 --> 2464.82]  to work through.
[2465.12 --> 2465.52]  I agree.
[2465.66 --> 2468.06]  And I was not aware of this until you mentioned it just now.
[2468.08 --> 2471.22]  And I downloaded it as you were talking and looking through it.
[2471.26 --> 2472.20]  It's very current.
[2472.20 --> 2476.76]  It's fall of 2021 and we're in August of 2021 as we're recording this.
[2477.26 --> 2480.96]  So it's a recent resource and I'm looking through it and it looks fantastic.
[2481.28 --> 2482.80]  Yeah, it's like 500 pages.
[2483.28 --> 2483.66]  Oh, yeah.
[2483.66 --> 2484.70]  It's huge.
[2484.88 --> 2486.34]  And it covers so many great topics.
[2486.56 --> 2487.46]  So yeah, thank you.
[2487.54 --> 2490.48]  I'm going to be going through this after we stop recording this episode.
[2490.80 --> 2493.08]  There's definitely other ones that take this approach.
[2493.24 --> 2498.40]  Like I'm thinking of this dive into deep learning resource that is very comprehensive, but also
[2498.40 --> 2501.06]  very much code based and provides code examples.
[2501.06 --> 2505.34]  And I think this is really useful because you get your hands on very quickly and are
[2505.34 --> 2507.98]  able to explore things very rapidly.
[2508.78 --> 2510.62]  So yeah, definitely check it out.
[2511.00 --> 2512.02]  August 10th, two days.
[2512.10 --> 2514.26]  As we record this, it was released two days ago.
[2514.44 --> 2515.12]  Oh, look at that.
[2515.22 --> 2519.08]  I'm really on top of Twitter here.
[2519.68 --> 2521.00]  People must have liked it on Twitter.
[2521.16 --> 2522.28]  It got into my feed.
[2522.46 --> 2523.50]  So thank you, Jeff Heaton.
[2523.68 --> 2528.44]  If you're listening, come on to the show sometime and talk to us about how the class went.
[2528.56 --> 2528.96]  Absolutely.
[2529.34 --> 2530.42]  We'd love to hear about it.
[2530.42 --> 2536.34]  If you're interested in these sorts of resources or topics that we talk about on the show,
[2536.68 --> 2539.58]  maybe check out our community at Practical AI.
[2539.86 --> 2544.52]  You can join a Slack channel where there's discussions on these sorts of resources and
[2544.52 --> 2545.28]  other things.
[2545.48 --> 2548.26]  You can find that at changelog.com slash community.
[2548.70 --> 2551.16]  We're on LinkedIn and Twitter and other places.
[2551.58 --> 2555.94]  So find us and let us know what you're thinking about the show and start some discussion around
[2555.94 --> 2557.30]  various AI topics.
[2557.30 --> 2561.60]  I really enjoyed today's conversation, Chris, talking about words and what they mean.
[2561.84 --> 2562.22]  I did too.
[2562.28 --> 2562.82]  It's fascinating.
[2563.08 --> 2567.56]  And for me as a participant, and I'm just absorbed already in this book.
[2567.66 --> 2569.58]  You've lost my attention, Daniel, because I'm...
[2569.58 --> 2570.62]  I've totally lost you.
[2570.88 --> 2571.06]  Yeah.
[2571.16 --> 2572.80]  I'm totally into the book now.
[2572.98 --> 2574.28]  So yeah, go download it, everyone.
[2574.40 --> 2576.30]  It's free out there on the archive.
[2576.30 --> 2577.30]  So cool.
[2577.50 --> 2578.04]  Great show.
[2578.24 --> 2578.38]  Yeah.
[2578.50 --> 2578.92]  Thanks, Chris.
[2579.02 --> 2579.28]  See ya.
[2579.40 --> 2579.72]  See you later.
[2582.78 --> 2585.22]  Thank you for listening to Practical AI.
[2585.62 --> 2590.96]  We have a bundle of awesome podcasts for you at changelog.com, including our brand new
[2590.96 --> 2596.54]  show, Ship It with Gerhard Lezou, a podcast about getting your best ideas into the world
[2596.54 --> 2597.78]  and seeing what happens.
[2598.12 --> 2602.02]  It's about the code, the ops, the infra, and the people that make it happen.
[2602.02 --> 2606.06]  Yes, we focus on the people because everything else is an implementation detail.
[2606.40 --> 2611.10]  Subscribe now at changelog.com slash ship it or simply search for Ship It and your favorite
[2611.10 --> 2611.76]  podcast app.
[2611.84 --> 2612.34]  You'll find it.
[2612.48 --> 2615.74]  Of course, the galaxy brain move is to subscribe to our master feed.
[2615.86 --> 2621.10]  It's all changelog podcasts, including Practical AI and Ship It in one place.
[2621.54 --> 2626.20]  Search changelog master feed or head to changelog.com slash master and subscribe today.
[2626.58 --> 2631.38]  Practical AI is hosted by Daniel Whitenack and Chris Benson with music by Breakmaster Cylinder.
[2631.38 --> 2634.12]  We're brought to you by Fastly, LaunchDarkly, and Linode.
[2634.42 --> 2635.12]  That's all for now.
[2635.34 --> 2636.28]  We'll talk to you again next week.
[2661.38 --> 2665.38]  Game on.
[2665.38 --> 2665.50]  Game on.
