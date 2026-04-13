[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.14] on Linde servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.14 → 23.48] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.48 → 28.94] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[28.94 → 34.50] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[34.98 → 42.44] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.44 → 51.06] DigitalOcean and try it today for free. Head to do.co slash Changelog. Once again, do.co slash Changelog.
[58.94 → 68.78] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.20 → 74.68] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.74 → 78.82] and data science happen. Join the community and slack with us around various topics of the show
[78.82 → 84.64] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[88.94 → 97.88] Welcome to Practical AI. I'm joined by my co-host, Chris Benson, who is a digital transformation and
[97.88 → 105.02] AI specialist. And I'm Daniel Whiten ack. I'm working in AI for good. And we're going to do another news
[105.02 → 110.52] and updates and learning resources episode for everyone. I think there's been a pretty good
[110.52 → 118.22] response on that. There's a lot of news to keep up with in the AI world. And always great to have a few
[118.22 → 124.08] more learning resources at your fingertips. So, hey, Chris, how are you doing? I'm doing pretty good. I'm excited
[124.08 → 129.78] about it. We got some cool stuff to talk about this week. Yeah, for sure. As always, there's surprising
[129.78 → 136.50] things each week and things that, you know, are sometimes expected. But yeah, it's always exciting
[136.50 → 143.08] regardless. Absolutely. So what have you seen this last week? Yeah, the first one that came across
[143.08 → 150.44] my path was this survey that O'Reilly did called the state of machine learning adoption in the
[150.44 → 156.60] enterprise. And they have, you know, they have a blog post about it. But then you can actually
[156.60 → 161.36] download the full report. You know, I think you have to put in your email or whatever to download
[161.36 → 167.14] it. But it's its free. And it is pretty interesting if you're working, you know, in particular
[167.14 → 174.54] at a larger company and interested to know, you know, kind of how the landscape of machine
[174.54 → 179.74] learning is playing out in larger companies. I think it's really relevant. They ask a bunch of
[179.74 → 185.08] different questions, everything from, you know, what people's titles are, you know, where they're
[185.08 → 191.24] located. But also, I think some interesting things, the one that piqued my interest was actually who's
[191.24 → 196.88] building the machine learning models within an enterprise company, the biggest percentage
[196.88 → 204.02] of that were kind of embedded data science teams. But then it kind of went down the percentages from
[204.02 → 210.52] there through external consultants, all the way down to cloud ML services. And I was actually pretty
[210.52 → 217.52] surprised. There was only like 3% of people using cloud ML services, or at least that's how I read
[217.52 → 222.72] the information. Really? And that that was actually astounding to me. I don't I don't know if
[222.72 → 226.08] you have thoughts on that. I thought I would have expected that to be much higher just because it's
[226.08 → 232.00] so easy to use these services. You know, maybe that's because we're in our little AI bubble,
[232.00 → 238.16] and we think about this and, you know, acting in it all the time. But I admit is, you know, we're hearing
[238.16 → 243.80] constantly from these cloud providers about their services. And I guess I'm a bit surprised to that,
[243.80 → 250.78] that it's not a higher uptake. Yeah, I don't know. I mean, I think for anyone out there that in
[250.78 → 257.36] particular, if you're maybe in a software engineering role, or in a primarily, you know, a team with
[257.36 → 263.38] primarily software engineers, I think using these cloud ML services and black box sort of models,
[263.38 → 270.30] like from machine box, if you remember back to our episode, to using those sorts of things are
[270.30 → 275.06] incredibly powerful, where you can think about, you know, you're writing an application, and you can
[275.06 → 281.04] just think about, oh, I want to integrate, you know, speech to text, or I want to integrate, you know,
[281.16 → 287.10] image object recognition in my application, well, you don't have to build a model, you can just utilize
[287.10 → 291.54] one of these services. And I think that's incredibly powerful, where you can think more about the
[291.54 → 297.50] functionality that you're trying to enable rather than the, you know, the neural network
[297.50 → 302.90] architecture, or whatever it is. Absolutely. And for listeners, that was episode two on machine
[302.90 → 308.10] box, if they want to reference that. It was a great episode. So I imagine that that will change
[308.10 → 312.50] dramatically over the next few years with everyone trying to get this is maybe this is one of those
[312.50 → 318.10] moments where companies are still certainly trying to figure out how to incorporate AI into their
[318.10 → 322.74] strategy. And maybe we'll see a much higher uptake when that occurs. Yeah, for sure.
[322.74 → 330.06] So I ran across several articles. And the first one was called auto Keras, the killer of Google's
[330.06 → 336.12] auto ML. And, and, you know, part of what caught my attention was probably the provocative title.
[336.60 → 343.26] But they, they start off talking about kind of telling, again, what Google auto ML is, and that
[343.26 → 348.52] it's based on the neural architecture search that Google developed, which is really about searching
[348.52 → 355.30] for an optimal, an optimal neural network architecture or model to do a particular task on a given
[355.30 → 361.38] data set. And, and, and then they, they, I think the reason they introduced that is they wanted to
[361.38 → 366.86] say, hey, there's this new thing called auto Keras, which is an open source Python library. And that's
[366.86 → 374.60] what really caught my attention is one of the thesis of the article was that in addition to this auto Keras
[374.60 → 380.82] library, just being a great library to get into that it's open source. And they made a they
[380.82 → 387.06] really noted that if is there's anything that could give something like Google auto ML a run for its
[387.06 → 393.44] money, it's the fact that as you get these high quality alternatives in the open source world that
[393.44 → 398.72] are available, instead of, you know, paying Google $20 an hour to use that, you know, to use their auto
[398.72 → 404.28] ML implementation, that that is probably a trend that will be a powerful thing to come in the
[404.28 → 408.92] years ahead. And I know that both I love open source, and I know you do too. And so that really
[408.92 → 416.66] caught my attention. Yeah. And maybe, you know, that is what is partly factoring into this trend of,
[416.84 → 422.56] you know, people not using the cloud ML services as much as we might have thought, simply just because
[422.56 → 428.64] there's so many great open source packages out there, which a lot of them like, like you're kind of
[428.64 → 434.48] mentioning here, don't require you to think through an entire neural network architecture, but allow
[434.48 → 442.38] you to use a lot of things out of the box, utilize pre-trained models, utilize things as a service via
[442.38 → 448.66] JSON API or whatever it is. And so you know, maybe that is partly why that we're seeing that trend, I
[448.66 → 454.78] noticed that this one, you know, it's, it's, it's not from Google, it's, it's, but it is on, you know,
[454.78 → 460.22] open source on GitHub, it's extremely active, as it looks like it has, you know, over 2000 stars. And
[460.22 → 466.38] so yeah, good, good catch. So the next one that I found kind of follows in that trend as well,
[466.38 → 473.36] of open source tooling, and this one's called Neutron, I guess a play on neutron, I assume,
[473.68 → 479.86] but a lot of people are probably familiar with like tensor board, which is like a visualization tool
[479.86 → 485.10] attached to, or very tightly integrated with TensorFlow, which allows you to kind of visualize
[485.10 → 491.16] the architecture of your neural network, among with along with many other things. But this,
[491.24 → 498.32] this one caught my attention, just because of how, you know, how well supported all of these different
[498.32 → 504.74] types of models are from all sorts of various frameworks. So Neutron is also a way for you to
[504.74 → 509.82] visualize your neural network, the structure of it and various things about it. But it says,
[509.86 → 515.44] right now that it supports Onyx format, Keras, Core ML, TensorFlow Lite, it also has experimental
[515.44 → 523.02] support for Café, Cafe2, Monet, TensorFlow.js, and TensorFlow. And so this is really like a pretty
[523.02 → 527.68] cool thing. And, you know, a trend that I think I've mentioned on this podcast before that I really
[527.68 → 534.24] enjoying seeing in the community is this kind of idea of interoperability, where this is a tool for
[534.24 → 539.16] visualizing your neural network. And it doesn't really matter which framework you're using,
[539.16 → 543.84] but there's interoperability with a bunch of them. So it's definitely worth looking
[543.84 → 550.48] at, especially if you don't want to, you know, tie yourself into a particular framework or set of
[550.48 → 555.44] tools. Yeah, it looks I'm looking at the GitHub page while you're talking about it. And it looks
[555.44 → 563.00] pretty great. It has almost 1400 stars and 131 forks at the time that we're recording. And, you know,
[563.00 → 569.92] it looks very active in terms of there's a lot of recent updates to it. So in addition to all the
[569.92 → 575.14] the different frameworks it supports with models and stuff, I'm definitely going to try this
[575.14 → 581.82] one out myself. For sure. So then the next thing will take a little bit of a turn. I'm often really
[581.82 → 587.84] interested in some of the non-technical posts as well about how AI is affecting the world in different
[587.84 → 594.60] ways. And I came across one that is from Harvard Business Review, and it's called,
[595.10 → 602.00] What's the purpose of company in the age of AI? And, you know, I'm often talking about digital
[602.00 → 606.56] transformation in general and how AI affects that. And so that that caught my attention. But
[606.56 → 612.98] it was interesting to see Harvard Business Review seriously considering that with these new tools,
[612.98 → 619.00] how does that literally change the business functions technology aside that AI is introducing?
[619.36 → 625.56] And they kind of to summarize it, they kind of came down to that from a business strategy standpoint,
[625.80 → 631.52] AI was really going to have an effect in one of the four following ways. And one is really AI
[631.52 → 636.80] being used to exploit existing advantage and to make that existing advantage more pronounced.
[637.18 → 641.86] They also talked a lot about tradeoffs in terms of long term and short term. And we're all used to
[641.86 → 646.20] hearing about companies that get caught in the short term, you know, for stock market, for quarterly
[646.20 → 651.90] reporting and stuff like that, but that AI can be used to figure out what tradeoffs make sense for
[651.90 → 658.00] moving companies more into a long term perspective, and that there may be some insights there that would
[658.00 → 663.20] not otherwise be available. The third one that they mentioned really appealed to me, and I know it's
[663.20 → 667.84] going to appeal to you in that they're talking about, they define it as a moral or spiritual call to
[667.84 → 673.64] action. And I know, you explicitly always talked about AI for good. And that's a big important
[673.64 → 681.78] thing for me as well. And as I think about my future, and the organizations that I want to be part of,
[682.06 → 686.06] knowing that that organization stands for something more than just making a profit,
[686.06 → 692.70] is a motivating factor. So I found it fascinating to think of AI being used to promote
[692.70 → 700.56] that bettering the world approach. And then the final thing was really a kind of being the
[700.88 → 709.14] they use Steve Jobs, and Elon Musk as examples, is really people who are going to really meld the world
[709.14 → 713.92] into their own view, rather than trying to fit into the world. And you might say that that is innovation
[713.92 → 719.68] for the purpose of creating value. But I, I just like seeing this conversation where companies are
[719.68 → 724.40] recognizing how important this is, and recognizing it's not just another tech coming in, but it's
[724.40 → 728.88] actually something that's going to affect the core way they operate. Yeah, this, this is great. I think
[728.88 → 734.38] this is a really great perspective, especially the things like you mentioned, I mean, you know,
[734.50 → 739.66] the things that kind of pique my interest and, and coming from the AI for good perspective,
[739.66 → 743.86] in particular, where, you know, it talks about a moral or spiritual call to action.
[743.92 → 750.76] And I know I'm motivated, you know, primarily by, you know, my Christian faith in terms of infusing
[750.76 → 757.24] a morality into the technology that I build. And I had a lot of those conversations with people lately,
[757.24 → 764.44] where, you know, the, the morality, if there is some in AI is really driven by that of its creators.
[764.44 → 770.92] And so, you know, to, to be a part of the development of AI is also to be a part of that
[770.92 → 776.22] kind of moral piece of it. And we, we really need to be having those conversations. And it's great
[776.22 → 781.18] to see that there's a lot of people having those conversations in various circles. And it's great
[781.18 → 786.00] to see that. And, and I'm, I'm going to, I'm going to surprise and embarrass you and note to our
[786.00 → 792.44] listeners that Daniel is speaking at an upcoming conference that, that has a faith based perspective
[792.44 → 795.24] on technology. And what is it called, Daniel?
[795.24 → 801.16] It's called Faith Leads. It's in, it's in, in Nashville and having a lot of great conversations
[801.16 → 806.78] recently with, with people in that context, that's going to be a great conference. So I recommend you
[806.78 → 811.64] check, check that out if you're at all interested in that kind of intersection. But I know that there's
[811.64 → 816.40] a lot of people having these conversations. There's, I've seen a bunch of articles with people talking
[816.40 → 822.56] about, you know, how, how your world worldview and how your morality is kind of infused in the
[822.76 → 828.18] into the technology you build. And not only, you know, is, is a separate piece of who you are,
[828.18 → 833.86] but it actually can kind of mould in very naturally with the technology that you build. Um, I think
[833.86 → 839.92] that helps people also, you know, feel like, you know, they can put them, the their whole selves
[839.92 → 844.60] into the technology that they're building, um, and create a lot of passion for, for the things
[844.60 → 849.68] that they're building, um, which is, is super important, you know, and to finish that up,
[849.72 → 855.00] I, it's so good to see, I love, I, when I saw that you tweeted that, um, I wasn't surprised and
[855.00 → 859.84] I was very happy. And, um, and as we look and, and other people we know in the space are really
[859.84 → 867.12] focused on using AI for good. I think it's a fantastic counterpoint to the predictions of AI as a
[867.12 → 873.60] as a, as a scary thing in, in so many people's minds. Um, I just love seeing these great use cases
[873.60 → 877.98] for using this technology to, to better the world. And I hope that, uh, I hope that our listeners
[877.98 → 883.14] will help us, uh, spread that, uh, across, uh, the AI, uh, industry in general. Yeah. Yeah,
[883.14 → 887.96] for sure. And I, I definitely recommend, um, I mean, I think there are a couple of great links as well.
[887.96 → 894.74] I, I know in, in our episode three, we talked to, um, Amanda and Latina and Peter about the great work
[894.74 → 899.12] that they're doing with TensorFlow, helping African farmers. If you're, if you're at all interested,
[899.12 → 904.54] I just encourage you to listen to that episode. It's incredibly inspiring just to utilize the
[904.54 → 910.40] skills that we have for, for, uh, helping people improve their quality of life, um, in a real
[910.40 → 916.34] practical way. And, and, and literally saving lives, uh, in Africa there, I mean, literally saving lives.
[916.34 → 922.06] It was, that was, uh, it was an emotional episode, uh, uh, which, uh, so yeah, absolutely. They should go
[922.06 → 935.20] listen to that. This episode of practical AI is brought to you by hired. One thing people hate
[935.20 → 940.78] doing is searching for a new job. It's so painful to search through open positions on every job board
[940.78 → 946.76] under the sun. The process to find a new job is such a mess. If only there was an easier way.
[947.24 → 951.06] Well, I'm here to tell you there is our friends at hired have made it so that companies send you
[951.06 → 956.72] offers with salary benefits and even equity upfront. All you have to do is answer a few
[956.72 → 961.04] questions to showcase who you are and what type of job you're looking for. They work with more than
[961.04 → 966.76] 6,000 companies from startups to large publicly traded companies in 14 major tech hubs in North
[966.76 → 971.90] America and Europe. You get to see all of your interview requests. You can accept, reject, or make
[971.90 → 976.34] changes to their offer even before you talk with anyone. And it's totally free. This isn't going to
[976.34 → 979.60] cost you anything. It's not like you have to go there and spend money to get this opportunity.
[979.60 → 983.44] And if you get a job through hired, they're even going to give you a bonus. Normally it's $300,
[983.78 → 988.54] but because you're a listener of practical AI, it's $600 instead. Even if you're not looking for a
[988.54 → 994.36] job, you can refer a friend and hire will send you a check for $1,337 when they accept the job.
[994.54 → 999.66] As you can see, hire makes it too easy. Get started at hire.com slash practical AI.
[999.66 → 1018.68] Well, I'll bring us into the next thing that I found here, which is not totally unrelated,
[1018.68 → 1025.36] but in a different vein. And that's that Julia, the Julia team, if you're not familiar, Julia is
[1025.36 → 1033.36] another programming language that's very prominent in scientific computing. And in certain communities,
[1033.48 → 1038.46] especially, I think more on the academic sense, but it's kind of starting to filter into industry.
[1039.08 → 1045.76] And they just released version 1.0. So first, congrats to the Julia team. That's really great.
[1046.10 → 1052.74] And I have to say, if you haven't taken a look at Julia, just try a few examples. I think that
[1052.74 → 1058.58] you'll appreciate what they're trying to do. I was at Julia Con, I think it was last year,
[1058.94 → 1065.46] and the community is just really doing some amazing things in kind of distributed computing,
[1065.72 → 1072.52] large scale scientific computing, but also in terms of machine learning and utilizing GPUs and
[1072.52 → 1078.78] a bunch of different things. So we'll link to the blog post about Julia 1.0, but just encourage you to
[1078.78 → 1084.70] give the team congrats on Twitter and also try out a few examples if you've never used Julia.
[1085.04 → 1089.86] All right, I will definitely leap into that. That's a huge congratulation to hitting 1.0.
[1090.00 → 1095.76] I've also been watching Julia develop over the last few years, and it's just an impressive language,
[1095.76 → 1101.70] and it's coming along at a perfect time for that. I actually have my next article is actually
[1101.70 → 1105.56] kind of counterpoint to the Harvard Business Review, and I just mentioned before,
[1105.56 → 1112.72] this one is a blog post by a person named Ian Hogarth, if I'm pronouncing that right,
[1113.02 → 1118.66] called AI Nationalism. And the crux of it is, whereas the Harvard Business Review talked about
[1118.66 → 1126.30] the changes that companies are having to think about in terms of their operations, this blog talks
[1126.30 → 1135.22] about geopolitics and economic concerns and how AI is really going to be driving entirely new types of
[1135.22 → 1142.48] geopolitics in the years ahead. And to the point where it will transform not only economies, but
[1142.48 → 1150.56] military strategy and thinking. And the author actually goes so far as to suggest that AI policy
[1150.56 → 1157.20] may eventually be one of the most, if not the most important parts of government policy because of the
[1157.20 → 1165.04] profound impact that it has on government operations. And, you know, as we're at this moment where not only
[1165.04 → 1171.80] in the United States, but around the world, we're having all sorts of tumultuous politics with people on
[1171.80 → 1180.46] different sides. And obviously, it's at times, you know, very hotly contested. We seem to have left the
[1180.46 → 1189.04] period of politics being a slightly kinder, gentler thing to do in the past. But as we think about how
[1189.04 → 1196.02] AI may affect this, I just found that an interesting thought process. And he goes on in this article for
[1196.02 → 1200.42] in quite a lot of detail in a bunch of areas, far more than we can cover in the podcast. So I would
[1200.42 → 1204.78] certainly encourage listeners to take a read and be thoughtful about it.
[1204.78 → 1213.68] Yeah. And I definitely will take a look at that and take that perspective in. It's always good to
[1213.68 → 1218.30] have those, you know, those checks and balances and make sure you're hearing different sides of
[1218.30 → 1224.28] the story. I would agree with you in the sense that, especially in light of, I think, all of us,
[1224.34 → 1229.88] when we were watching, for example, the Facebook hearings at Congress, we're just kind of, at least
[1229.88 → 1234.56] all of us that work in this industry or in our maybe of a younger generation are just cringing
[1234.56 → 1240.10] at the fact of, you know, how little is understood at the government level about these new techniques
[1240.10 → 1245.84] and what's really driving, you know, really driving decision-making in industry, which is so
[1245.84 → 1249.86] different. And as that filters into government, I can't help but think that there's really going to
[1249.86 → 1255.84] be some profound changes at every level of government in terms of how they go about their
[1255.84 → 1260.68] decision-making and how they manage companies that are utilizing these technologies as well.
[1260.68 → 1267.68] Yeah, I agree. I remember a big part, aside from the actual reporting on the hearings themselves,
[1268.00 → 1274.90] some of the senators really, really took a beating when it became how apparent it was that they weren't
[1274.90 → 1280.96] familiar with the implications of these technologies. And we live in a time when we can't really afford
[1280.96 → 1285.68] to ignore these things anymore. I mean, they're not just technology, they affect the way we live our
[1285.68 → 1293.76] everyday life and what can and cannot happen. For sure. So now on to what really matters in the
[1293.76 → 1305.12] global context, which is video games. So I don't know if you're a video game connoisseur. I haven't
[1305.12 → 1312.94] been a big video gamer since the days of Super Nintendo, but there is this very popular game
[1312.94 → 1318.42] called Data. You probably almost everyone has heard of it. So I probably don't
[1318.42 → 1326.22] need to mention anything about it. But OpenAI developed five. My understanding is that it's
[1326.22 → 1333.12] it's called OpenAI 5, which is a team of five neural networks. So this is a team game. And so they have
[1333.12 → 1339.74] a team of five neural networks called OpenAI 5. And what happened is they played a tournament
[1339.74 → 1350.02] recently where they played against the team that says of the 99.95 percentile Data players.
[1350.40 → 1356.20] So essentially the some of the best in the world. Right. And they won, I think is two out of
[1356.20 → 1360.54] three. Correct me if I'm wrong in our community. But yeah, I think there's a lot of interesting
[1360.54 → 1365.14] things about this. I mean, it's just kind of entertaining in general, as these things are along
[1365.14 → 1369.80] with Alfaro and other things. But I also think it's pretty interesting that this is kind of a
[1369.80 → 1376.98] has that team play element. It also has an element in the game, which is like drafting, which I guess
[1376.98 → 1382.28] is considered to be a pretty hard challenge. And so there are a lot of facets to this that are pretty
[1382.28 → 1388.36] interesting. And so if either is you're interested in Data or if you're interested in these sorts of
[1388.36 → 1394.14] game playing neural networks, this is a unique one and one to look into. And
[1394.14 → 1398.66] there's some, you know, some videos online and all that good stuff that you can dive into.
[1399.06 → 1404.68] That's that's that's fascinating. It's funny how, and I'm not a big gamer either. So I won't
[1404.68 → 1412.20] really go too far because I'm out of my depth. But, you know, we've seen so many demonstrations of AI
[1412.20 → 1417.72] capabilities in recent years through gaming in different ways, in different capabilities. And so it's I'm
[1417.72 → 1424.30] always wondering what's going next. Yeah. And so this is a fascinating one, I guess. Do are we want to
[1424.30 → 1429.54] move into some learning resources at this point? Let's do it. Let's let's learn something.
[1429.78 → 1436.20] OK, sounds good. You want to go for it? Sure. Yeah. So what I was going to point out this week for people
[1436.20 → 1443.18] to try out is the PyTorch tutorials. So if you go is you just search for PyTorch tutorials, of course,
[1443.18 → 1448.42] we'll include it in the show notes. But search for that. The reason why I mentioned this is I'm
[1448.42 → 1453.92] actually going through some of these now and have been for a bit in preparation for some workshop
[1453.92 → 1459.06] materials that I'm putting together and some online course materials, which hopefully I'll be sharing in
[1459.06 → 1466.22] a future learning resources episode. But yeah, this is this has been really great for me to learn a
[1466.22 → 1471.52] little bit more about PyTorch, which I've thoroughly enjoyed working with PyTorch so far. It's been very
[1471.52 → 1477.50] natural, at least for me and in my background. And the tutorials really help with that. So
[1477.50 → 1483.14] they have a bunch, you know, deep learning with PyTorch, a 60-minute blitz PyTorch for former
[1483.14 → 1489.22] Torch users is probably not a ton of those. Maybe there is maybe there's more than I think. But
[1489.22 → 1494.38] there's also learning PyTorch with examples, transfer learning tutorial, data loading and processing
[1494.38 → 1499.04] tutorial. It's really, you know, practical things and they give you patterns. What I love is that
[1499.04 → 1504.38] they give you patterns that you can kind of reuse in your PyTorch programs. So you're, you know,
[1504.42 → 1510.18] you're not always starting from scratch. You kind of do a lot of copy and paste and go from
[1510.18 → 1515.12] there. Yeah, this is a really rich set of tutorials that they have here as I'm looking through it.
[1515.42 → 1521.76] It's in, you know, as we've talked about different frameworks over time. And, you know, we really have
[1521.76 → 1527.16] a great set of resources by each of the frameworks. This PyTorch one is awesome. You know,
[1527.16 → 1531.12] we've talked about TensorFlow and Keras and various others in the past. But, you know,
[1531.32 → 1536.06] if someone out there is listening and thinking about looking at this, you know, see one that
[1536.06 → 1541.44] that feels right and just dive into it. There are so many great examples where you can take whichever
[1541.44 → 1547.38] framework PyTorch or others and start doing stuff that just jump into the pool and start doing stuff.
[1547.38 → 1550.84] And you'll find that you can get productive pretty quickly there.
[1551.16 → 1556.66] Yeah, just jump in and try to run something that works right and then go from there. You don't have
[1556.66 → 1560.66] to feel like you need to understand every little piece of it before you run something.
[1561.06 → 1566.12] Just take one of these and try it, run it, see, see if it works and then try to start thinking about,
[1566.28 → 1571.46] oh, when could I use this and with my own data or what if I modified it to do this or that? And,
[1571.62 → 1573.42] you know, take that approach I think is really useful.
[1573.82 → 1580.10] Okay. I ran across something about it's almost it's almost meta about learning. It was on Life hacker
[1580.10 → 1585.66] and it's how to get started in machine learning, learning and robotics. And before we go on,
[1585.78 → 1594.56] you know, next week we're going to be interviewing Chris Rebellion on robotic perception using mask
[1594.56 → 1600.02] our CNN. And with that in mind is a future thing and thinking about crossing machine learning and
[1600.02 → 1605.26] robotics. This was interesting, not only because I knew that was coming, but also because
[1605.26 → 1611.30] it talks about these two gentlemen. And I'm not going to say their names because I'll butcher it
[1611.30 → 1616.92] terribly. The link is in the show notes, but it notes that one of them at least was 20 years old,
[1616.96 → 1622.34] maybe both of them. And they're there were trying to get started in this, and they were involved in a
[1622.34 → 1628.14] hackathon. And they just kind of talked about some of their lessons learned about how to get started in
[1628.14 → 1633.42] this field. And there's so many people, whether you're 20 or 40 or 60, there's so many people that are
[1633.42 → 1639.10] starting to move into this, that I thought that they had a really great perspective. And a couple
[1639.10 → 1643.96] of the key things that they said that if you're starting out, they refer to it as cross the streams.
[1643.96 → 1650.74] And what they meant by that is to think out of the box and not think about the problem you're
[1650.74 → 1654.98] trying to solve in the way everybody that came before you might have solved that with previous
[1654.98 → 1660.78] technologies, with new advancements happening so fast and with robotics, it may be it may not just be
[1660.78 → 1665.00] from an algorithmic standpoint, it might be the sensors that you're using and where sensors are
[1665.00 → 1671.12] applied and how they're combined and stuff. And they basically said, go for something that other
[1671.12 → 1675.68] people aren't necessarily doing and see if you can make it work. And then the next thing is they said
[1675.68 → 1680.92] is got an assignment and that is to make it real. They were involved in a hackathon. And in that
[1680.92 → 1686.68] perspective, you know, they had a set time limit to knock some code out. And, you know, that with that
[1686.68 → 1691.90] with that time approaching quickly, you have to produce whatever you can in a short amount of
[1691.90 → 1697.20] time. But that forced them to really think quickly and act on it quickly and see what they
[1697.20 → 1701.62] could produce. And that assignment, they said, made a big difference. And finally, when you have your
[1701.62 → 1706.22] assignment, they said, break down your project instead of being overwhelmed and saying, oh, my gosh,
[1706.22 → 1711.60] we've had we've we've we've taken this very ambitious assignment on in terms of how we're going to
[1711.60 → 1716.16] approach, and we have a set timeline. They just said, break it down to pieces, just like you would
[1716.16 → 1722.20] if you were a software engineer or any one of many other things. It's a project, and they're in a
[1722.20 → 1727.08] project is a big thing that's composed of lots of little things. And they said that they just they
[1727.08 → 1732.98] would basically divide and conquer the project and were able to use open source tools like
[1732.98 → 1739.12] Pandas, which I know you mentioned in our last conversation. And they were out able to turn out a good
[1739.12 → 1744.48] product. And I just thought it was a great attitude with some great practical advice for doing practical
[1744.48 → 1749.84] AI at an entry level. And I wanted to share that with our listeners. Awesome. Yeah. And there's
[1749.84 → 1755.06] a bunch of resources if you're looking, maybe you're not you don't have a hackathon near you or something
[1755.06 → 1760.64] like that. If you're looking for a project to get started with, or you feel like you've built up some
[1760.64 → 1766.00] skills and want to try them out, there are a bunch of ways to do that remotely as well. Of course, you can
[1766.00 → 1771.08] try out different competitions and stuff. But there's also things like data kind. If you're not
[1771.08 → 1778.80] familiar with that, that's that's a way to volunteer on real projects related to social good,
[1778.90 → 1783.06] things like poverty and global warming and public health. There are a lot of ways to get involved.
[1783.36 → 1788.14] And if you're is you're interested and need some help in finding some of those opportunities,
[1788.14 → 1794.10] make sure and pop over to our community. We have a Slack channel. You can find that at
[1794.10 → 1800.24] changelog.com slash community. There's a practical AI channel in that Slack. And we'd be happy
[1800.24 → 1805.50] to talk through some of those things. And or if you have, you know, interesting news coming your way,
[1805.58 → 1809.92] keep keeping us up to date with what you're finding interesting. And we'll look forward to hearing
[1809.92 → 1815.26] from you. Yeah, we do have a great group of listeners that are active on those in Slack.
[1815.66 → 1821.98] Also on LinkedIn, we have a practical AI group on LinkedIn, which we actively monitor. So there, and we're
[1821.98 → 1827.62] on social media. So there 's's a lot of great ways of reaching out. We are very accessible.
[1827.96 → 1831.74] And so don't hesitate to reach out to us and give us your feedback suggestions.
[1832.28 → 1836.36] And we're looking forward to those conversations. All right. Sounds good. Well, I'll see you
[1836.36 → 1845.10] or talk to you next week, Chris, about mask our CNN. And I'm looking forward to figuring out what that
[1845.10 → 1850.10] is and having that discussion. Me too. I'm looking forward to it. Have a good week, Daniel. Yeah, you too. Bye.
[1850.20 → 1850.42] Bye.
[1851.98 → 1857.24] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show, do us a
[1857.24 → 1862.02] favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on Twitter
[1862.02 → 1865.54] or social network, share a link with a friend, whatever you got to do, share the show with a
[1865.54 → 1870.04] friend if you enjoyed it. And bandwidth for changelog is provided by Vastly. Learn more at
[1870.04 → 1874.30] fastly.com. And we catch our errors before our users do here at changelog because of Rollbar.
[1874.56 → 1879.72] Check them out at rollbar.com slash changelog. And we're hosted on Linde cloud servers.
[1879.72 → 1883.14] Head to leno.com slash changelog. Check them out. Support this show.
[1883.56 → 1888.66] This episode is hosted by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith.
[1888.88 → 1894.78] The music is by Break master Cylinder. And you can find more shows just like this at changelog.com.
[1894.98 → 1898.98] When you go there, pop in your email address, get our weekly email, keeping you up to date
[1898.98 → 1904.38] with the news and podcasts for developers in your inbox every single week. Thanks for tuning in.
[1904.38 → 1905.32] We'll see you next week.
